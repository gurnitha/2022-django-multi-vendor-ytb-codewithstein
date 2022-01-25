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