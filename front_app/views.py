import email
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from front_app.models import Catagory, Message, Product, Service, TeamMember, Testimonial
from .constants import about_info_body, about_information
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    team_member = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()
    product_list = Product.objects.all()

    index_data = {
        'about_body': about_info_body,
        'about_list_info' : about_information,
        'catagory_list' : catagories,
        'service_list' : service_list,
        'team_member' : team_member,
        'testimonials' : testimonials,
        'product_list' : product_list,
        'is_index': True,
    }
    return render(request,"front_app/index.html", context=index_data)

def product_detail(request, pk):
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    product_list = Product.objects.get(pk=pk)
    print(product_list)
    context_data = {
        'catagory_list': catagories,
        'service_list': service_list,
        'product_list': [product_list]
    }
    return render(request, "front_app/product-detail.html", context=context_data)

def catagory_detail(request, pk):
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    catagory = Catagory.objects.get(pk=pk)
    product_list = Product.objects.filter(catagory=catagory)
    print(product_list[0].productimage_set.all())
    context_data = {
        'catagory_list': catagories,
        'service_list': service_list,
        'product_list': product_list
    }
    return render(request, "front_app/product-detail.html", context=context_data)

def auth_page(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    service_list = Service.objects.all()
    return render(request,"front_app/auth.html",context={
        'service_list': service_list,
    })

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if first_name != None and last_name != None and email != None and password != None and confirm_password != None :
            if password == confirm_password:
                user = User.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    password = make_password(password)
                )
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect("index")

            else:
                service_list = Service.objects.all()
                return render(request,"front_app/auth.html",context={
                    'service_list': service_list,
                    'error_message' : 'The password not match.',
                    'register_data' : {
                        'first_name' : first_name,
                        'last_name' : last_name,
                        'email' : email,                        
                    },
                    'register_error' : True
                })
        else:
            service_list = Service.objects.all()
            
            return render(request,"front_app/auth.html",context={
                'service_list': service_list,
                'error_message' : 'All field are required.',
                'register_data' : {
                    'first_name' : first_name,
                    'last_name' : last_name,
                    'email' : email,                        
                },
                'register_error' : True
            })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            service_list = Service.objects.all()
            return render(request,"front_app/auth.html",context={
                'service_list': service_list,
                'error_message' : 'Wrong crediantial.',
                'login_data' : {
                    'email' : email
                    },
                'login_error' : True
            })
    return redirect('auth-page')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("index")
    return redirect('index')

def send_message(request):
    if not request.user.is_authenticated:
        return HttpResponse('You must be login.')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if name != None and subject != None and email != None and message != None :
            
            current_user = request.user
            
            user = User.objects.get(pk=current_user.id)
            Message.objects.create(
                sender =  user,
                email = email,
                subject = subject,
                body = message
            )
            messages.success(request, "Message send successful." )
            return HttpResponse('OK')
        else:
            messages.error(request, "All field are required." )
            return HttpResponse('All field are required.')
    return HttpResponse('Is not post request.')
    
def messages_page(request):    
    if not request.user.is_authenticated:
        return redirect('auth-page')
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    print(request.user.email)
    user = User.objects.get(email__exact=request.user.email)
    print(user)
    # catagory = Catagory.objects.get(pk=pk)
    # product_list = Product.objects.filter(catagory=catagory)
    messages_list = Message.objects.filter(sender=user)
    context_data = {
        'catagory_list': catagories,
        'service_list': service_list,
        'message_list' : messages_list
    }
    return render(request, "front_app/messages.html", context=context_data)

def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('auth-page')
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    user = User.objects.get(email__exact=request.user.email)

    context_data = {
        'catagory_list': catagories,
        'service_list': service_list,
        'user' : {
            'username' : user.username,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email' : user.email
        }
    }
    return render(request, 'front_app/profile.html', context_data)

def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('auth-page')
        
    if  request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        if username != None and lastname != None and email != None and firstname != None :
            current_user = request.user
            username_user = User.objects.filter(username=username)
            print(username_user)
            if len(username_user) > 0 and not current_user.username == username:
                messages.error(request, "Username not unique." )
                return redirect('profile-page')
            
            email_user = User.objects.filter(email=email)
            if len(email_user) > 0 and not current_user.email == email:
                messages.error(request, "Email not unique." )
                return redirect('profile-page')
            
            user = User.objects.get(pk=current_user.id)
            user.username = username
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()
            messages.success(request, "Profile update Succed." )
            return redirect('profile-page')
        else:
            messages.error(request, "All field are required." )
            return redirect('profile-page')
    return redirect('index')
    

    