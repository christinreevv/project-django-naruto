from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from sitewomen import settings
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html' #атрибут указывает на путь к шаблону Django, который будет использоваться для отображения формы аутентификации
    extra_context = {'title': 'Авторизация'} #этот атрибут позволяет добавить дополнительные данные в контекст шаблона

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html' #этот атрибут указывает на путь к шаблону Django, который будет использоваться для отображения формы регистрации
    extra_context = {'title': "Регистрация"} #этот атрибут позволяет добавить дополнительные данные в контекст шаблона
    success_url = reverse_lazy('users:login') #этот атрибут определяет URL-адрес страницы, на которую пользователь будет перенаправлен после успешной регистрации. reverse_lazy — это функция Django, которая возвращает URL-адрес по имени маршрута.

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html' #этот атрибут указывает на путь к шаблону Django, который будет использоваться для отображения формы обновления профиля
    extra_context = {
        'title': "Профиль пользователя", #в контекст шаблона добавляются две переменные: title со значением "Профиль пользователя"
        # и default_image со значением settings.DEFAULT_USER_IMAGE
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self): #этот метод определяет URL-адрес страницы, на которую пользователь будет перенаправлен после успешного обновления профиля
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):#этот метод определяет объект, который будет обновляться формой
        # в данном случае объектом будет текущий аутентифицированный пользователь (self.request.user)

        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")#этот атрибут определяет URL-адрес страницы, на которую пользователь будет перенаправлен после успешного изменения пароля
    template_name = "users/password_change_form.html" #этот атрибут указывает на путь к шаблону Django, который будет использоваться для отображения формы изменения пароля
