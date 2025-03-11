# PP5-Real_Honey - Buy Local, Authentic Honey - Online

**1. Key Project Information**

Project Name: PP5_Real_Honey
   * 1.1 Description
      Real Honey is a user-friendly and scalable online marketplace that connects local beekeepers with customers, allowing them to purchase honey and honey products from the online store. 

      * Key Goal
      To provide a seamless and enjoyable shopping experience while supporting local beekeepers.

      * Target Audience
      - Nature and health-conscious individuals that love honey. 
      - Online shoppers seeking convenience
      - Supporters of local beekeepers

      * Live Project:
      URL: 

      * Dummy Card for Testing: 
      - Card Number:  4242 4242 4242 4242
      - Expiry: 01/34
      - CVC: 123
      - ZIP: 12345

      * Test failing transactions *

      Developer: 
      Andrea Nilsson Coronado

      Note: This project is for educational purposes only!

**2. Table of Contents**

1. Key Project Information

2. Table of Contents

3. User Experience (UX)

4. Features

5. Marketing

6. Validation, Testing & Bugs

7. Deployment

8. Technologies & Credits

9. Handling Product Images

10. Additional Resources

11. Future Implementations

12. User Stories: 

13. Resources for project development. 

14. Issues



**3. User Experience (UX)**

   *3.1 The Strategy Plane*
      3.1.1 The Idea:
         To create an e-commerce platform that offers locally sourced honey and honey-related products with a focus on authenticity and sustainability. 

      3.1.2 The Ideal User
         - Interested in natural and organic products.
         - Health- conscious individuals
         - Enthisiasts of unique honey flavours.
         - Supporters of sustainable and ethical sourcing.
         - Online shoppers looking for a convenient experience. 

      3.1.3 Site Goals
         - Provide a seamless shopping experience.
         - Ensure users can easily browse and purchase honey.
         - Offer transparency about honey origins and beekeepers
         - Implement strong SEO. 

      3.1.4 Epics and user stories: 
         [Link or resume of useer stories]

   *3.2 The Scope Plane*
      3.2.1 Features to be implemented.
         - Product Listings & Categorization
         - Sorting and Filtering of products
         - Cart and Checkout
         - User Authentication
         - SEO
         - Responsive Design

   *3.3 The Structure Plan*
         - Site map
         - Database Schema

   *3.4 Wireframes*
         [link or imgs]

   *3.5 The Surface Plan*
         - Logo
         - Color Palette
         - Fonts
         - Icons (fontawsome)
         - Images

**4. Features**
   *4.1 Core Features:*
         - Header with navigation and logo.
         - Footer with contact info, adress and social media engagement. 
         - Wishlist management
         - Order History
         - Search functionality
         - Notifications (on-screen and email)

   *4.2 Pages:*
         - Landing page. Home.
         - Product list page
         - Product Detail page.
         - Checkout Page:
            
         - Profile management 

         - Settings for REal Honey Project (Cart/Discounts):
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

   *4.3 Future Implementations:*
      4.3.1 Bulk product import via CSV:
         This feature can be implemented in the future to allow administrators to upload product details through a CSV file, reducing the time and effort required for manual data entry. For this we will need to immport csv. This won't be done in this project now because this project is in a small scale, otherwise, it can be implemented in the future.
         https://docs.djangoproject.com/en/5.1/howto/outputting-csv/

      4.3.2 Future implementation product size:
         Currently, the product size options are defined as a set of predefined choices in the SIZE_CHOICES tuple. This approach ensures consistency and simplifies management for standard product sizes like 450g and 600g. However, it may require code updates every time a new size (e.g., 50g or 700g) needs to be added.

      4.3.3 Aditional Future Enhancements:
         - Product Inventory management
         - Improved search and filtering options
         - Wishlist functionality
         - Order tracking and status updates
         - Customer reward points and discounts
         - AI based product recomendations 

