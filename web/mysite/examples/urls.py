from django.urls import path
from . import views

urlpatterns = [
    path('dogs/<int:id>', views.dog, name="dog"),
    path('dogs/', views.dogs),
    path('calc/<operation>/<int:num1>/<int:num2>', views.calc),
    path('text/<user_text>', views.cool_text),
    path('hello/<imie>', views.hello),
    path('about', views.about),
    path('', views.index),
]