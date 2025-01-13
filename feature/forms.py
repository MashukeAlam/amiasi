from django import forms
from .models import Feature

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['feature_name', 'link', 'reward']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding classes directly to form fields
        self.fields['feature_name'].widget.attrs.update({'class': 'block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'})
        self.fields['link'].widget.attrs.update({'class': 'block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'})
        self.fields['reward'].widget.attrs.update({'class': 'block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'})
