from django import forms

from .models import MarketingPreference

class MarketingPreferenceForm(forms.ModelForm):
    subscribed=forms.BooleanField(label='Recieve Marketing Email ? ',required=False)



    class Meta:
        model = MarketingPreference
        fields=[
            'subscribed',

        ]