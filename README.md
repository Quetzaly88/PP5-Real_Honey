# PP5-Real_Honey - Buy Local, Authentic Honey - Online

**1. Key Project Information**

Project Name: PP5_Real_Honey
      * Description
      Real Honey is a user-friendly and scalable online marketplace that connects local beekeepers with customers, allowing them to purchase honey and honey products from the online store. 

      * Key Goal
      To provide a seamless and enjoyable shopping experience while supporting local beekeepers.

      * Target Audience
      - Nature and health-conscious individuals that love honey. 
      - Online shoppers seeking convenience
      - Supporters of local beekeepers

      * Live Project:
      URL: https://pp5-real-honey-60f1f8b03b81.herokuapp.com/

      * Dummy Card for Testing: 
      - Card Number:  4242 4242 4242 4242
      - Expiry: 01/34
      - CVC: 123
      - ZIP: 12345

      * Test payments using Stripe test cards.
      - Card number 4242 4242 4242 4242 (successful)
      - Card number 4000 0000 0000 0002 (failed)
      - Card number 4000 0025 0000 3155 (3D Secure)

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
         ----------
         - Database Schema
         ----------

   *3.4 Wireframes*
         [link or imgs]
         ------------

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
         * Performed bu using print(), console.log() and manual testing. 
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
            * Why Use Python-Decouple? 
               - Keeps secret keys secure by storing them in .env (added to .gitignore)
               - Improves maintainability by separating configuration from the codebase.
               - Prevents security risks by avoiding storing secrets in vesion control. 
            * Installation of python-decouple:
               The python-decouple helps manage environment variables securely by loading them from a .env file instead of hardcoding sensitive information in settings.py.
            * How I used python decouple? 
               1. Install: pip install python-decouple
               2. Create a .env file in project root and add it to .gitignore
               3. Add secret keys to .env: 
               SECRET_KEY='your-django-secret-key'
               STRIPE_PUBLIC_KEY='your-public-key-here'
               STRIPE_SECRET_KEY='your-secret-key-here'
               STRIPE_WEBHOOK_SECRET='your-webhook-secret-here' # if needed
               DEBUG=True  # Change to False in production
            *Load the secrets in settings.py:
               import os
               from decouple import config  # Import python-decouple
               SECRET_KEY = config("SECRET_KEY")  # Securely fetch secret key
               STRIPE_PUBLIC_KEY = config("STRIPE_PUBLIC_KEY")
               STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
               STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET") # if needed
               DEBUG = config("DEBUG", default=False, cast=bool). **(Toggle debug will be changed in .env)
            
      [Stripe Payment Integration:]
         Overview:
            * Stripe payment processing in the project. Stripe is used to securely handle online payments for customer orders. 
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

**9. Handling product images and information**
   To ensure product information and images persists across deployments, fixtures were used. However, some product data was missing after loading the fixtures, so an automated script was created to fix missing descriptions. 
 
      1. Create a fixture file (Backup of all product data)
         - products/fixtures/ all_products_backup.json
      2. Load fixtures into the Database
         - python manage.py loaddata fixtures/products.json
      3. Dump Existing Data into a Fixture to export current data as a fixture
         - python manage.py dumpdata app_name.ModelName --indent 2 > fixtures/products.json

   
   * Fixing Missing Product Information in Fixtures, to ensure all products have a short description, an automation script was created:
      1. Create and store the script
         - Create a new Python script named update_fixtures.py in the root directory of the project (same level as manage.py).
         - The script reads products/fixtures/all_products_backup.json, updates missing descriptions, and saves a new fixture file. (code copied from chat.gpt)
      2. Run the Script to Update Missing Descriptions
         - python update_fixtures.py
         This generated an updated fixture file:
            - all_products_backup_updated.json
      3. Load the Updated Fixture into the Database
         - python manage.py loaddata products/fixtures/all_products_backup_updated.json
      4. Verify Data in Django Admin and Product Listings
         - Check if descriptions are correct and ensure proper display
      5. Replace the old Fixture with hte updated one
         - mv products/fixtures/all_products_backup_updated.json products/fixtures/all_products_backup.json
            * Each time you update products through Django Admin, remember to export new data:
               - python manage.py dumpdata products.Product products.ProductSize --indent 2 > products/fixtures/all_products_backup.json.
               This ensures your fixture always contains the latest product details
            * Test the Fixture by Reloading It. To make sure everything is working, reload the fixture and verify data:
               - python manage.py loaddata products/fixtures/all_products_backup.json

   This method ensures all product descriptions are always complete while keeping the fixture-based data management consistent across deployments. 

