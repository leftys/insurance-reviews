from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_review', views.new_review, name = 'new_review'),
    path('submit_review', views.submit_review, name = 'submit_review'),
    path('about', views.about, name = 'about'),
]
