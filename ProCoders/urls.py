from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Supports/About', views.about, name='about'),
    path('Quiz', views.quiz, name='quiz'),
    path('Quiz/<str:lang>', views.quiz_lang, name='quiz_lang'),
    path('get_quiz/<str:lang>/', views.get_quiz, name='get_quiz'),
    path('check_ans/<str:lang>', views.check_ans, name='check_ans'),
    path('User/LogIn', views.login, name='login'),
    path('User/SignIn', views.signin, name='signin'),
    path('User/LogOut', views.logout, name='logout'),
    path('User/<str:profile>', views.profile, name='profile'),
    path('ChatRoom', views.chatroom, name='chatroom'),
    path('chat_room/<str:room>', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('chat_room/get_messages/<str:room>', views.get_messages, name='get_messages'),
    path('Supports/Language/<str:lang>', views.language, name='language'),
]