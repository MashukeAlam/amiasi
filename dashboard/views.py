from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from feature.models import FeatureConsumptionHistory

@login_required
def dashboard_view(request):
    user = request.user

    # Calculate earnings per feature type
    top_features = (
        FeatureConsumptionHistory.objects.filter(user=user)
        .values('feature__feature_name')
        .annotate(total_earned=Sum('feature__reward'))
        .order_by('-total_earned')[:3]
    )

    feature_label_map = {
        'youtube_like': 'YouTube Likes',
        'youtube_sub': 'YouTube Subscriptions',
        'youtube_view': 'YouTube Views'
    }

    # Add readable names
    for item in top_features:
        item['label'] = feature_label_map.get(item['feature__feature_name'], item['feature__feature_name'])

    return render(request, 'dashboard/index.html', {
        "top_features": top_features
    })
