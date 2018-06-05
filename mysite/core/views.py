from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.core.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.first_name = form.cleaned_data.get('password1')
            post.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('https://m.facebook.com/groups/bidformedgte/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
