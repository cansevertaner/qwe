from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    url('login_sign', views.login_sign, name='login_sign'),
    url('new_register', views.new_register, name='new_register'),
    url(r'^game_detail/(?P<game_id>\S+)', views.game_detail, name="game_detail"),
    url(r'^new_vote/(?P<game_id>\S+)', views.votes, name="new_vote"),
    url('hakkimizda', views.hakkimizda, name='hakkimizda'),
    url(r'^profil/(?P<user_id>\S+)', views.profil, name="profil"),

    url('', views.index, name='index'),

]
urlpatterns += staticfiles_urlpatterns()