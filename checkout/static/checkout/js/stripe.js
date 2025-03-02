document.addEventListener("DOMContentLoaded", function () {
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();

    // Define Stripe card style
    var style = {
        base: {
            color: "#000",
            fontFamily: '"Roboto", sans-serif',
            fontSmoothing: "antialiased",
            fontSize: "16px",
            "::placeholder": {
                color: "#aab7c4"
            }
        },
        invalid: {
            color: "#dc3545",
            iconColor: "#dc3545"
        }
    };


    var card = elements.create("card", { style: style });
    card.mount("#card-element");

    card.on("change", function (event) {
        var displayError = document.getElementById("card-errors");
        displayError.textContent = event.error ? event.error.message : "";
    });

    var form = document.getElementById("checkout-form");
    var submitButton = document.getElementById("submit-button");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        submitButton.disabled = true;
        submitButton.innerHTML = "Processing...<i class='fas fa-spinner fa-spin'></i>";

        stripe.confirmCardPayment(clientSecret, {
            payment_method: { card: card }
        }).then(function (result) {
            if (result.error) {
                document.getElementById("card-errors").textContent = result.error.message;
                submitButton.disabled = false;
                submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
            } else {
                form.submit();
            }
        });
    });
});
