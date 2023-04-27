from django.urls import path

from .views import LabsViewSet, UserAPIView

urlpatterns = [
    path('labs', LabsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', LabsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view())
]
