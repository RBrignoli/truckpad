from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, mixins
from operations.serializers import DriverProfileSerializer, DriverReportSerializer, OriginDestinationSerializer
from rest_framework.decorators import action
from django.utils import timezone

from operations.models import DriverProfile, DriverReport


class DriverProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)  # TODO change to IsAuthenticated
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer

    @action(methods=['get'], detail=False, url_path='check-has-own-vehicle')
    def check_has_own_vehicle(self, request):
        has_own_vehicle = self.queryset.filter(own_vehicle=True).count()
        return Response(
            {'Motoristas com veículo próprio': has_own_vehicle},
            status=status.HTTP_200_OK
        )

    @action(methods=['get'], detail=False, url_path='check-document-number')
    def check_document_number(self, request):
        document_number = request.query_params.get('document_number', '')
        document_registered = self.queryset.filter(document_number=document_number).exists()
        return Response(
            {'document_registered': document_registered},
            status=status.HTTP_200_OK
        )


class DriverReportViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)  # TODO change to IsAuthenticated
    queryset = DriverReport.objects.all()
    serializer_class = DriverReportSerializer

    @action(methods=['get'], detail=False, url_path='check-transporting-reports')
    def check_transporting_reports(self, request):
        period = request.query_params.get('period', '')
        reports = self.queryset.filter(
            created_at__date__gte=(timezone.now() - timezone.timedelta(days=int(period))).date(),
            status=DriverReport.LOADED).count()
        return Response(
            {f'Reports de motoristas transportanto carga nos ultimos {period} dias': reports},
            status=status.HTTP_200_OK,
        )


class OriginDestinationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)  # TODO change to IsAuthenticated
    queryset = DriverReport.objects.filter(
        created_at__date__gte=(timezone.now() - timezone.timedelta(days=7)).date())
    serializer_class = OriginDestinationSerializer
