from django.contrib import admin

# Register your models here.

from .models import USER_TYPE, USER_MASTER, PLAN_MASTER, MEMBERSHIP_MASTER, TRAINER_DETAILS, PAYMENT_MASTER, PRODUCT_MASTER, FEEDBACK_MASTER, WORKOUT_MASTER, ORDER_MASTER, ORDER_DETAILS, ATTENDANCE_MASTER

admin.site.register(USER_TYPE)
admin.site.register(USER_MASTER)
admin.site.register(PLAN_MASTER)
admin.site.register(MEMBERSHIP_MASTER)
admin.site.register(TRAINER_DETAILS)
admin.site.register(PAYMENT_MASTER)
admin.site.register(PRODUCT_MASTER)
admin.site.register(FEEDBACK_MASTER)
admin.site.register(WORKOUT_MASTER)
admin.site.register(ORDER_MASTER)
admin.site.register(ORDER_DETAILS)
admin.site.register(ATTENDANCE_MASTER)