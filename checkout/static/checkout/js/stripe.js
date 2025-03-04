document.addEventListener("DOMContentLoaded", function () {
  console.log("Stripe JS loaded");

  if (typeof stripePublicKey === "undefined" || !stripePublicKey) {
    console.error("Stripe public key is missing.");
    return;
  }

  var stripe = Stripe(stripePublicKey);
  var elements = stripe.elements();
  console.log("Stripe with key:", stripePublicKey);

  var style = {
    base: {
      color: "#000",
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSmoothing: "antialiased", // "antialiased" or "auto"
      fontSize: "16px",
      "::placeholder": {
        color: "#aab7c4",
      },
    },
    invalid: {
      color: "#dc3545",
      iconColor: "#dc3545",
    },
  };

  var card = elements.create("card", { style: style });
  card.mount("#card-element");

  card.on("change", function (event) {
    var displayError = document.getElementById("card-errors");
    displayError.textContent = event.error ? event.error.message : "";
  });

  var form = document.getElementById("payment-form");
  var submitButton = document.getElementById("submit-button");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    submitButton.disabled = true;
    submitButton.innerHTML =
      "Processing...<i class='fas fa-spinner fa-spin'></i>";

    if (typeof clientSecret === "undefined" || !clientSecret) {
      document.getElementById("card-errors").textContent =
        "Payment failed. Please try again.";
      submitButton.disabled = false;
      submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
      return;
    }

    stripe
      .confirmCardPayment(clientSecret, {
        payment_method: { card: card },
      })
      .then(function (result) {
        if (result.error) {
          document.getElementById("card-errors").textContent =
            result.error.message;
          submitButton.disabled = false;
          submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
        } else {
          form.submit();
        }
      });
  });
});
