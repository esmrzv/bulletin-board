from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from board.models import Ad, Feedback
from board.paginators import MyPagination
from board.serializers import AdSerializer, FeedbackSerializer


class AdCreateApiView(CreateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdListApiView(ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = MyPagination


class AdDetailApiView(RetrieveAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdUpdateApiView(UpdateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdDeleteApiView(DestroyAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class FeedbackListApiView(ListAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackDetailApiView(RetrieveAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackCreateApiView(CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackUpdateApiView(UpdateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackDeleteApiView(DestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