**5. Marketing**
   *5.1 Social Media Presence:*
         - Active engagement on platforms like Facebook, instagram and youtube.
         - Social media buttons integrated on all the website. 
         - Community engagement through newsletters. 

   *5.2 Search Engine Optimization (SEO)*
         - SEO- friendly URLs and meta tags
         - Structured content for better search engine indexing.
         - Email marketing campaigns for customer engagement. 

**6. Validation, Testing & Bugs
   *6.1 Validation*
      - HTML, CSS and JavaScript validation
      - Accessibility testing
      - SEO validation using Google Tools

   *6.2 Testing*
      - Manual and automated tests.
         - Performed bu using print(), console.log() and manual testing. 
      - User experience Testing
      - Payment gateway testing.
         - Usind dummy credit card information. 

   *6.3 Bugs*
      - Issues with Stripe due to missing postload.js in base.html. 
      - Several changes on models for better performance. 
      - Fixed checkout and Stripe integration: Ensured that cart items persisted untill payment confirmation.
      - Add default favicon to avoid 404 error. 
      - Fixed error in Order and OrderLineItem models to prevent AttributeError.
      - Resolved pagination issue and wishlist items to transfer correctly to cart. 
      - Resolved issue of best sellers and featured products not seen in home page. 
      - Reinstallation of Django that was causing problems for lack of compatibility....

   

**7. Deployment**
   *7.1 Deployment Steps*
      - Transfer progress from IDE to GitHub
      - Deployment to cloud Heroku.

   *7.2 Deployment Prerequisites*
      - Email Configuration
      - Database Setup
      - Cloud Storage Configuration
      - Payment Gateway Integration


