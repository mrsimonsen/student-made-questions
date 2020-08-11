from django.db import models
from django.urls import reverse #Used to generate URLS by reversing the URL pattern
import uuid #required for primary keys?

#custom validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def v_MC(value):
    if 5 < value or value < 3:
        raise ValidationError(
        _(f'Must have 3 to 5 choices'),
        )
def v_FB(value):
    if value <= 0:
        raise ValidationError(
        _(f'Must have at least 1 blank')
        )
def v_MA(value):
    if value < 3:
        raise VaildationError(
        _(f'Must have a least 3 choices')
        )

class Format(models.Model):
    '''question format type'''
    FORMATS = (
    ('FB', 'Fill in the Blank'),
    ('MA', 'Multiple Answer'),
    ('MC','Multiple Choice'),
    ('SA', 'Short Answer'),
    ('TF','True/False'),
    )

    format = models.charField(
    max_length=2,
    choices=FORMATS,
    default='MC',
    help_text='question format')

    if format not in ("TF","SA"): #no numbers for TF or SA
        if format == "MC":
            d=4
            v_n="Number of choices"
            v=[v_MC]
        elif format == "FB":
            d=1
            v_n="Number of blanks"
            v=[v_FB]
        elif format == 'MA':
            d=3,
            v_n="Number of choices"
            v=[v_MA]
        num_responses = models.PositiveSmallIntegerField(
        default=d,
        verbose_name=v_n,
        validators=v
        )


    def __str__(self):
        return self.format

class Question(models.Model):
    '''a model representing a question'''
    question = models.TextField()

    format = models.ForeignKey('Format')
