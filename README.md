# django-click-counter
App to track the number of clicks on an item (Example: A like button on a blog).
## Installation
```
pip install git+https://github.com/bpsagar/django-click-counter.git
```

## Quickstart
Add blog to INSTALLED_APPS in settings.py of your project
```
INSTALLED_APPS = [
    ...
    'clickcounter',
]
```
Add blog urls to urlpatterns in urls.py of your project
```
urlpatterns = [
    ...
    url(r'^clickcounter/', include('clickcounter.urls', namespace='clickcounter')),
]
