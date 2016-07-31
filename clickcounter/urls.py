from django.conf.urls import url

from . import views


urlpatterns = [
    # URL to increment a counter
    url(r'^increment-counter/$', views.increment_counter,
        name='increment_counter'),
]
