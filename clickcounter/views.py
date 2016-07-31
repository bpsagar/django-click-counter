from .models import ClickCounter
from django.conf import settings
from django.db.models import F
from django.http import HttpResponse

import json

DEFAULT_COUNTER_SETTINGS = {
    'DEFAULT': {
        'MAX_CLICKS_PER_SESSION': 1
    }
}


CLICK_COUNTER_SETTINGS = getattr(
    settings, 'CLICK_COUNTER_SETTINGS', DEFAULT_COUNTER_SETTINGS)


def increment_counter(request):
    identifier = request.POST.get('identifier')
    if not identifier:
        return HttpResponse(json.dumps({'status': 'ERROR'}))
    type = request.POST.get('type', 'DEFAULT')
    counter, created = ClickCounter.objects.get_or_create(
        identifier=identifier, type=type)
    max_clicks = CLICK_COUNTER_SETTINGS.get(counter.type).get(
        'MAX_CLICKS_PER_SESSION')
    session_counter = request.session.get(counter.session_key(), 0)
    if session_counter < max_clicks:
        ClickCounter.objects.filter(identifier=identifier).update(
            counter=(F('counter')) + 1)
        counter = ClickCounter.objects.get(identifier=identifier)
        request.session[counter.session_key()] = counter.counter

    return HttpResponse(
        json.dumps({'status': 'OK', 'counter': counter.counter}),
        content_type="application/json")
