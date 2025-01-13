from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreditRequestForm
from django.contrib import messages

@login_required
def credit_request_view(request):
    if request.method == 'POST':
        form = CreditRequestForm(request.POST)
        if form.is_valid():
            credit_request = form.save(commit=False)
            credit_request.user = request.user  # Attach the logged-in user to the request
            credit_request.save()
            messages.success(request, 'Credit request submitted successfully!')
            return redirect('dashboard')  # Redirect to the dashboard or a success page
        else:
            messages.error(request, 'There was an error in your request. Please try again.')
    else:
        form = CreditRequestForm()
    # Get all credit requests for the current user
    credit_requests = request.user.creditrequest_set.all().order_by('-created_at')
    return render(request, 'credit/index.html', {'form': form, 'credit_requests': credit_requests})