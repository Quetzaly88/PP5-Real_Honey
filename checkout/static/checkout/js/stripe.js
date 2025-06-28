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
    
    var style = {
        base: {
            color: "#000",
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSize: "16px",
            "::placeholder": { color: "#aab7c4" },
        },
        invalid: { color: "#dc3545", iconColor: "#dc3545" },
    };

    var card = elements.create("card", { style: style });
    card.mount("#card-element");

    card.on("change", function (event) {
        var displayError = document.getElementById("card-errors");
        displayError.innerHTML = event.error ? `<span class="icon"><i class="fas fa-times"></i></span> <span>${event.error.message}</span>` : "";
    });

    var form = document.getElementById("payment-form");
    var submitButton = document.getElementById("submit-button");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        submitButton.disabled = true;
        submitButton.innerHTML = "Processing... <i class='fas fa-spinner fa-spin'></i>";

        var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        var saveInfo = document.querySelector("#id-save-info")?.checked || false;

        var postData = {
            csrfmiddlewaretoken: csrfToken,
            client_secret: clientSecret,
            save_info: saveInfo,
        };

        fetch("/checkout/cache_checkout_data/", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams(postData),
        })
        .then(response => response.json())
        .then(data => {
            console.log("✅ Checkout data cached:", data);

            var fullName = document.querySelector("#id_full_name")?.value || "";
            var email = document.querySelector("#id_email")?.value || "";
            var phoneNumber = document.querySelector("#id_phone_number")?.value || "";
            var address = document.querySelector("#id_address")?.value || "";
            var city = document.querySelector("#id_town_or_city")?.value || "";
            var country = document.querySelector("#id_country")?.value || "";
            var postal_code = document.querySelector("#id_postcode")?.value || "";

            return stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: elements.getElement("card"),
                    billing_details: {
                        name: fullName,
                        email: email,
                        phone: phoneNumber,
                        address: {
                            line1: address,
                            city: city,
                            country: country,
                            postal_code: postal_code,
                        },
                    },
                },
            });
        })
        .then(function (result) {
            if (result.error) {
                document.getElementById("card-errors").innerHTML = `<span class="icon"><i class="fas fa-times"></i></span> <span>${result.error.message}</span>`;
                submitButton.disabled = false;
                submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
            } else {
                console.log("✅ Payment succeeded, submitting form...");
                form.submit();
            }
        })
        .catch(error => {
            console.error("❌ Error processing payment:", error);
            submitButton.disabled = false;
            submitButton.innerHTML = "Pay Now <i class='fas fa-lock'></i>";
        });
    });
});
