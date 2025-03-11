document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ Stripe JS Loaded");

  // Get Stripe public key and client secret from JSON-script
  var stripePublicKey = JSON.parse(document.getElementById("id_stripe_public_key").textContent);
  var clientSecret = JSON.parse(document.getElementById("id_client_secret").textContent);

  if (!stripePublicKey || !clientSecret) {
      console.error("❌ Stripe keys are missing.");
      return;
  }

  var stripe = Stripe(stripePublicKey);
  var elements = stripe.elements();

  console.log("✅ Stripe initialized with key:", stripePublicKey);

  // Define custom styling for the card element
  var style = {
      base: {
          color: "#000",
          fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
          fontSize: "16px",
          "::placeholder": { color: "#aab7c4" },
      },
      invalid: { color: "#dc3545", iconColor: "#dc3545" },
  };

  // Create the Stripe card element
  var card = elements.create("card", { style: style });
  card.mount("#card-element");

  // Handle real-time validation errors
  card.on("change", function (event) {
      var displayError = document.getElementById("card-errors");
      displayError.textContent = event.error ? event.error.message : "";
  });

  // Handle form submission
  var form = document.getElementById("payment-form");
  var submitButton = document.getElementById("submit-button");

  if (!form || !submitButton) {
      console.error("❌ Payment form or submit button is missing.");
      return;
  }

  form.addEventListener("submit", function (event) {
      event.preventDefault();

      // Prevent multiple submissions
      if (submitButton.disabled) return;

      submitButton.disabled = true;
      submitButton.innerHTML = "Processing... <i class='fas fa-spinner fa-spin'></i>";

      console.log("🔄 Submitting checkout data before payment...");

      // Get CSRF token and save-info checkbox value
      var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
      var saveInfo = document.querySelector("#id-save-info")?.checked;

      // Prepare checkout data
      var postData = {
          csrfmiddlewaretoken: csrfToken,
          client_secret: clientSecret,
          save_info: saveInfo,
      };

      // Send checkout data to Django before confirming payment
      fetch("/checkout/cache_checkout_data/", {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams(postData),
      })
      .then(response => response.json())
      .then(data => {
          console.log("✅ Checkout data cached:", data);

          // Retrieve customer details from form
          var fullName = document.querySelector("#id_full_name")?.value || "";
          var email = document.querySelector("#id_email")?.value || "";
          var phoneNumber = document.querySelector("#id_phone_number")?.value || "";
          var address = document.querySelector("#id_address")?.value || "";
          var city = document.querySelector("#id_town_or_city")?.value || "";
          var country = document.querySelector("#id_country")?.value || "";

          console.log("🛒 Billing details:", fullName, city);

          // Confirm payment with Stripe
          return stripe.confirmCardPayment(clientSecret, {
              payment_method: {
                  card: card,
                  billing_details: {
                      name: fullName,
                      email: email,
                      phone: phoneNumber,
                      address: {
                          line1: address,
                          city: city,
                          country: country,
                      },
                  },
              },
          });
      })
      .then(function (result) {
          if (result.error) {
              document.getElementById("card-errors").textContent = result.error.message;
              resetButton();
          } else {
              console.log("✅ Payment succeeded, submitting form...");
              form.submit(); // Only submit form after successful payment
          }
      })
      .catch(error => {
          console.error("❌ Error processing payment:", error);
          resetButton();
      });
  });

  // Helper function to reset submit button
  function resetButton() {
      submitButton.disabled = false;
      submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
  }
});
