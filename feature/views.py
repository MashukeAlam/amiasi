from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feature, FeatureConsumptionHistory
from .forms import FeatureForm
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.http import require_POST

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

@login_required
def youtube_view(request):
    # Get all `youtube_like` features not yet consumed by the current user
    consumed_feature_ids = FeatureConsumptionHistory.objects.filter(
        user=request.user
    ).values_list('feature_id', flat=True)

    unconsumed_features = Feature.objects.filter(
        feature_name='youtube_view'
    ).exclude(
        id__in=consumed_feature_ids
    ).order_by('?')  # random order

    features_data = list(unconsumed_features.values('id', 'link', 'feature_name'))

    return render(request, 'feature/youtube_view.html', {
        'features': features_data
    })


@csrf_exempt
@require_POST
@login_required
def consume_feature(request):
    try:
        feature_id = int(request.POST.get('feature_id'))
        feature = Feature.objects.get(id=feature_id)

        # Check last consumption time
        last_consumption = FeatureConsumptionHistory.objects.filter(
            user=request.user
        ).order_by('-created_at').first()

        if last_consumption:
            time_diff = timezone.now() - last_consumption.created_at
            if time_diff < timedelta(seconds=15):
                return JsonResponse({'error': 'Wait at least 15 seconds before consuming again.'}, status=400)

        # Record the consumption
        FeatureConsumptionHistory.objects.create(
            user=request.user,
            feature=feature
        )

        # Increase user's credit
        request.user.credit.increase(feature.reward)

        return JsonResponse({'success': True, 'reward': feature.reward})
    except Feature.DoesNotExist:
        return JsonResponse({'error': 'Feature not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

