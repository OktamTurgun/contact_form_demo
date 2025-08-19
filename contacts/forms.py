from django import forms
from .models import ContactMessage
class ContactMessageForm(forms.ModelForm):
  class Meta:
    model = ContactMessage
    fields = ["first_name", "last_name", "phone", "email", "message"]
    widgets = {
        "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ism"}),
        "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Familiya"}),
        "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+99890xxxxxxx"}),
        "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Example@example.com"}),
        "message": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Xabaringiz..."}),
    }
