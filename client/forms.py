from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'address': 'Address',
            'email': 'Email',
            'phone': 'Phone',
        }

    def __init__(self, *args, **kwargs):

        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['fullname'].widget.attrs.update({
            'id': 'fullname',
            'placeholder': 'Full Name',
        })

        self.fields['address'].widget.attrs.update({
            'id': 'address',
            'placeholder': 'Address',
        })

        self.fields['email'].widget.attrs.update({
            'id': 'email',
            'placeholder': 'Email',
        })

        self.fields['phone'].widget.attrs.update({
            'id': 'phone',
            'placeholder': 'Phone',
        })
