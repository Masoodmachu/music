
from music import views
from django.urls import path, include
app_name='music'

urlpatterns = [

    path('',views.index,name='home'),
    path('hindi/',views.hindi,name='hindi'),
    path('thamil/',views.thamil,name='thamil'),
    path('malayalam/',views.malayalam,name='malayalam'),
    path('english/',views.english,name='english'),
    path('events/',views.events,name='events'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('album/',views.album,name='album'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('dt/<int:id>',views.dt,name='dt'),

]
