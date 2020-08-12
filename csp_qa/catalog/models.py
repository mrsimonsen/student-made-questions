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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique ID for this question')
    format = models.ForeignKey('Format', on_delete=models.SET_NULL,null=True)
    question = models.TextField()

    def __str__(self):
        return f'{id} - {format}:{question}'
