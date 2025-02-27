document.addEventListener("DOMContentLoaded", function () {
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();
    var card = elements.create("card");
    card.mount("#card-element");

    card.on("change", function (event) {
        var displayError = document.getElementById("card-errors");
        displayError.textContent = event.error ? event.error.message : "";
    });

    var form = document.getElementById("checkout-form");
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        document.getElementById("submit-button").disabled = true;

        stripe.confirmCardPayment(clientSecret, {
            payment_method: { card: card }
        }).then(function (result) {
            if (result.error) {
                document.getElementById("card-errors").textContent = result.error.message;
                document.getElementById("submit-button").disabled = false;
            } else {
                form.submit();
            }
        });
    });
});
