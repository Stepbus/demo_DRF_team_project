from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    """Note: The code above sets is_staff, is_active, and is_superuser to True for every user
    that successfully registers, which not what you'd want in a real-world application for security reasons.
    This example is to demonstrate how you could set these fields. In a real-world application,
    it would want to have some logic to determine who gets these privileges."""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True
            user.save()
            login(request, user)
            return redirect('api-root')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