**8. Technologies & Credits**
   *8.1 Technologies:*

      - Django (Backend Framework). 

      - Allauth:
         To setup an entire authentication sistem and user account sistem 
      - Python (Core Programming Language)
      - HTML, CSS, JavaScript (Frontend Technologies)
      - Bootstrap (UI Framework)
      - PostgreSQL (Database)
      - Flake8(Debugging)

      [Python-Decouple:]
         Secret Keys & Security Improvements: Security improvements made to protect sensitive API keys and secret credentials.

            Why Use Python-Decouple? 
               - Keeps secret keys secure by storing them in .env (added to .gitignore)
               - Improves maintainability by separating configuration from the codebase.
               - Prevents security risks by avoiding storing secrets in vesion control. 

            Installation of python-decouple:
               The python-decouple helps manage environment variables securely by loading them from a .env file instead of hardcoding sensitive information in settings.py.

            How I used python decouple? 
               1. Install: pip install python-decouple
               2. Create a .env file in project root and add it to .gitignore
               3. Add secret keys to .env: 
               SECRET_KEY='your-django-secret-key'
               STRIPE_PUBLIC_KEY='your-public-key-here'
               STRIPE_SECRET_KEY='your-secret-key-here'
               STRIPE_WEBHOOK_SECRET='your-webhook-secret-here' # if needed
               DEBUG=True  # Change to False in production

            Load the secrets in settings.py:
               import os
               from decouple import config  # Import python-decouple
               SECRET_KEY = config("SECRET_KEY")  # Securely fetch secret key
               STRIPE_PUBLIC_KEY = config("STRIPE_PUBLIC_KEY")
               STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
               STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET") # if needed
               DEBUG = config("DEBUG", default=False, cast=bool). **(Toggle debug will be changed in .env)
            
      [Stripe Payment Integration:]
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
               - Path: checkout/static/js/stripe.js

         Conclusion: 
               This integration allows secure payment processing using Stripe Elements. It ensures that: 
                  - No sensitive card details are stored on the server.
                   - Secure and efficient transactions.
                   - Real-time validation and error handling. 

      [Stripe Webhooks Instalation.]
         Part 1: Installing Stripe CLI
            1. Open Your Mac Terminal
               - Press `Command + Space` to open **Spotlight Search**.  
               - Type **Terminal** and press **Enter**.  

            2. Install Homebrew (If Not Already Installed)
            Homebrew is a package manager for macOS that simplifies software installations.
               -  Verify Homebrew Installation:
               bash: brew --version

            3. Install Stripe CLI
            bash: brew install stripe/stripe-cli/stripe

            4. Verify installation
            bash: stripe version. 
               If Stripe CLI is installed correctly, it will return a version number (e.g., 1.23.5 or higher).

         Part 2: Logging into Stripe CLI
            1. Authenticate with Stripe. To log in and authenticate your Stripe account, run:
            bash: stripe login
               This will open a browser window prompting you to log in to your Stripe account.
               Follow the instructions to complete the authentication.

               Once logged in, Stripe CLI will be linked to your account for testing webhooks and payments.

         Part 3: Troubleshooting Permission Errors
            If you encounter "permission denied" errors during login, follow these steps:

            1. Check Permissions of ~/.config Directory
            bash: ls -ld ~/.config
               If the owner is root instead of your username, change it. Replace yourusername with your actual macOS username:
            bash: sudo chown -R yourusername:staff ~/.config

            2.  Verify Updated Permissions
            bash: ls -ld ~/.config

            3.  Retry Logging In
            bash: stripe login

            * Note: Stripe CLI login keys expire every 90 days. You will need to log in again using the same command.

         Part 4: Testing Webhooks Using Stripe CLI
            1. Preparing Your Code

               - Modify checkout/webhooks.py to confirm the webhook is working:

                  print('Success!')
                  return HttpResponse(status=200)

                  This will print "Success!" and return a 200 OK response when the webhook is triggered.

               - Modify settings.py to include localhost in ALLOWED_HOSTS:

                   ALLOWED_HOSTS = ['localhost', '127.0.0.1']
            
            2.  Open Three Terminals

               * Python server	Runs Django (python manage.py runserver)
               * Stripe portal	Generates a webhook listener (stripe listen --forward-to localhost:8000/webhook/)
               * Testing terminal	Sends Stripe webhook triggers (e.g., stripe trigger payment_intent.succeeded)

         Part 5. Steps to Test Webhooks
            1. Start Django Server
               bash: python manage.py runserver
            2. Start Stripe Webhook Listener
               bash: stripe listen --forward-to localhost:8000/webhook/
            3. Store the Signing Secret in env.py
               - os.environ.setdefault('STRIPE_WH_SECRET', 'your signing secret here')
            4. Restart Django Server
            5.  Trigger a Test Webhook in the Third Terminal
               bash:
                  stripe trigger payment_intent.created
                  stripe trigger payment_intent.succeeded
                  stripe trigger payment_intent.payment_failed
                  stripe trigger charge.succeeded
                  stripe trigger charge.failed
               * You should see "Trigger succeeded" in the terminal.

         Part 6: Confirm Webhook Events in Stripe Dashboard.
            - Log into Stripe Dashboard
            - Click Developers > Events
            - Select the latest event and scroll down to Webhook CLI responses
            - Expand the response and confirm it shows 200 OK and correct webhook messages

         Part 7: Verify Webhooks in Django
            1. Check the Python Server Terminal
            
                  * Webhook received: payment_intent.succeeded 
                  Success!

                  * This confirms that the webhook was received successfully.



               *8.2 Credits:*
                  [Code-Institute tutors]: 
                  [Chat GPT]: I used AI for the Stripe set up because of time management and how clear were the steps to follow, 

**9. Additional Resources**
   *Useful links for Django, Bootstrap and Stripe documentation 


