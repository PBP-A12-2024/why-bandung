from django import forms
from django.contrib.auth.models import User
from dashboard.models import JournalEntry
from dashboard_admin.models import ProductEntry, TokoEntry

class journalEntryForm(forms.ModelForm):
    store = forms.ModelChoiceField(
        queryset=TokoEntry.objects.all(),  
        widget=forms.Select(attrs={
            'class': 'appearance-none rounded-md block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
        }),
        empty_label="Select a Store" 
    )

    class Meta:
        model = JournalEntry
        fields = ['title', 'store', 'description', 'ratings' ]

