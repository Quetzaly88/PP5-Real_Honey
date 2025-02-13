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