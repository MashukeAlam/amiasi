from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feature
from .forms import FeatureForm

@login_required
def create_feature(request):
    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.user = request.user
            feature.save()
            messages.success(request, 'Feature created successfully!')
            return redirect('feature:index')  # Assuming you have a dashboard URL pattern
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeatureForm()
    # Get all features for the current user
    features = request.user.features.all().order_by('-created_at')

    return render(request, 'feature/index.html', {'form': form, 'features': features})


# Create your views here.

