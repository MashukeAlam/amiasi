from django import forms
from .models import CreditRequest

class CreditRequestForm(forms.ModelForm):
    class Meta:
        model = CreditRequest
        fields = ['payment_method', 'transaction_number', 'phone_number', 'amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding classes directly to form fields
        self.fields['amount'].widget.attrs.update({'class': 'block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'})
        self.fields['payment_method'].widget.attrs.update({'class': 'block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'})
        self.fields['transaction_number'].widget.attrs.update({'class': 'block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'})
        self.fields['phone_number'].widget.attrs.update({'class': 'block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'})