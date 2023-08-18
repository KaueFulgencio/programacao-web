from django.urls import path
from app_projeto_final import views

urlpatterns = [
    path('',views.home,name="home"),
    path('usuarios/', views.usuarios, name="usuarios_cadastrados")
]
