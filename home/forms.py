from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'message': 'Message'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-4 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-300 ease-in-out shadow-sm hover:shadow-md',
                'placeholder': 'Your Name',
                'style': 'font-size: 16px; font-weight: 500;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-4 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-300 ease-in-out shadow-sm hover:shadow-md',
                'placeholder': 'Email Address',
                'style': 'font-size: 16px; font-weight: 500;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full p-4 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-300 ease-in-out shadow-sm hover:shadow-md',
                'rows': 5,
                'placeholder': 'Your Message',
                'style': 'font-size: 16px; font-weight: 500;'
            }),
        }
