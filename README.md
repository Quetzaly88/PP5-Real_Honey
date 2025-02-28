# PP5-Real_Honey
navbar: https://getbootstrap.com/docs/4.0/components/navbar/

Bootstrap 4 Card container: https://bbbootstrap.com/snippets/card-container-48980697

bootstrap pagination: https://getbootstrap.com/docs/4.0/components/pagination/



FUTURE IMPLEMENTATION: Bulk product import via CSV
This feature can be implemented in the future to allow administrators to upload product details through a CSV file, reducing the time and effort required for manual data entry. For this we will need to immport csv. This won't be done in this project now because this project is in a small scale, otherwise, it can be implemented in the future.
https://docs.djangoproject.com/en/5.1/howto/outputting-csv/
  
color palette generator http://colormind.io/image/

footer bootstrap snippet https://mdbootstrap.com/snippets/standard/mdbootstrap/2885115



Future implementation product size:
Currently, the product size options are defined as a set of predefined choices in the SIZE_CHOICES tuple. This approach ensures consistency and simplifies management for standard product sizes like 450g and 600g. However, it may require code updates every time a new size (e.g., 50g or 700g) needs to be added.



SETTINGS FOR REAL HONEY PROJECT (cart/discounts)
   In this project, I define custom settings in settings.py to configure advanced shopping cart functionality as delivery fees, discounts and session behaviour. This settings help centralize configuration and make the codebase more flexible. 

# Custom Shopping cart settings: 
    - Custom settings are accessed using django.config.settings
    * from django.conf import settings
      free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD


FREE_DELIVERY_THRESHOLD = 50.00 *Free delivery for orders above this value
STANDARD_DELIVERY_PERCENTAGE = 10 *Delivery fee as a percentage of the total

# Session Settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_SAVE_EVERY_REQUEST = True

# Messages Framework Settings
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',  # Bootstrap error message
}

Documentation: 
https://docs.djangoproject.com/en/5.1/topics/settings/
https://docs.djangoproject.com/en/5.1/topics/http/sessions/#settings
https://docs.djangoproject.com/en/5.1/ref/settings/#std:setting-MESSAGE_TAGS
https://docs.djangoproject.com/en/5.1/ref/settings/


**STRIPE PAYMENT INTEGRATION**
Overview:
   Stripe payment processing in the project. Stripe is used to securely handle online payments for customer orders. 
1. Pip Install Stripe
2. Open an account in Stripe to obtain API Keys. This keys are added in the main settings.py.
3. Modify checkout/views.py
   - Creating a Stripe PaymentIntent
   - Passing the client secret to the frontend
   - Handling order creation after successful payment. 
4. Modify checkout.html
   - Ensure that checkout.html passes the client_secret to Javascript
5. Create stripe.js for Payment Processing.
   - Path: checkout/static/js/stripe.js (https://chatgpt.com/)

Conclusion: 
   This integration allows secure payment processing using Stripe Elements. It ensures that: 
   - No sensitive card details are stored on the server.
   - Secure and efficient transactions.
   - Real-time validation and error handling. 


** About Secret Keys **
Security improvements made to protect sensitive API keys and secret credentials. 

* Installation of python-decouple:
  The python-decouple helps manage environment variables securely by loading them from a .env file instead of hardcoding sensitive information in settings.py.
  
  Why using python-decouple? 
  - Keep secret keys secure by storing them in .env and adding .env in .gitignore. This prevent accidental leaks when pushing code to Github. 

  - Improves mantainability by separating configuration from the codebase. This makes it easier to switch environments (development, staging, production). 

  - Prevent Security Risks. Python-decouple ensures secrets are not stored in version control (Git).

  How we used python decouple? 
  1. Install: pip install python-decouple
  2. Create a .env file in project root and add it to .gitignore
  3. Add secret keys to .env: 

      SECRET_KEY='your-django-secret-key'
      STRIPE_PUBLIC_KEY='your-public-key-here'
      STRIPE_SECRET_KEY='your-secret-key-here'
      STRIPE_WEBHOOK_SECRET='your-webhook-secret-here' # if needed
      DEBUG=True  # Change to False in production

4. Load the secrets in settings.py

      import os
      from decouple import config  # Import python-decouple

      SECRET_KEY = config("SECRET_KEY")  # Securely fetch secret key

      STRIPE_PUBLIC_KEY = config("STRIPE_PUBLIC_KEY")
      STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
      STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET") # if needed
      <!-- or debug=True???? -->
      <!-- DEBUG = config("DEBUG", default=False, cast=bool)   -->

      https://pypi.org/project/python-decouple/
      https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html
      
