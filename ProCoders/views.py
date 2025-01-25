from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from .models import *

# home page 
def index(request):
    languages = Languages.objects.all()
    return render(request, 'index.html',{'languages' : languages})

# SignIn page 
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'This Email is Already Registerd')
                return redirect('/User/SignIn')

            elif User.objects.filter(username=username).exists():
                messages.info(request,'This Username is Already Exist\nplease Try anoter user name')
                return redirect('/User/SignIn')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('/User/LogIn')
        else :
            messages.info(request, 'The Password and Confirm Password did not match')
            return redirect('/User/SignIn')

    return render(request, 'User/Login/signin.html')

# LogIn page 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('/User/LogIn')
    return render(request, 'User/Login/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# profile page
def profile(request, profile):
    user = User.objects.get(username=profile)
    context = {
        'user' : user,
    }
    return render(request, "templates/User/Profile/profile.html", context=context)

# about page
def about(request):
    return render(request, 'Supports/About/index.html')

# quiz page
@login_required(login_url='/User/LogIn')
def quiz(request):
    languages = Languages.objects.all()
    return render(request, 'Quiz/index.html',{'languages' : languages })
    
# quiz_lang page
@login_required(login_url='/User/LogIn')
def quiz_lang(request,lang):
    return render(request, 'Quiz/Language/quiz.html', { 'lang' : lang })

@login_required(login_url='/User/LogIn')
def get_quiz(request, lang):
    language = Languages.objects.get(language=lang)
    quiz = Quiz.objects.filter(language=language).order_by('?').first()

    quiz_data = {
        'id': quiz.id,
        'question': quiz.question,
        'option1': quiz.option1,
        'option2': quiz.option2,
        'option3': quiz.option3,
        'option4': quiz.option4,
    }

    return JsonResponse({
        'quiz': quiz_data
    })

@login_required(login_url='/User/LogIn')
def check_ans(request, lang):
    ans = request.GET.get('ans')
    quiz_id = request.GET.get('quiz_id')
    quiz = Quiz.objects.get(id=quiz_id)
    
    quiz_data = {
        'id': quiz.id,
        'question': quiz.question,
        'option1': quiz.option1,
        'option2': quiz.option2,
        'option3': quiz.option3,
        'option4': quiz.option4,
        'answer': quiz.answer,
        'explanation': quiz.explanation,
    }

    if ans == quiz.answer:
        quiz_data['status'] = 'correct'
    else:
        quiz_data['status'] = 'wrong'


    return JsonResponse({
        'quiz': quiz_data
    })

# language page
def language(request, lang):
    languages = Languages.objects.all()
    l = Languages.objects.get(language=lang)
    return render(request, 'Supports/Language/index.html', context={'lang' : l, 'languages' : languages } )

# chatroom page
@login_required(login_url='/User/LogIn')
def chatroom(request):
        return render(request, 'ChatRoom/index.html')

@login_required(login_url='/User/LogIn')
def room(request,room):
    username = request.GET.get('username')
    room_detail = Room.objects.get(name=room)
    context = {
         'username' : username,
         'room' : room,
         'room_details' : room_detail

    }
    return render(request, 'ChatRoom/room.html', context=context)

@login_required(login_url='/User/LogIn')
def checkview(request):
    room_choice = request.POST['room_choice']
    room = request.POST['room_name']
    username = request.POST['username']

    if room_choice == "join":
        if Room.objects.filter(name = room).exists():
            return redirect('/chat_room/'+room)
        else :
            return HttpResponse("<H1>Room is Does not Exist</H1>")
    else:
        if not Room.objects.filter(name = room).exists():
            user = User.objects.get(username=username)
            new_room = Room.objects.create(name=room, created_by=user)
            new_room.save()
            return redirect('/chat_room/'+room)
        else :
            return HttpResponse("<H1>Room is Already Exist</H1>")
    
@login_required(login_url='/User/LogIn')
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    room = Room.objects.get(id=room_id)
    new_message = Message.objects.create(value=message, user=username, room=room)
    new_message.save()
    return HttpResponse("Message send Successfully")

@login_required(login_url='/User/LogIn')
def get_messages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({
         "messages" : list(messages.values())
    })
