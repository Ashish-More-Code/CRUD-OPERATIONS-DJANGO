from django.urls import path
from msgapp import views

urlpatterns = [
    path('',views.creat),
    path('dashboard',views.dashboard),
    path('delete/<rid>',views.delete),
     path('edit/<rid>',views.edit)

]