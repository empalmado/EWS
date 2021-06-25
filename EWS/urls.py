from django.urls import path
from . import views

urlpatterns = [
	path('', views.EstimatePage),
	path('Paps/', views.Page, name="Paps"),

]












