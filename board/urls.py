from django.urls import path
from board.views import AdCreateApiView, AdDetailApiView, AdUpdateApiView, AdDeleteApiView, AdListApiView

from board.apps import BoardConfig

app_name = BoardConfig.name

urlpatterns = [
    path('create/', AdCreateApiView.as_view(), name='create'),
    path('<int:pk>/detail/', AdDetailApiView.as_view(), name='create'),
    path('<int:pk>/update/', AdUpdateApiView.as_view(), name='update'),
    path('<int:pk>/delete/', AdDeleteApiView.as_view(), name='delete'),
    path('list/', AdListApiView.as_view(), name='list')
]