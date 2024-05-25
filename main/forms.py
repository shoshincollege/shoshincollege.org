from django import forms

from main import models


class Subscription(forms.ModelForm):
    class Meta:
        model = models.Subscription
        fields = ["email"]
