from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages  # For Message
from django.contrib.auth.models import User, Permission  # For Create The USer
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from Blog.models import Blog_Post, Upload_Video, Upload_Image, Blog_Comment, Video_Comment, Image_Comment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


# from .models import user


# Create your views here.

def LoginForm(request):
    return render(request, 'user/Login.html')


def Login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['password']
        u = authenticate(request, username=uname, password=passw)
        if u is not None:
            login(request, u)
            messages.success(request, "Successfully Logged In ")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again ")
            return redirect('LoginForm')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')


@login_required
def Profiles(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        profile = None
    posts = Blog_Post.objects.filter(user=request.user)
    b_comments = Blog_Comment.objects.filter(post__in=posts)
    video = Upload_Video.objects.filter(user=request.user)
    v_comments = Video_Comment.objects.filter(post__in=video)
    image = Upload_Image.objects.filter(user=request.user)
    i_comments = Image_Comment.objects.filter(post__in=image)

    return render(request, 'user/Profile.html',
                  {'profile': profile, 'posts': posts, 'video': video, 'image': image, 'b_comments': b_comments,
                   'v_comments': v_comments, 'i_comments': i_comments})


def RegistrationForm(request):
    return render(request, 'user/Registration.html')


def Registrations(request):
    if request.method == 'POST':
        Username = request.POST['username']
        First_Name = request.POST['FName']
        Last_Name = request.POST['LName']
        Photo = request.FILES['photo']
        Email = request.POST['email']
        Bio = request.POST['bio']
        Pass = request.POST['pass']
        CPass = request.POST['cpass']

        if len(Pass) != 8:
            messages.warning(request, "Password must be 8 character ")
            return redirect('RegistrationForm')
        if not Pass.isalnum():
            messages.warning(request, "Password must be alphanumeric")
            return redirect('RegistrationForm')
        if Pass != CPass:
            messages.warning(request, "Both Passwords are not same")
            return redirect('RegistrationForm')
        if User.objects.filter(username=Username).exists():
            messages.warning(request, 'Please Enter Unique Username, Your username is also available ')
            return redirect('RegistrationForm')
        else:
            # Create The User
            user = User.objects.create_user(username=Username, email=Email, password=Pass, first_name=First_Name,
                                            last_name=Last_Name)
            profile = Profile(user=user, photo=Photo, bio=Bio)

            user.save()
            profile.save()
            messages.success(request, "Your BLOGGY-JI Account Has Been Successfully Created, Now  Its Time To Login ...")

        return redirect('LoginForm')
    else:
        return HttpResponse('404 - Not Found')


def ForgotPassword(request):
    Username = request.POST['uname']
    email = request.POST['email']
    password = request.POST['pass']

    if len(password) != 8:
        messages.warning(request, "Password must be 8 character ")
        return redirect('ForgotPasswordForm')
    if not password.isalnum():
        messages.warning(request, "Password must be alphanumeric")
        return redirect('ForgotPasswordForm')
    user = User.objects.filter(username=Username, email=email).first()
    if user:
        user.set_password(password)
        user.save()
        messages.success(request, 'Password Updated Successfully, Now its time to login')
        return redirect('LoginForm')
    else:
        messages.warning(request, 'Your Details is not Correct')
        return redirect('ForgotPasswordForm')


def ForgotPasswordForm(request):
    return render(request, 'user/ForgotPassword.html')


def EditProfile(request, id):
    if request.method == 'POST':
        Username = request.POST['Username']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Email = request.POST['Email']
        Bio = request.POST['Bio']
        ProfilePhoto = request.FILES.get('ProfilePhoto')

        if ProfilePhoto is None:
            try:
                profile = Profile.objects.get(user=request.user)
                ProfilePhoto = profile.photo
            except ObjectDoesNotExist:
                pass
        user = User.objects.get(id=id)
        user.username = Username
        user.first_name = FirstName
        user.last_name = LastName
        user.email = Email
        user.save()
        profile = Profile.objects.get(user=id)
        profile.bio = Bio
        profile.photo = ProfilePhoto
        profile.save()
        messages.success(request, 'Your Profile Has Been Updated Successfully.')

        return redirect('Profile')
