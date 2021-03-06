# 2022-django-multi-vendor-ytb-codewithstein
This is my exercise based on the tutorials by Code With Stein Channel on Youtube https://www.youtube.com/watch?v=FN3EfKC2i6M&amp;list=PLpyspNLjzwBkeyP_4_bZBdtRjZQreDR_H&amp;index=2

Github repository: https://github.com/gurnitha/2022-django-multi-vendor-ytb-codewithstein


#### 1. Create django project and apps

        E:.
        ├───apps
        │   ├───core
        │   │   ├───migrations
        │   │   │   └───__pycache__
        │   │   └───__pycache__
        │   ├───product
        │   │   ├───migrations
        │   │   │   └───__pycache__
        │   │   └───__pycache__
        │   └───vendor
        │       ├───migrations
        │       │   └───__pycache__
        │       └───__pycache__
        └───config
            └───__pycache__

        modified:   README.md


#### 2. Create static pages: frontpage and contact in core app

        modified:   README.md
        new file:   apps/core/templates/core/base.html
        new file:   apps/core/templates/core/contact.html
        new file:   apps/core/templates/core/frontpage.html
        new file:   apps/core/urls.py
        modified:   apps/core/views.py
        modified:   config/urls.py


#### 3. Create static pages: product, category and search in product app

        modified:   README.md
        modified:   apps/core/templates/core/base.html
        modified:   apps/core/templates/core/frontpage.html
        new file:   apps/product/templates/product/category.html
        new file:   apps/product/templates/product/product.html
        new file:   apps/product/templates/product/search.html
        new file:   apps/product/urls.py
        modified:   apps/product/views.py
        modified:   config/urls.py


#### 4. Create static pages: add_product, become_vendor, login, vendor_admin pages

        modified:   apps/core/templates/core/base.html
        new file:   apps/vendor/templates/vendor/add_product.html
        new file:   apps/vendor/templates/vendor/become_vendor.html
        new file:   apps/vendor/templates/vendor/login.html
        new file:   apps/vendor/templates/vendor/vendor_admin.html
        new file:   apps/vendor/urls.py
        modified:   apps/vendor/views.py
        modified:   config/urls.py


#### 5. Add and load static and media files

        modified:   README.md
        modified:   apps/product/templates/product/product.html
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   static/css/main.css
        new file:   static/img/img-large.jpeg
        new file:   static/img/img.jpeg
        new file:   static/js/main.js


### 6. VENDORS
--------------

#### 6.1 Create Vendor model, create and apply migration

        STEPS:

        1. Create model
        2. Create migration
        3. Apply migration
        4. Register model to admin

        modified:   README.md
        modified:   apps/vendor/admin.py
        new file:   apps/vendor/migrations/0001_initial.py
        modified:   apps/vendor/models.py


#### 6.2 Add logic to become_vendor method and  Use UserCreationForm to create a new user

        STEPS:

        1. In vendor/views.py:
           - import UserCreationForm
           - import redirect
        2. In vendor/views.py (become_vendor)
           - load UserCreationForm
           - add logic to create a user
        3. Load the form to become_vendor page
        4. Test it out :)

        modified:   README.md
        modified:   apps/vendor/templates/vendor/become_vendor.html
        modified:   apps/vendor/views.py


#### 6.3 Showing the authenticated user with restriction

        STEPS:

        1. Import login_required
        2. Create instance of the user (vendor)
        3. Use is_authenticated method to show link
           to authenticated user
        4. Test it out :)

        modified:   README.md
        modified:   apps/core/templates/core/base.html
        modified:   apps/vendor/templates/vendor/vendor_admin.html
        modified:   apps/vendor/views.py


#### 6.4 Logout user

        STEPS:

        1. In vendor/urls.py: Import auth_views
        2. Use it to create path to logout
        3. Add link to vendor_admin to logout
        4. Test it out :)

        NOTE: After logging out, it return to admin panel page

        modified:   README.md
        modified:   apps/vendor/templates/vendor/vendor_admin.html
        modified:   apps/vendor/urls.py  


#### 6.5 Darurat (It does not work. Has to back to 6.4)

        modified:   apps/vendor/templates/vendor/login.html
        modified:   apps/vendor/urls.py
        modified:   apps/vendor/views.py
        modified:   config/settings.py


#### 6.6 Making vendor to login and logout using django.contrib.auth

        modified:   README.md
        modified:   apps/vendor/templates/vendor/become_vendor.html
        modified:   apps/vendor/urls.py
        modified:   apps/vendor/views.py
        modified:   config/settings.py


### 7. PRODUCT
--------------


#### 7.1 Create Category and Product models

        modified:   README.md
        modified:   apps/product/admin.py
        new file:   apps/product/migrations/0001_initial.py
        modified:   apps/product/models.py


#### 7.2 Show list of products in admin area

        modified:   README.md
        modified:   apps/vendor/templates/vendor/vendor_admin.html
        modified:   apps/vendor/views.py


#### 7.3 Make it possible for vendors to add products

        modified:   README.md
        new file:   apps/vendor/forms.py
        modified:   apps/vendor/templates/vendor/add_product.html
        modified:   apps/vendor/views.py
        new file:   media/uploads/img-large.jpeg
        new file:   media/uploads/img-large_uQsXPIi.jpeg


#### 7.4 Show newest product on the frontpage

        modified:   README.md
        modified:   apps/core/templates/core/frontpage.html
        modified:   apps/core/views.py
        new file:   media/uploads/uploads/img-large_uQsXPIi.jpeg
        modified:   static/css/main.css


#### 7.5 (Darurat, doest now work) Show detail view of a product

        NOTE: It shows error, I could not fix it

        NoReverseMatch at /
        Reverse for 'product' with arguments '('', '')' not found. 1 pattern(s) tried: ['(?P<category_slug>[-a-zA-Z0-9_]+)/(?P<product_slug>[-a-zA-Z0-9_]+)/$']
        
        modified:   README.md
        modified:   apps/core/templates/core/frontpage.html
        modified:   apps/product/templates/product/product.html
        modified:   apps/product/urls.py
        modified:   apps/product/views.py
