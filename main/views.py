from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.


def Home(request):
    if request.user.is_authenticated:
        return redirect('/landing')
    template = loader.get_template('home.html')
    ctx = {
        'loggedin': "No",
        'header': "front-header"
    }
    return HttpResponse(template.render(ctx))


# @login_required(login_url='/')
class Landing(TemplateView):
    template_name = 'landing.html'


@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/landing')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/landing')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    return redirect('/accounts/login')

# Logout function. Redirects user to index page on logout


def logoutPage(request):
    logout(request)
    return redirect('/accounts/login')


# class SignupPageView(TemplateView):
#     form = CustomSignupForm
#     initial = {'key': 'value'}
#     template_name = "signup.html"

#     def get(self, request, *args, **kwargs):
#         form = self.form(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
