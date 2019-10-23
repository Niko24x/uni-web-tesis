from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from .views import ingresoUsuario, Usuarios, usuarioActualizar, usuario_editar
from seguridad import views as seguridad_vistas
from django.contrib.auth import views as auth_views


app_name = 'seguridad'
urlpatterns = [
    #path('ingresousuario/', ingresoUsuario.as_view(), name='ingresoUsuario'),
    path('login/', auth_views.LoginView.as_view(template_name='seguridad/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/', Usuarios, name='mantenimiento_usuarios'),
    path('ingresousuario/', seguridad_vistas.ingresoUsuario, name='ingresoUsuario'),
    path('usuarios/<pk>/act/', login_required(usuarioActualizar.as_view()), name='usuario_actualizar'),
    #path('usuarios/<pk>/setpw/', login_required(usuarioSetPassword.as_view()), name=' usuario_setpw'),
    path('usuarios/<int:pk>/edit/<int:estado>', login_required(usuario_editar), name='usuario_editar'),
]
    