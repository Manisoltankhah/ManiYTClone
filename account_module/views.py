from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import status, generics
from rest_framework.response import Response
from .forms import RegisterForm, LoginForm
from .models import User
from api.serializer import UserSerializer
from rest_framework.permissions import AllowAny


# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def delete(self, request, *args, **kwargs):
#         User.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class CreateUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = User
#     permission_classes = [AllowAny]
#
# class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'pk'


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        # print(f'random string: {get_random_string(6)}')
        context = {
            "register_form": register_form
        }
        return render(request, 'sign-up-page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            username = register_form.cleaned_data.get('username')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if not user:
                new_user = User(email=user_email, is_active=True, username=username)
                new_user.set_password(user_password)
                new_user.save()
                # email_to_user = EmailMessage('activate user account', f'''http://127.0.0.1:8080/activate-account/{new_user.email_active_code}''', to=[f'{new_user.email}'])
                # email_to_user.send()
                return redirect(reverse('login-page'))
            else:
                register_form.add_error('email', 'email had been used')

        context = {
              "register_form": register_form
        }
        return render(request, 'sign-up-page.html', context)


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            "login_form": login_form
        }
        return render(request, 'login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'account is not active')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))

        context = {
             "login_form": login_form
        }
        return render(request, 'login_page.html', context)
