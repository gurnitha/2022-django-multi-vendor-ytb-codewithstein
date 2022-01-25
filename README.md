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