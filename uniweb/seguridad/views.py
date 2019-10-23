from django.shortcuts import render

from .forms import SignUpForm, ChangeUserForm#, ChangePassword
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import (ListView,
    CreateView, 
	UpdateView, 
	DeleteView)

def ingresoUsuario(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('seguridad:mantenimiento_usuarios')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def Usuarios(request):
    lstUsuarios = User.objects.all()
    return render(request, 'seguridad/usuarios_list.html', {'Usuarios': lstUsuarios})

class usuarioActualizar(UpdateView):
    form_class = ChangeUserForm
    template_name = 'seguridad/usuario_template.html'
    model = User
    
    def form_valid(self, form_class):
        user = form_class.save()
        return redirect('seguridad:mantenimiento_usuarios')

#class usuarioSetPassword(UpdateView):
#    form_class = ChangePassword
#    template_name = 'seguridad/usuario_template.html'
#    model = User
    
#    def form_valid(self, form_class):
#        user = form_class.save()
#        return redirect('seguridad:mantenimiento_usuarios')

    
def usuario_editar(request, pk, estado):
    user = get_object_or_404(User, pk=pk)
    if estado == 1:
        user.is_active = 1
    elif estado == 0:
        user.is_active = 0
    user.save()
    return redirect('seguridad:mantenimiento_usuarios')