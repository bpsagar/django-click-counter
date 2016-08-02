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
```

## TemplateTags
Loading template tags: `{% load clickcounter_extras %}`

1. `indentifier_for_instance`: A template tag to get an identifier for an instance. It is generated using the model name, app label and model's primary key.
   ```
   {% identifier_for_instance instance=blog %}
   ```
2. `counter_for_identifier`: A template tag to get the counter value for an identifier.
   ```
   {% counter_for_identifier identifier='blog-0' %}
   ```
3. `counter_for_instance`: A template tag to get the counter value for an instance. This template tag makes use of the above tags to generate an identifier for the instance and then gets the counter for that identifier.
   ```
   {% counter_for_instance instance=blog %}
   ```
