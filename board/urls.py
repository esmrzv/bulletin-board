from django.urls import path
from board.views import AdCreateApiView, AdDetailApiView, AdUpdateApiView, AdDeleteApiView, AdListApiView, \
    FeedbackListApiView, FeedbackDetailApiView, FeedbackUpdateApiView, FeedbackDeleteApiView, FeedbackCreateApiView

from board.apps import BoardConfig

app_name = BoardConfig.name

urlpatterns = [
    path('create/', AdCreateApiView.as_view(), name='create'),
    path('<int:pk>/detail/', AdDetailApiView.as_view(), name='create'),
    path('<int:pk>/update/', AdUpdateApiView.as_view(), name='update'),
    path('<int:pk>/delete/', AdDeleteApiView.as_view(), name='delete'),
    path('list/', AdListApiView.as_view(), name='list'),
    path('feedback/list/', FeedbackListApiView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/detail/', FeedbackDetailApiView.as_view(), name='feedback-detail'),
    path('feedback/<int:pk>/update/', FeedbackUpdateApiView.as_view(), name='feedback-update'),
    path('feedback/<int:pk>/delete/', FeedbackDeleteApiView.as_view(), name='feedback-delete'),
    path('feedback/create/', FeedbackCreateApiView.as_view(), name='feedback-create'),


]