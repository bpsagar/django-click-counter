from django import template
from django.apps import apps

register = template.Library()


@register.simple_tag
def identifier_for_instance(instance):
    '''A template tag to get an identifier for an instance'''
    return '%s-%s-%d' % (
        instance._meta.app_label, instance._meta.object_name, instance.pk)


@register.simple_tag
def counter_for_identifier(identifier):
    '''A template tag to get a counter for a identifier'''
    ClickCounter = apps.get_model('clickcounter', 'ClickCounter')
    counter = ClickCounter.objects.filter(identifier=identifier).first()
    if counter:
        return counter.counter
    return 0


@register.simple_tag
def counter_for_instance(instance):
    '''A template tag to get a counter for an instance'''
    identifier = identifier_for_instance(instance=instance)
    return counter_for_identifier(identifier=identifier)


@register.simple_tag(takes_context=True)
def session_counter_for_identifier(context, identifier):
    '''A template tag to get a counter from that session for an identifier'''
    ClickCounter = apps.get_model('clickcounter', 'ClickCounter')
    request = context['request']
    counter = ClickCounter.objects.filter(identifier=identifier).first()
    if counter:
        return request.session.get(counter.session_key(), 0)
    return 0


@register.simple_tag(takes_context=True)
def session_counter_for_instance(context, instance):
    '''A template tag to get a counter from that session for an instance'''
    identifier = identifier_for_instance(instance=instance)
    return session_counter_for_identifier(
        context=context, identifier=identifier)
