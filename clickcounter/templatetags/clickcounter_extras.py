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
    return ClickCounter.objects.get(identifier=identifier).counter


@register.simple_tag
def counter_for_instance(instance):
    '''A template tag to get a counter for an instance'''
    identifier = identifier_for_instance(instance=instance)
    return counter_for_identifier(identifier=identifier)