**10. Additional Resources**
   *Useful links for Django, Bootstrap and Stripe documentation 



**11. Future Implementations**
   This project implements key e-commerce functionalities, focusing on product browsing, user authentication, shopping cart management, wishlist features, cheeckout..............

**12. User Stories:**

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
Implemented critical fixes to "Stripe integration" to ensure smooth payment processing and reliable webhook handling.  

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

   *We resolved a critical Stripe card element mounting issue that prevented payments from processing. Additional checks ensure the card element remains in the DOM before confirming payments. We also fixed a KeyError: 'county', ensuring all order fields are handled properly

   *Final Outcome:
      - Orders are **properly linked** to checkout data and webhook responses.  
      - Payments are **validated & confirmed** before redirecting users.  
      - Stripe webhooks **reliably process** order completions.  

   *Stripe payments are now fully functional. Because of my deadline I used AI to help me out fixing this issue. Javascript code was pasted to avoid more critical issues. 

14.2 CLOUDINARY SETUP
* Create a claudinary account and set up a confirmation code to be able to see the api secret key.
* CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@dapm2mnex

   Media Files Storage – Cloudinary
   Originally, the project was planned to use AWS S3 for media storage.
   However, after reviewing the project requirements and the importance of rapid deployment, Cloudinary was chosen for the following reasons:

* Simpler and Faster Setup: Cloudinary integrates easily with Django using the django-cloudinary-storage package, requiring fewer configuration steps compared to AWS S3 (which needs IAM users, CORS setup, storage classes, etc.).

* Ideal for Portfolio Projects: Cloudinary offers a free plan that fits the needs of this e-commerce application without extra configuration for custom domains or regional buckets.

* Quick Deployment: Cloudinary allows rapid deployment of media files in production environments like Heroku, where file systems are ephemeral (i.e., lost after dyno restarts).

* Built-in Image Optimization: Cloudinary automatically optimizes images for faster loading times, improving UX and SEO without additional settings.

      How It Was Implemented:
      1. Installed the required packages:

         pip install django-cloudinary-storage cloudinary

      2. Media File Storage - Local Development vs. Cloudinary Production. 
         In order to handle media files correctly during development and production, the following smart configuration was implemented in settings.py:

         if 'DEVELOPMENT' in os.environ:
            DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
         else:
            CLOUDINARY_STORAGE = {
               'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
               'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
               'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
            }
            DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

      * ADD DEVELOPMENT=1 in the .env file TO BE ABLE TO SAVE UPLOADED IMAGES INTO THE LOCAL /MEDIA/ DIRECTORY. 

      
      3. Configured environment variables securely in Heroku Config Vars.

      4. Updated requirements.txt and deployed to Heroku.

   All product images and user-uploaded files are now safely stored and served via Cloudinary.
   This choice ensured a faster, simpler, and more reliable deployment for the project's timeline and technical requirements.

---------------------
Back to Top




edit products
http://127.0.0.1:8000/products/edit/1/

add products
http://127.0.0.1:8000/products/add/


