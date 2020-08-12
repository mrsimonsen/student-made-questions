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


class TF(models.Model):
    '''a model representing a TF question'''
    c=(('T','True'),('F','False'))
    correct = models.CharField(
    max_length=1,
    choices=c,
    default='T',
    )

    def __str__(self):
        return self.correct

class SA(models.Model):
    '''a model representing a SA question'''
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.answer

class FB(models.Model):
    '''a model representing a FB question'''
    num = models.PositiveSmallIntegerField(
    default=1,
    verbose_name='Number of blanks',
    validators=[v_FB],
    )


class MC(models.Model):
    '''a model representing a MC question'''
    num = models.PositiveSmallIntegerField(
    default=4,
    verbose_name='Number of choices',
    validators=[v_MC],
    )

class MA(models.Model):
    '''a model representing a MC question'''
    num = models.PositiveSmallIntegerField(
    default=4,
    verbose_name='Number of choices',
    validators=[v_MA],
    )

class Question(models.Model):
    '''a unique question'''
    FORMATS = (
    ('FB','Fill in the Blank'),
    ('MA', 'Multiple Answer'),
    ('MC', 'Multiple Choice'),
    ('SA', 'Short Answer'),
    ('TF', 'True/False')
    )
    format = models.CharField(max_length=2, default='MC', choices=FORMATS, help_text='question format')
    question = models.TextField()

    '''if format not in ("TF","SA"): #no numbers for TF or SA
        d=0
        v_n=''
        v=[]
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
        validators=v,
        )'''

    def __str__(self):
        return f'{id} - {format}:{question}'
