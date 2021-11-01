from django.contrib import admin
from .models import (
    Category,
    Enrollment,
    SubscriptionType,
    Module,
    Group,
    Course,
    Subscription,
    Event,
    Recording,
)

admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Enrollment)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Event)
admin.site.register(SubscriptionType)
admin.site.register(Recording)
admin.site.register(Subscription)

# Register your models here.
