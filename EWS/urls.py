from django.urls import path
from . import views

urlpatterns = [
	path('', views.Firstpage),
	path('Paps/', views.Page, name="Paps"),

]












