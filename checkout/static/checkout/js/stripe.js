document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Stripe JS Loaded");

    // Get Stripe public key and client secret from JSON-script
    var stripePublicKeyElement = document.getElementById("id_stripe_public_key");
    var clientSecretElement = document.getElementById("id_client_secret");

    if (!stripePublicKeyElement || !clientSecretElement) {
        console.error("❌ Stripe keys are missing.");
        return;
    }

    var stripePublicKey = JSON.parse(stripePublicKeyElement.textContent);
    var clientSecret = JSON.parse(clientSecretElement.textContent);

    if (!stripePublicKey || !clientSecret) {
        console.error("❌ Invalid Stripe public key or client secret.");
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

    // Ensure Stripe card is mounted before proceeding
    var cardElement = document.getElementById("card-element");

    if (!cardElement) {
        console.error("❌ Card element container is missing.");
        return;
    }

    card.mount("#card-element");

    console.log("🔍 Verifying if Stripe card element is mounted...");
    setTimeout(() => {
        if (!document.querySelector(".StripeElement")) {
            console.error("❌ Stripe card element is not mounted.");
        } else {
            console.log("✅ Stripe card element is mounted:", document.querySelector(".StripeElement"));
        }
    }, 2000);

    // Handle real-time validation errors
    card.on("change", function (event) {
        var displayError = document.getElementById("card-errors");
        displayError.textContent = event.error ? event.error.message : "";
        console.log("🔄 Card input changed...");
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

        console.log("🛒 Checking form submission...");
        console.log("🔍 Checking if Stripe card element is still in the DOM before confirming payment...");

        if (!document.getElementById("card-element")) {
            console.error("❌ Card element is missing before confirming payment.");
            resetButton();
            return;
        }

        console.log("✅ Stripe card element is still present.");

        // Prevent multiple submissions
        if (submitButton.disabled) return;

        submitButton.disabled = true;
        submitButton.innerHTML = "Processing... <i class='fas fa-spinner fa-spin'></i>";

        console.log("🔄 Submitting checkout data before payment...");

        // Get CSRF token and save-info checkbox value
        var csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');
        if (!csrfTokenElement) {
            console.error("❌ CSRF token not found.");
            resetButton();
            return;
        }

        var csrfToken = csrfTokenElement.value;
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

            // Ensure the card element is still present in DOM before proceeding
            if (!document.getElementById("card-element")) {
                console.error("❌ Card element disappeared.");
                resetButton();
                return;
            }

            // Retrieve customer details from form
            var fullName = document.querySelector("#id_full_name")?.value || "";
            var email = document.querySelector("#id_email")?.value || "";
            var phoneNumber = document.querySelector("#id_phone_number")?.value || "";
            var address = document.querySelector("#id_address")?.value || "";
            var city = document.querySelector("#id_town_or_city")?.value || "";
            var country = document.querySelector("#id_country")?.value || "";

            console.log("🛒 Billing details:", { fullName, email, phoneNumber, address, city, country });

            // Check again before processing payment
            if (!document.getElementById("card-element")) {
                console.error("❌ Card element has disappeared before confirming payment!");
                resetButton();
                return;
            } else {
                console.log("✅ Card element is still present before confirming payment.");
            }

            // Confirm payment with Stripe, ensuring we use the exact element reference
            return stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: elements.getElement("card"), // Using getElement ensures we're referencing the right card element
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
                console.error("❌ Payment error:", result.error.message);
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
