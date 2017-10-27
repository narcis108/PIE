from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView

from .forms import SignUpForm
from .models import Utilizator


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'index.htm')


def my_account(request):
    return render(request, 'my_account.html')


class AccountUpdate(UpdateView):
    model = Utilizator
    fields = ('first_name', 'last_name', 'data_nasterii', 'gender', )
    context_object_name = 'accountUpdate'
    template_name = 'update_account.html'


    def form_valid(self, form):
        user = form.save()
        user.save()
        return redirect('myAccount')
