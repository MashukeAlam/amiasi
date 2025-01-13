from django.contrib import admin
from .models import Credit, CreditRequest

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')

@admin.register(CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'transaction_number', 'phone_number', 'amount', 'approved', 'created_at', 'updated_at')
    list_filter = ['payment_method', 'approved', 'created_at']
    search_fields = ['user__username', 'transaction_number']

    actions = ['approve_credit_requests']

    def approve_credit_requests(self, request, queryset):
        updated_count = 0
        for credit_request in queryset:
            if not credit_request.approved:
                credit_request.approve()  # Approve and update the user's credit
                updated_count += 1
        self.message_user(request, f'{updated_count} credit request(s) approved and user credit updated.')
    approve_credit_requests.short_description = 'Approve selected credit requests and update user credit'