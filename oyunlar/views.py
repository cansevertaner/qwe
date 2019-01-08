import json
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
# Create your views here.
from .models import Games, Votes

from django.contrib import messages


def index(request):
    games = Games.objects.all()
    for i in games:
        i.img_name=str(i.game_img)[14:]
        if i.get_vote_count() % 10 == 1:
            i.yildiz = 1
        elif i.get_vote_count() % 20 == 2:
            i.yildiz = 2
        elif i.get_vote_count() % 30 == 3:
            i.yildiz = 3
        elif i.get_vote_count() % 40 == 4:
            i.yildiz = 4
        elif i.get_vote_count() % 50 == 5:
            i.yildiz = 5
    return render(request, 'oyunlar/index.html', {'games': games})
def hakkimizda(request):

    return render(request, 'oyunlar/hakkimizda.html')
def profil(request,user_id):
    if request.user.id:
        user=User.objects.get(id=user_id)
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user.username = username
            user.set_password(password)
            user.save()
            auth_login(request, user)

        return render(request,'oyunlar/profil.html', {'user':user})
def login_sign(request):
    if not request.user.id:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect(reverse('index'))
        else:
            hata = "0"
            if username != None and password != None:
                hata = "1"
            return render(request, 'oyunlar/login_sign.html',{'hata':hata})
    else:
        auth_logout(request)
        return redirect(reverse('login_sign'))
    return render(request, 'oyunlar/login_sign.html')


def new_register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')

    is_user = User.objects.filter(username=username)
    is_user_mail=User.objects.filter(email=email)
    if not is_user and not is_user_mail:
        user = authenticate(request, username=username, email=email, password=password)
        if (user is None) and (username is not None):
            User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect(reverse('index'))
    else:
        if is_user or is_user_mail:
            hata_mes="1"
            return render(request, 'oyunlar/new_register.html', {'hata_mes': hata_mes})
    return render(request, 'oyunlar/new_register.html')

def game_detail(request,game_id):
    game=Games.objects.get(id=game_id)
    yildiz2=""
    static1=game.game_title+"/TemplateData/favicon.ico"
    static2=game.game_title+"/TemplateData/style.css"
    static3=game.game_title+"/TemplateData/UnityProgress.js"
    static4=game.game_title+"/Build/UnityLoader.js"
    static5=game.game_title+"/Build/"+game.game_title+".json"
    if game.get_vote_count()%10==1:
        yildiz2=1
    elif game.get_vote_count()%20==2:
        yildiz2 = 2
    elif game.get_vote_count() % 30 == 3:
        yildiz2 = 3
    elif game.get_vote_count() % 40 == 4:
        yildiz2 = 4
    elif game.get_vote_count() % 50 == 5:
        yildiz2 = 5
    return render(request, 'oyunlar/game_detail.html', {'static1':static1,'static2':static2,'static3':static3,'static4':static4,'static5':static5,'game':game,'yildiz':yildiz2})
def votes(request,game_id):
    game=Games.objects.get(id=game_id)
    content_type = ContentType.objects.get_for_model(Games)
    obj_id = game.id
    user = request.user
    if request.is_ajax():
        vote_sts=request.POST.get('value_sts')
        if request.POST:
            is_vote_user=Votes.objects.filter(user=user,object_id=obj_id)
            if is_vote_user:
                user.voted = True
                durum=2
            else:
                user.voted = False
                durum=1
            if not user.voted:
                new_vote_question = Votes(user=user, content_type=content_type,object_id=obj_id,value_sts=vote_sts)
                new_vote_question.save()
                user.voted=True
                total_vote=game.get_vote_count()
                dump=json.dumps({
                    'vote': total_vote,
                    'durum': durum,
                })
            else:
                user.voted = False
                is_vote_user.first().delete()
                total_vote=game.get_vote_count()

                dump=json.dumps({
                    'vote': total_vote,
                    'durum': durum,
                })
    return HttpResponse(dump,content_type='application/json')