**Heroku Deployment:**

   * 1. Prepare the Project for deployment 
   install heroku: brew tap heroku/brew && brew install heroku
   - heroku --version

      1.1 Install required Dependencies:

         * psycopg2-binary: Required for PostgreSQL database connection.
         * dj-database-url: Allows easy database configuration using a DATABASE_URL environment variable.
         * gunicorn: A production-ready web server for running Django applications on Heroku.

            After installation the 'pip freeze > requirements.txt' file was updated to include dependencies. 

      1.2 Configure Environment Variables:

         - Inside env.py (DO NOT commit this file to GitHub!):

            import os
            os.environ.setdefault('SECRET_KEY', 'your-secret-key-here')

         - In settings.py, we updated the SECRET_KEY to use the environment variable instead of hardcoding it:

            import os
            SECRET_KEY = os.environ.get('SECRET_KEY')

      1.3 Set up the database (PostgreSQL):

         _ Since SQLite is not suitable for production, we migrated to PostgreSQL, a cloud-based relational database provided by Heroku.
            * Created a PostgreSQL database using Code Institute's PostgreSQL instance. 
            * Updated settings.py to support PostgreSQL:

                  import dj_database_url
                  if 'DATABASE_URL' in os.environ:
                     DATABASES = {
                        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
                     }
                  else: 
                     DATABASES = {
                        'default': {
                              'ENGINE': 'django.db.backends.sqlite3',
                              'NAME': BASE_DIR / 'db.sqlite3',
                        }
                     }
         * The DATABASE_URL was retrieved from Heroku Config Vars.

      1.4 Find 'import env' in settings and replace with: 
               if os.path.isfile("env.py"):
               import env
               from pathlib import Path


   * 2. Setting up Heroku:

         * Log in to heroku and create the app
         * Add in conf vars:
            - DISABLE_COLLECTSTATIC:  1
            - SECRET_KEY: Random secret key from  https://randomkeygen.com/
         * Create Procfile in root directory with this information: 
            - web: gunicorn real_honey.wsgi:application
         * Create runtime.txt with this info:
            - Python 3.12
         * In settings.py, add the URL for your app to the ALLOWED_HOSTS. Remove https:// from the start of the URL, and the trailing slash from the end of the URL:
            - 'pp5-real-honey-60f1f8b03b81.herokuapp.com'
         * In .env Debug Mode (True for development, False for production)
         DEBUG=False. Before Deployment. 

   * 3. Deploy in Heroku

Issues: 

   -  Heroku deployment failed due to missing dependencies and  a configuration error in settings.py.
      * Missing python-decouple: This was installed
         pip install python-decouple
         pip freeze > requirements.txt

   - Heroku rejects deployment because of an invalid Python version format in runtime.txt. Additionally, Heroku now prefers .       python-version instead of runtime.txt.
      * Ensured Django 3.12 exixts in runtime.txt
      * Deleted runtime.txt
      * Instead Heroku asks to create 'echo "3.12" > .python-version' in root directory. After this change the Deployment was sucessful!

      https://devcenter.heroku.com/articles/python-support

Creating an AWS Amazon Web Services s3 Account:
This is a cloud-based storage servive that gives us a small piece of Amazon's infrastructure to be able to save our files. 
- Navigate to aws.amazon.com
- Open an account and continue all the verifications.
- Create New Bucket called "real-honey".
      To create the new bucket:
      1. Enter a bucket name
      2. Select ‘ACLs enabled’
      3. Select ‘Bucket owner preferred’
      4. Deselect ‘Block all public access’
      5. Check the box to acknowledge the risk of public access
      6. Leave the other options unchanged and click ‘create bucket’
- Enable static website hosting:
      When the bucket is created, click on the bucket name to view the bucket details. Go to Static website hosting and click Edit.
            1. Click ‘Enable’
         2. Enter ‘index.html’ (without quotes) into the Index document input
         3. Enter ‘error.html’ (without quotes) into the Error document input
         4. Click ‘Save changes
- Go to Permissions and find 'Cross-origin resource sharing (CORS)': 

         [
         {
         "AllowedHeaders": ["Authorization"],
         "AllowedMethods": ["GET"],
         "AllowedOrigins": ["*"],
         "ExposeHeaders": []
         }
         ]
- Save Changes

