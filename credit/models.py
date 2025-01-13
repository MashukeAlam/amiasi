from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Credit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=20)

    def __str__(self):
        return f"{self.amount} 💸"
    
class CreditRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PAYMENT_METHOD_CHOICES = [
        ('bkash', 'Bkash'),
    ]
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default='bkash')
    transaction_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    amount = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def approve(self):
        """Increase the user's credit when the request is approved."""
        if not self.approved:
            print(self.user)
            self.approved = True
            credit = Credit.objects.get(user=self.user)
            credit.amount += self.amount
            credit.save()
            self.save()

    def __str__(self):
        return f"Credit Request {self.id} by {self.user.username} for {self.amount} BDT"
    
@receiver(post_save, sender=User)
def create_user_credit(sender, instance, created, **kwargs):
    if created:
        Credit.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_credit(sender, instance, **kwargs):
    instance.credit.save()
