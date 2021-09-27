from django import forms
from django.contrib.auth .forms  import UserCreationForm,AuthenticationForm, UsernameField
from  django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import PasswordInput, Widget
from django.utils.translation import gettext, gettext_lazy as _
from.models import Post

class SignUpForm(UserCreationForm):
        password1=forms.CharField(label='Password', widget=PasswordInput(attrs={'class':'form-control'}))
        password2=forms.CharField(label='Confirm Password(again)',widget=PasswordInput(attrs={'class':'form-control'})) # hite name chaneg kel pass cha nav lebel gheun  widget gheun dot dto sathi passinput dila
        class Meta:
                model=User
                fields=['username', 'first_name', 'last_name', 'email']
                labels={'first_name':'Frist Name', 'last_name':'Last Name' ,'email':'Email'} # label gheun tya filedch name mdhe change kela
                widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                        'first_name':forms.TextInput(attrs={'class':'form-control'}),  
                        'last_name':forms.TextInput(attrs={'class':'form-control'}),  
                        'email':forms.EmailInput(attrs={'class':'form-control'}),     # bootstrap cha class lavnya satho widget cha use krun attrs cha usr krunb form control lavla
                
                }
class LoginForm(AuthenticationForm):
        username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
        password=forms.CharField(label=_("Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))


class PostForm(forms.ModelForm):
        class Meta:
            model=Post
            fields=['title','desc']
            labels={'title':'Title','desc':'Description'}
            widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                        'desc':forms.Textarea(attrs={'class':'form-control'}),
                }