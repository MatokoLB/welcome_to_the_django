from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name="cadastrar_funcionario" ),
    path('login/', views.login, name="login" ),
    path('logout/', views.logout, name="logout"),
    path('editar_funcionario/<int:id>', views.editar_funcionario, name="editar_funcionario"),
    path('update_funcionario/<int:id>', views.update_funcionario, name="update_funcionario"),
    path('delete_funcionario/<str:id>/', views.delete_funcionario, name="delete_funcionario"),
]