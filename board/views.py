from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from board.models import Ad, Feedback
from board.paginators import MyPagination
from board.serializers import AdSerializer, FeedbackSerializer
from users.permissions import IsAdmin, IsUser
from rest_framework.filters import SearchFilter


class AdCreateApiView(CreateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsUser | IsAdmin)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdListApiView(ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = MyPagination
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter]
    search_fields = ['title']


class AdDetailApiView(RetrieveAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsUser | IsAdmin)


class AdUpdateApiView(UpdateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsUser | IsAdmin,)


class AdDeleteApiView(DestroyAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsUser | IsAdmin, IsAuthenticated)


class FeedbackListApiView(ListAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsUser | IsAdmin)


class FeedbackDetailApiView(RetrieveAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsUser | IsAdmin)


class FeedbackCreateApiView(CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsUser | IsAdmin,)


class FeedbackUpdateApiView(UpdateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsUser | IsAdmin,)


class FeedbackDeleteApiView(DestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsUser | IsAdmin)
