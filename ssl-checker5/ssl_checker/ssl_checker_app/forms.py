from django import forms 

class VideoSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
    clear_search = forms.BooleanField(initial=False, widget=forms.HiddenInput)