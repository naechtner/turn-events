from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import date


class Tournament(models.Model):
  
    name = models.CharField(max_length=50, null=False)
    date = models.DateField(null=False, default=date.today)
    location = models.TextField(null=False)

    club = models.ForeignKey('Club', verbose_name=ugettext_lazy('Host'), null=True, blank=True)

    class Meta:
        db_table = 'gymnastics_tournaments'

    def __str__(self):
        return '{0}'.format(self.name)


class MyForm(forms.Form):
    date = forms.DateField(widget=AdminDateWidget)