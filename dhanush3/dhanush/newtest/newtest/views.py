from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User
from newtest.forms import LoginForm
from django.contrib import messages



def signin(request):
    form=LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')  # Success message
                return render(request, 'home.html')  # Redirect to home page after successful login
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'index.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})


def signup(request):
    form=LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        uname=request.POST.get("username")
        passw=request.POST.get("password")
        email=request.POST.get("email")
        confirm=request.POST.get('confirm-password')
       
        if(confirm==passw):
            form=LoginForm()
            new=User.objects.create_user(uname,email,passw)
            new.save()
            print("appended to data base")
        else:
            error_message = 'confirm password does not match the password entered '
            return render(request, 'sign.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'signup.html', {'form':form})




def submit(request):
    return render(request,'signin.html')

def submit1(request):
    return render(request,'index.html')


def cal(request):
    return render (request,'calculator.html')


def graph(request):
    return render (request,'graph.html')

def research(request):
    return render (request,'research.html')


def feedback(request):

    if request.method=='POST':
         fname=request.POST['fname']
         fsubject=request.POST['fsubject']
         fphone=request.POST['fphone']
         fquery=request.POST['fquery']
         feed=User.objects.create_user(fname,fsubject,fquery)
         feed.save()
         print("the data has been returned to DB ")

    return render (request,'feedback.html')

def research(request):
    

    if request.method=='POST':
         rname=request.POST['fname']
         rsubject=request.POST['fsubject']
         rphone=request.POST['fphone']
         rdesc=request.POST['fquery']
         find=User.objects.create_user(rname,rsubject,rdesc)
         find.save()

         print("the data has been returned to DB ")

    return render (request,'research.html')