* In permissions find 'Bucket policy' and edit/ policy generator.
      1. For the policy type you can select ‘S3 Bucket Policy’
      2. For the principal you can enter “*” without quotes
      3. For the Action select ‘GetObject’ from the dropdown
      - Then go back to the bucket policy editor in the other tab and click this button to copy the ARN:
      Then go back to the Policy Generator in the other tab
      1. Paste the ARN into the ARN input
      2. Click ‘Add Statement
      3. Scroll down and click ‘Generate Policy’
      4. Copy all of the text in the popup:
      5. Go back to the policy editor in the other tab and paste in the policy code.
      6. Edit the ‘Resource’ value by adding /* to the end, to allow access to all objects within the bucket.
      {
  "Id": "Policy1742108698616",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1742108686683",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::real-honey*/",
      "Principal": "*"
    }
  ]
}

In permissions, Edit 'Access control list (ACL)': 
      1. Click ‘List’ in the Everyone (public access)
      2. Click the checkbox to indicate that you understand the effects of the changes
      3. Click ‘Save changes’


Step 1 - Create a user group
1. Search for ‘iam’ in the search bar at the top
2. Click on ‘IAM’
Click ‘User Groups’ on the left:
Click ‘Create Group’:
Enter a group name: (here I’ve used ‘manage-test-bucket’ as the name of the bucket is
‘test-bucket’)
Scroll down to the bottom and click ‘Create user group’:
Step 2 - Create a Policy
Click ‘Policies’ in the menu to the left:
Click ‘Create Policy’:
1. Click the ‘JSON’ tab
2. Click the ‘Actions’ dropdown
3. Click ‘Import policy’
1. Search for ‘s3’
2. Select ‘AmazonS3FullAccess’
3. Click ‘Import Policy’
1. Search for ‘s3’ at the top
2. Right click ‘S3’
3. Click ‘Open in a new tab’
Unset
In the new tab:
1. Select your bucket
2. Click ‘Copy ARN’
Go back to the previous tab and add your ARN in quotes to the ‘Resource’ list twice, for the
second one add /* after the ARN.

            {
            "Version": "2012-10-17",
            "Statement": [
            {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
            "s3:*"
            ],
            "Resource": [
            "MY ARN",
            "MY ARN/*"
            ]
            }
            ]
            }
Scroll to the bottom and click ‘Next’:
Enter a policy name and description:
Scroll down and click ‘Create policy’:
You’ll see a success message:
Step 3 - Attach the policy to the group
Click ‘User groups’ in the menu to the left:
Click your group:
1. Click the ‘Permissions’ tab
2. Click the ‘Add permissions’ dropdown
3. Click ‘Attach policies’
1. Search for your policy (you can search for the policy name or description that you
entered previously)
2. Select the checkbox beside your policy
3. Click ‘Attach policies’
Step 4 - Create a User
1. Click ‘Users’ in the menu to the left
2. Click ‘Create user’
1. Enter a user name
2. Click ‘Next’
1. Select the group you created previously
2. Click ‘Next’
Scroll down and click ‘Create user’:
Step 5 - Create an Access Key
Click on your new user:
Click ‘Security credentials’:
Scroll down to the ‘Access keys’ section and click ‘Create access key’:
1. Select ‘Application running outside AWS’
2. Click ‘Next’
Click ‘Create access key’:
1. Scroll down and click ‘Download .csv file’
2. Click ‘Done’
Open the .csv file in any text editor (such as Notepad on Windows, TextEdit on Mac). It will look
like this:
Note that the values are separated by a comma, a common mistake is to see the forward slash
as separating the values, but it’s actually part of the last value:
Use the values as your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY heroku
config vars:

# Now that we've created an s3 bucket and the appropriate user's groups and security policies for it, we connected django to it.
- install two new packages.
      * pip3 install boto3
      * pip3 install django-storages
      * pip3 freeze > requirements.txt

Deployment & Webhooks Setup:

1. AWS S3 Setup
- Configured AWS S3 for static and media files.
- Updated settings.py to use AWS S3 
- Uploaded media files to the S3 media folder with public read access.

2. Stripe Webhooks Setup
- Create a webhook in Stripe Dashboard > Developers > Webhooks
- Set endpoint "https://your-heroku-app.herokuapp.com/checkout/wh/"
- Enabled all events and copied the Signing Secret.
- Added STRIPE_WH_SECRET to Heroku Config Vars.
- Updated settings.py to include the webhook secret. 

3. Testing Stripe Webhooks
- Installed Stripe CLI / stripe log-in.
- Foward events "stripe listen --forward-to your-heroku-app.herokuapp.com/checkout/wh/"
- Trigger test events:
   stripe trigger payment_intent.succeeded
   stripe trigger payment_intent.payment_failed
- Verified logs: heroku logs --tail


Email Configuration and Testing
- Configure Gmail for e-commerce emails.
   1. Open "see all settings" in own gmail accoun.
   2. Find accounts and import/other google account settings
   3. In security create 2-step verification.
   4. Search "app passwords"
   5. Create app "real-honey-app" and save the 16 digit password. 
   6. In Heroku save in config Vars:
      - EMAIL_HOST_USER---'my-app-email@gmail.com'
      - EMAIL_HOST_PASSWORD---16 digit password without spaces
      - DEFAULT_FROM_EMAIL---'my-app-email@gmail.com'

   7. Add the necessary functionality in settings.py:
   
         # Email Configuration
      if 'DEVELOPMENT' in os.environ:
         EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
         DEFAULT_FROM_EMAIL = 'realhoney@example.com'
      else:
         EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
         EMAIL_USE_TLS = True
         EMAIL_PORT = 587
         EMAIL_HOST = 'smtp.gmail.com'
         EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
         EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
         DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)

   8. Commit changes and restart heroku dynos 
      - heroku ps:restart
      - heroku run python manage.py shell

   9. Run the Django shell on Heroku and send a test email:
      -  from django.core.mail import send_mail

      -  send_mail(
            'Test Email from Real Honey',
            'This is a test email to confirm SMTP settings work correctly.',
            'my-app-email@gmail.com',
            ['recipient-email@example.com'],
            fail_silently=False,
         )
   10. If the function returns 1, the email was sent successfully.




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



from PP4:
Python Code Validation To ensure code quality and PEP8 compliance, I used:

- **[Flake8](https://flake8.pycqa.org/)** to identify issues such as unused imports, indentation problems, trailing spaces, etc.
   Command in terminal: pip install flake8
   Command to run flake: flake8 .

- A '.flake8' config was used to exclude irrelevant files. A new file called '.flake8' was created in the project root.
   File: 

   [flake8]
   ignore = E501
   exclude =
         venv,
         migrations,
         __pycache__,
         static,
         manage.py,
         .vscode,
         settings.py
   max-complexity = 10

      * What this config does:
         - ignore = E501: skips the "line too long" error

         - exclude: skips folders and files you don’t want to check (like migrations, static, etc.)

         - max-complexity: optional — sets the allowed complexity of functions (you can remove this line if not needed)

   Again, run command: flake8 .

- **[Autopep8](https://pypi.org/project/autopep8/)** was used to automatically fix basic errors: 
Command in terminal: pip install autopep8
Command in terminal: autopep8 . --in-place --recursive
command in terminal to keep checking the errors: flake8 .


from PP4, static files not showing in deployed app
Static files (CSS, JavaScript, images): Static files were configured work in both development and production using WhiteNoise and Django's static settings:

   STATIC_URL = '/static/'
   STATICFILES_DIRS = [BASE_DIR / 'static']
   STATIC_ROOT = BASE_DIR / 'staticfiles'
Command to collect static files:

% python manage.py collectstatic 
This collects all static assets into the /staticfiles/ directory, which is served by Heroku in production.

DISABLE_COLLECTSTATIC = 1 is removed from config vars in Heroku. This variable skips static file collection, which breaks CSS, images and JavaScript in production.

Middleware configuration (in settings.py):

MIDDLEWARE = [ 'django.middleware.security.SecurityMiddleware', 'whitenoise.middleware.WhiteNoiseMiddleware', ...]

Heroku Setup & Commands

To prepare and deploy your app on Heroku:

% heroku run --app pp5-real-honey "python manage.py collectstatic --noinput"

Explanation: - Heroku run: Executes a one-time command on the Heroku dyno (remote server).
