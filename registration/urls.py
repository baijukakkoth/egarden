from django.urls import path
from .import views
urlpatterns = [
 path("", views.callName, name='studName'),
 path('first', views.firstENV, name='firstEnverionment'),
 path('second', views.callLink, name='hyperlinks'),
 path('third', views.callNewPage, name='newPage'),
]