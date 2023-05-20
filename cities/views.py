from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import City,Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User


from .forms import Commentform



def index(request):
    print('Entramos al index')
    cities = City.objects.all()

    return render(request, 'cities.html', {'cities':cities})

def get_city(request, id):
    city = City.objects.get(id=id)
    comments = Comment.objects.filter(city=id)
    comments_form = Commentform()
    return render (request, 'city.html', {
        'city':city, 
        'form':comments_form, 
        'comments': comments
        })



def create_new_comment(request, id):

    if request.method == 'POST':
        form = Commentform(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user=request.user
            new_comment.city= City.objects.get(id=id)
            new_comment.save()

        return redirect('city', id=id)
    else:
        return redirect('city', id=id)
        

def loggin(request):
    print('Entro en loggin')
    if request.method == 'GET':
        return render(request, 'registration/login.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print('Valor de user:', user)
        if user is None:
            return render(request,'registration/login.html',{
                'form':AuthenticationForm,
                'error':'Username or password is incorrect'
            })
        else:
            login(request,user)
            return redirect('index')
        

def loggout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'GET':
        return render(request,'registration/register.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.create_user(username=request.POST['username'],
                                               password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('index')
            except:
                return render(request,'registration/register.html',{
                    'form':UserCreationForm,
                    'error':'Username already exists'
                })
