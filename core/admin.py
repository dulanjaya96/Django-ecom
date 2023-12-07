from django.contrib import admin
from .models import Item, Order, OrderItem, Payment, Coupon, Refund, Profile
import csv
from django.http import HttpResponse
from rangefilter.filter import DateRangeFilter

 
def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'

def export_orders(modeladmin, request, queryset):  
    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders_report.csv"'

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Order ID', 'User', 'Ordered Date', 'Billing Address', 'Payment', 'Coupon', 'Refund Requested', 'Refund Granted'])

    # Write each order's information to the CSV file
    for order in queryset:
        writer.writerow([
            order.id,
            order.user.username,
            order.ordered_date,
            order.billing_address,
            order.payment,
            order.coupon,
            order.refund_requested,
            order.refund_granted,
        ])

    return response

export_orders.short_description = "generate report"


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',                    
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',        
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = [('ordered_date', DateRangeFilter),
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                   ]
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted,
               export_orders]





admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Profile)
# admin.site.register(UserProfile)
