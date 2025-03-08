document.addEventListener("DOMContentLoaded", function () {
  console.log("Stripe JS loaded");

  // Ensure Stripe public key is available
  if (!window.stripePublicKey) {
    console.error("Stripe public key is missing.");
    return;
  }

  // Initialize Stripe and Elements
  var stripe = Stripe(window.stripePublicKey);
  console.log("STRIPE: ", stripe)
  var elements = stripe.elements();

  console.log("Stripe initialized with key:", window.stripePublicKey);

  // Custom styling for Stripe card element
  var style = {
    base: {
      color: "#000",
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSize: "16px",
      "::placeholder": { color: "#aab7c4" },
    },
    invalid: { color: "#dc3545", iconColor: "#dc3545" },
  };

  // Select the card element container
  var cardElement = document.getElementById("card-element");

  if (!cardElement) {
    console.error("Card element container (#card-element) is missing in the HTML.");
    return;
  }

  // Create and mount the Stripe card input
  var card = elements.create("card", { style: style });
  card.mount("#card-element");

  console.log("card: ", card)


  // Display errors on card input change
  card.on("change", function (event) {
    var displayError = document.getElementById("card-errors");
    if (displayError) {
      displayError.textContent = event.error ? event.error.message : "";
    }
  });

  // Handle form submission
  var form = document.getElementById("payment-form");
  var submitButton = document.getElementById("submit-button");

  console.log("form: ", form)
  console.log("submitButton: ", submitButton)


  if (!form || !submitButton) {
    console.error("Payment form or submit button is missing.");
    return;
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Prevent multiple submissions
    if (submitButton.disabled) return;

    submitButton.disabled = true;
    submitButton.innerHTML = "Processing... <i class='fas fa-spinner fa-spin'></i>";
    
    console.log("submitButton: ", submitButton)

    // Ensure clientSecret is available
    if (!window.clientSecret) {
      document.getElementById("card-errors").textContent =
        "Payment error. Please refresh and try again.";
      resetButton();
      return;
    }

    // Get customer details from form
    var fullName = document.querySelector("#id_full_name")?.value || "";
    var email = document.querySelector("#id_email")?.value || "";
    var phoneNumber = document.querySelector("#id_phone_number")?.value || "";
    var address = document.querySelector("#id_address")?.value || "";
    var city = document.querySelector("#id_town_or_city")?.value || "";
    var country = document.querySelector("#id_country")?.value || "";
    
    console.log("fullName: ", fullName)
    console.log("city: ", city)


    // Confirm payment with Stripe
    stripe.confirmCardPayment(window.clientSecret, {
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
        receipt_email: email,
      })
      .then(function (result) {
        if (result.error) {
          document.getElementById("card-errors").textContent =
            result.error.message;
          resetButton();
        } else {
          console.log("FORM IS SUBMITTING!")
          form.submit(); // Proceed with form submission after successful payment
        }
      });
  });

  // Helper function to reset the submit button
  function resetButton() {
    submitButton.disabled = false;
    submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
  }
});


// document.addEventListener("DOMContentLoaded", function () {
//   console.log("Stripe JS loaded");

//   if (typeof stripePublicKey === "undefined" || !stripePublicKey) {
//     console.error("Stripe public key is missing.");
//     return;
//   }

//   var stripe = Stripe(stripePublicKey);
//   var elements = stripe.elements();

//   console.log("Stripe with key:", stripePublicKey);

//   var style = {
//     base: {
//       color: "#000",
//       fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
//       fontSmoothing: "antialiased", // "antialiased" or "auto"
//       fontSize: "16px",
//       "::placeholder": { color: "#aab7c4" },
//     },
//     invalid: {
//       color: "#dc3545",
//       iconColor: "#dc3545",
//     },
//   };

//   var card = elements.create("card", { style: style });
//   card.mount("#card-element");

//   // Function to check if #card-element is Mounted
//   function isElementMounted() {
//     return document.getElementById("card-element").childNodes.length > 0;
//   }

//   card.on("change", function (event) {
//     var displayError = document.getElementById("card-errors");
//     displayError.textContent = event.error ? event.error.message : "";
//   });

//   var form = document.getElementById("payment-form");
//   var submitButton = document.getElementById("submit-button");

//   form.addEventListener("submit", function (event) {
//     event.preventDefault();

//     // Prevent multiple submissions
//     if (submitButton.disabled) {
//       return;
//     }

//     submitButton.disabled = true;
//     submitButton.innerHTML =
//       "Processing...<i class='fas fa-spinner fa-spin'></i>";

//     // Check if #card-element is still mounted
//     if (!isElementMounted()) {
//       console.log("Stripe card element is not mounted.");
//       document.getElementById("card-errors").textContent =
//         "Payment failed. Please try again.";
//       submitButton.disabled = false;
//       submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
//       return;
//     }

//     if (typeof clientSecret === "undefined" || !clientSecret) {
//       document.getElementById("card-errors").textContent =
//         "Payment failed. Please try again.";
//       submitButton.disabled = false;
//       submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
//       return;
//     }

//     var fullName = document.querySelector("#id_full_name").value;
//     var email = document.querySelector("#id_email").value;
//     var phoneNumber = document.querySelector("#id_phone_number").value;
//     var address = document.querySelector("#id_address").value;
//     var city = document.querySelector("#id_town_or_city").value;
//     var country = document.querySelector("#id_country").value;  //Stripe requires a 2-character country code ISO

//     stripe
//       .confirmCardPayment(clientSecret, {
//         payment_method: { 
//           card: card,
//           billing_details: {
//             name: fullName,
//             email: email,
//             phone: phoneNumber,
//             address: {
//               line1: address,
//               city: city,
//               country: country,
//             },
//           },
//         },
//         receipt_email: email,
//       })
//       .then(function (result) {
//         if (result.error) {
//           document.getElementById("card-errors").textContent =
//             result.error.message;
//           submitButton.disabled = false;
//           submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
//         } else {
//             form.submit();
//         }
//       });
//   });
// });