**12. User Stories Summary**
   This project implements key e-commerce functionalities, focusing on product browsing, user authentication, shopping cart management, wishlist features, cheeckout..............

      *User Story 1: Product Listing: Shoppers can browse a list of products with sorting, pagination, and responsive design. 
         - Displays product details (name, description, price, image).
         -  Implements sorting and pagination.
         -  Default placeholder for missing images.
         -  Fully responsive on desktop and mobile.
      
      *User Story 2: Authentication & Wishlist: Users can log in to save products, manage their shopping cart, and wishlist. 
         - Django Allauth for user authentication.
         - Add/remove items from cart and wishlist.
         - Cart and wishlist persists across sessions.
         - "Add to wishlist" button, to save favourite products. 

      *User Story 3: Product Detail and Search: View detailed product pages and search using filters. 
         - Product page includes full description, season, flavor tones, and images.
         - "Add to cart" and "add to wishlist" buttons.
         - Search and filter by keyword, price, category and size.

      *User Story 4: Advanced shopping cart:Enhances the shopping cart with discounts, delivery fees and wishlist integration. 
         - Users can update item quantities.
         - Apply coupon codes for discount.
         - Dinamic delivery fee calculation.
         - Move items from wishlist to cart. 

      *User Story 5: Featured products & UX Improvements: Enhances UX/UI with best sellers, contact info and better navigation. 
         - Feature products and best-seller badges.
         - Footer with contact information.
         - Improved product category filtering.
         - Admin panel display key product details.
         - Optimized UI for mobile and desktop. 

      *User Story 6: Checkout and Payment Integration: Implements a seamless checkout process with Stripe payments. 
         - Checkout page displays cart summary and shipping form.
         - Delivery fees apply dynamically.
         - Secure Stripe payment integration.
         - Order confirmation page and email notifications.  
         

**13. Resources for Project Development**

   * Useful links: 
   - navbar: https://getbootstrap.com/docs/4.0/components/navbar/

   - Bootstrap 4 Card container: https://bbbootstrap.com/snippets/card-container-48980697

   - bootstrap pagination: https://getbootstrap.com/docs/4.0/components/pagination/

   - color palette generator http://colormind.io/image/

   - footer bootstrap snippet https://mdbootstrap.com/snippets/standard/mdbootstrap/2885115

   * Documentation for settings: 
   - https://docs.djangoproject.com/en/5.1/topics/settings/
   - https://docs.djangoproject.com/en/5.1/topics/http/sessions/#settings
   - https://docs.djangoproject.com/en/5.1/ref/settings/#std:setting-MESSAGE_TAGS
   - https://docs.djangoproject.com/en/5.1/ref/settings/

   * Documentation for Stripe and Decouple: 
   - https://docs.stripe.com/js/payment_intents/confirm_konbini_payment
   - https://dashboard.stripe.com/test/dashboard
   - https://pypi.org/project/python-decouple/
         https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html
   - https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html

README:
Thank you to "mittnamnkenny" for creating an spectacular README file, which I have used as a path and template  to create my README. https://github.com/mittnamnkenny/galleriet.git


**14. Issues**
   14.1 Stripe Integration Fixes-Summary:
Implemented critical fixes to **Stripe integration** to ensure smooth payment processing and reliable webhook handling.  

   *Client Secret & Public Key Handling
      - Used `json_script` to safely pass `client_secret` and `stripe_public_key` to JavaScript, preventing encoding issues.  

   *Checkout Data Caching   
      - Implemented an AJAX request to **cache checkout data** before confirming payment, ensuring order details are available for Stripe webhooks.  
   
   *Improved Payment Submission Flow
      - Disabled the submit button while processing payments to **prevent duplicate submissions**.  
      - Restored the button if errors occurred to allow users to retry.  

   *Conditional Stripe Script Loading
      - Ensured Stripe JS only loads on the checkout page, preventing `clientSecret` and `stripePublicKey` errors elsewhere.  

   *Webhook Testing & Validation
      - Used **Stripe CLI** (`stripe listen --forward-to localhost:8000/checkout/webhook/`) to validate webhook events.  
      - Successfully triggered `payment_intent.succeeded` to verify order processing.  

   *Final Outcome:
      - Orders are **properly linked** to checkout data and webhook responses.  
      - Payments are **validated & confirmed** before redirecting users.  
      - Stripe webhooks **reliably process** order completions.  

   *Stripe payments are now fully functional. Because of my deadline I used AI to help me out fixing this issue. Javascript code was pasted to avoid more critical issues. 

---------------------
Back to Top