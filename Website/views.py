from django.shortcuts import render

# Create your views here.
from django.urls import include
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        msg_name = request.POST['name']
        msg_email = request.POST['email']
        msg_phone = request.POST['phone']
        msg_message = request.POST['message']

        #send an email
        send_mail('Message from : ' + msg_name, #subject
                  msg_message, #message
                  msg_email, #From
                    ['harishdeore10@gmail.com'], #To
                 )


        return render(request, 'contact.html', {'name' : msg_name})
    else:
        return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def rooms(request):
    return render(request, 'rooms.html')

def booknow(request):
    return render(request, 'booknow.html')