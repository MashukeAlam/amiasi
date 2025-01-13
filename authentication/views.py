from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Ensure this URL matches your login URL name
        else:
            # Add error messages directly to the template context
            messages.error(request, 'There were errors in your form submission. Please fix them below.')
    else:
        form = CustomUserCreationForm()

    # Render the template with the form
    return render(request, 'registration/register.html', {'form': form})
