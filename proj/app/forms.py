from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from app.models import MyUser , MusicFile
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "password_mismatch"
            )
        


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget = forms.PasswordInput())



class MusicUploadForm(forms.ModelForm):
    emails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter protected user email addresses  separated by commas (,)'}),required=False)
    class Meta:
        model = MusicFile
        fields = ['title','singer','file','image','visibility']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter music title'}),
            'singer': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter singer name'}),
            'file': forms.FileInput(attrs={'class':'form-control', 'placeholder': 'upload mp3'}),
            'image': forms.FileInput(attrs={'class':'form-control', 'placeholder': 'upload song image'}),
            'visibility': forms.Select(attrs={'class':'form-control','type':'radio'}),
            'emails': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter protected user email addresses  separated by commas (,)'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        visibility = cleaned_data.get("visibility")
        emails = cleaned_data.get("emails")
        print(emails,'clean')
        if visibility == 'Public' or visibility == 'Private':
            print(visibility)
            if emails==None or len(emails)>0 :
                print('has email')
                raise ValidationError('select \"protect\" visibility to mention emails')
            
    def clean_emails(self):
        emails = self.cleaned_data.get("emails")
        print(emails,'clean field')
        print(len(emails),'length clean field')
        if emails =='':
            return emails
        if len(emails)!=0: 
            email_split = emails.split(',')
            emails_list = [email.strip() for email in email_split if email !='']
            for email in emails_list:
                try:
                    user_exist = MyUser.objects.get(email=email)
                except ObjectDoesNotExist:
                    raise ValidationError('mentioned email does not exists')
            return emails_list
        
    def clean_file(self):
        file = self.cleaned_data.get('file')
        file_str = str(file)
        if file_str.endswith('.mp3'):
            return file
        else:
            raise ValidationError('upload mp3 file')

       

