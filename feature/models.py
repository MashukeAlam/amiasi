from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the default User model

class Feature(models.Model):
    feature_name = models.CharField(
        max_length=20,
        choices=[
            ('youtube_like', 'YouTube Like'),
            ('youtube_sub', 'YouTube Subscribe'),
            ('youtube_view', 'YouTube View')
        ]
    )
    link = models.CharField(max_length=255, null=True, blank=True)
    reward = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="features")

    def __str__(self):
        return str(self.feature_name)

class FeatureConsumptionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consumption_histories")
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="consumption_histories")
    consumption_type = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consumption by {self.user} for {self.feature}"
