from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from django.db import IntegrityError, transaction, DatabaseError
from django.db.models import F, Value, CharField, Q, Min, Max, Count
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as drf_filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status as HTTP_STATUS
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

#render the different encoarchments in JSON format
from .serializers import *
from .models import *


class EncroachmentsViewSet(GenericViewSet):
    queryset = Encroachments.objects.all().order_by('Encrt_ID')
    serializer_class = EncroachmentsSerializer
    class Meta:
        db_table        = 'encroachment_view'
        unique_together = ('Encrt_ID', 'Departments')
        indexes         = [
            models.Index(fields=['Encrt_ID'])
        ]

class EncroachmentTypeChoiceViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    queryset = EncroachmentTypeChoice.objects.filter(Encroachment_Status='active')
    serializer_class = EncroachmentTypeChoiceSerializer
    filter_backends = (drf_filters.DjangoFilterBackend,)

class EncroachmentCriticalityChoiceViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    queryset = EncroachmentCriticalityChoice.objects.filter(Encroachment_Status='active')
    serializer_class = EncroachmentCriticalityChoiceSerializer
    filter_backends = (drf_filters.DjangoFilterBackend,)

class EncroachmentDetailsViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    queryset = EncroachmentDetails.objects.all()
    serializer_class = EncroachmentDetailsSerializer
    filter_backends = (drf_filters.DjangoFilterBackend,)

