from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from .import views
urlpatterns = [

    path("", home, name="home"),
    path('vendor/', views.vendor, name='vendor'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('postavki/', views.postavki, name='postavki'),
    path('postavka/<int:post_id>', views.postavki_detail, name='postavki_detail'),
    path('proect/', views.proect, name='proect'),
    path('project/<int:project_id>', views.project_detail, name='project_detail'),
    path('card_info/<int:card_id>', views.card_detail, name='card_detail'),


    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('favourites/', favourite_list, name='favourite_list'),
    path('favourites/<int:id>/', favourite_add, name='favourite_add'),

    path('delete_contact/<int:pk>',
         views.delete_contact, name="delete-contact"),


]
