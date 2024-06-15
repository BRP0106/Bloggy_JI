from django.contrib import messages
from django.shortcuts import render, HttpResponse
from .models import Contact
from Blog.models import Blog_Post
from Profile.models import Profile
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def Home(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = None
        MyPosts = Blog_Post.objects.all()  # fetch all data from the database
        return render(request, 'home/Home.html', {'MyPosts': MyPosts, 'profile': profile})
    else:
        MyPosts = Blog_Post.objects.all()  # fetch all data from the database
        return render(request, 'home/Home.html', {'MyPosts': MyPosts})


def About(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = None
        return render(request, 'home/About.html', {'profile': profile})
    else:
        return render(request, 'home/About.html')


def Contacts(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = None
        if request.method == 'POST':
            Name = request.POST['name']
            Email = request.POST['email']
            Phone = request.POST['phone']
            Issue = request.POST['issue']
            contact = Contact(name=Name, email=Email, phone=Phone, issue=Issue)
            contact.save()
            messages.success(request, 'Your Contact Has Been Submited Successfully.')
        return render(request, 'home/Contact.html', {'profile': profile})
    else:
        if request.method == 'POST':
            Name = request.POST['name']
            Email = request.POST['email']
            Phone = request.POST['phone']
            Issue = request.POST['issue']
            contact = Contact(Name=Name, Email=Email, Phone=Phone, Issue=Issue)
            contact.save()
            messages.success(request, 'Your Contact Has Been Submited Successfully.')
        return render(request, 'home/Contact.html')




