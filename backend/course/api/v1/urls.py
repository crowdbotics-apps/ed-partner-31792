from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet,
    LessonViewSet,
    EnrollmentViewSet,
    SubscriptionTypeViewSet,
    PaymentMethodViewSet,
    ModuleViewSet,
    GroupViewSet,
    CourseViewSet,
    SubscriptionViewSet,
    EventViewSet,
    RecordingViewSet,
)

router = DefaultRouter()
router.register("category", CategoryViewSet)
router.register("module", ModuleViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("group", GroupViewSet)
router.register("course", CourseViewSet)
router.register("event", EventViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("recording", RecordingViewSet)
router.register("lesson", LessonViewSet)
router.register("subscription", SubscriptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
