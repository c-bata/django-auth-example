from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('top')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})
