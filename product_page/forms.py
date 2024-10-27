from django import forms
from dashboard.models import JournalEntry

class ReviewForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['ratings', 'description']

