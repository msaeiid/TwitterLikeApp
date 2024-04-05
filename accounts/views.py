from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


# function based views to Class Base Views

def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect(reverse('home'))
    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login"
    }
    return render(request, 'accounts/auth.html', context)


def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect(reverse("login"))
    context = {
        "form": None,
        "description": "Are you sure you want to log out?",
        "btn_label": "Click to Confirm",
        "title": "Logout"
    }
    return render(request, 'accounts/auth.html', context)


def registration_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_ = form.save(commit=True)
        user_.set_password(form.cleaned_data.get('password1'))
        # TODO: send a confirmation email to verify their account.
        login(request, user_)
        return redirect(reverse('home'))
    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"
    }
    return render(request, 'accounts/auth.html', context)
