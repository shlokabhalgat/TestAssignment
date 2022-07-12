from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ThoughtPostModel


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ThoughtPostedByUser(forms.ModelForm):
    thought_post_text = forms.CharField(max_length=1000,
                                        widget=forms.TextInput(attrs={'placeholder': 'Example- Write your thought here'
                                            , 'style': 'border : none;', 'class': 'form-control'}))

    class Meta:
        model = ThoughtPostModel
        fields = ['thought_post_text']
