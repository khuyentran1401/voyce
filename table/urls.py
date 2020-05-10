from django.urls import path
from table import views

urlpatterns = [
	path('', views.view_table, name='table'),
	]