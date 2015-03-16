from django import forms
from .models import Event,ExhibitorList

"""class abcForm(forms.Form):
    event_text = forms.CharField(label='event_text',max_length=200)
    pub_date = forms.DateTimeField()
   	event=forms.CharField(label='event',max_length=200)
   	company=forms.CharField(label='company',max_length=200)
    zip_code=forms.CharField(label='zip_code',max_length=200)
    city = forms.CharField(label='city',max_length=200)
    country =forms.CharField(label='country',max_length=200)
    booth_no=forms.CharField(label='booth_no',max_length=200)
    hall_no=forms.CharField(label='hall_no',max_length=200)"""

class abcForm(forms.ModelForm):
	#event_text = forms.CharField(label='event_text',max_length=200)
	#pub_date = forms.DateTimeField()
	class Meta:
		model=ExhibitorList
	"""
	event=forms.CharField(label='event',max_length=200)
	company=forms.CharField(label='company',max_length=200)
	zip_code=forms.CharField(label='zip_code',max_length=200)
	city = forms.CharField(label='city',max_length=200)
	country =forms.CharField(label='country',max_length=200)
	booth_no=forms.CharField(label='booth_no',max_length=200)
	hall_no=forms.CharField(label='hall_no',max_length=200)
	"""