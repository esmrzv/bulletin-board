from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from board.models import Ad
from board.paginators import MyPagination
from board.serializers import AdSerializer


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
