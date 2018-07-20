from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
# Create your views here.
from application.models import User
import ipdb

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email', 'date_joined','password']      

def index(request):
    if request.method == 'POST':
        form=UserForm(request.POST) 
        if form.is_valid:
            form.save()
            return render(request,template_name='index1.html')
    else:
        form=UserForm()
    context={'form':form}
    return render(request,template_name='index.html',context=context)


class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=['email','password']

def custom(request):
    check = False
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():        
            data = form.cleaned_data
            em=data['email']
            pwd=data['password']
            query_set=(User.objects.filter(email=em)) & (User.objects.filter(password=pwd))
            if not query_set:
                check = True
            else:
                return render(request,template_name='index1.html')
    else:
        form=LoginForm()
    context={'form':form, 'check':check}
    return render(request,template_name='index.html',context=context) 