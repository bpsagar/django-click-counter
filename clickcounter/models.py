from django.db import models


class ClickCounter(models.Model):
    '''A model to track the number of clicks'''

    # A unique identifier of an element whose clicks are tracked
    identifier = models.CharField(max_length=200, unique=True)

    # Counter to track clicks
    counter = models.IntegerField(default=0)

    # Optional type attribute to have different settings for different types
    type = models.CharField(max_length=100, default='DEFAULT')

    # Counter created datetime
    created_on = models.DateTimeField(auto_now_add=True)

    # Counter updated datetime
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Click Counter"
        verbose_name_plural = "Click Counters"

    def __str__(self):
        return '%s - %d' % (self.identifier, self.counter)

    def session_key(self):
        '''A session key which stores the click counter of that session'''
        return 'click-counter-id-%s' % self.identifier
