from rest_framework import serializers
from rest_framework.validators import ValidationError

from operations.models import DriverProfile, Address, DriverReport


class ProfileAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DriverProfileSerializer(serializers.ModelSerializer):
    address = ProfileAddressSerializer()

    def validate_document_number(self, document_number):
        if DriverProfile.objects.filter(document_number=document_number).exists():
            raise ValidationError('Não é possível cadastrar um usuário com um CPF já utilizado')
        return document_number

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        if address_data:
            address = Address.objects.create(**address_data)

        instance = DriverProfile.objects.create(address=address, **validated_data)

        return instance

    class Meta:
        model = DriverProfile
        fields = '__all__'


class DriverReportSerializer(serializers.ModelSerializer):
    origin = ProfileAddressSerializer(required=False)
    destination = ProfileAddressSerializer(required=False)
    driver = DriverProfileSerializer(required=False)
    document_number = serializers.CharField(required=False)

    def validate_document_number(self, document_number):
        if not DriverProfile.objects.filter(document_number=document_number).exists():
            raise ValidationError('Favor cadastrar o motorista antes de realisar seu report')
        return document_number

    def create(self, validated_data):
        origin_data = validated_data.pop('origin')
        destination_data = validated_data.pop('destination')
        document_number = validated_data.pop('document_number')

        origin = Address.objects.get_or_create(**origin_data)[0] if origin_data else None
        destination = Address.objects.get_or_create(**destination_data)[0] if destination_data else None
        driver = DriverProfile.objects.get(document_number=document_number)

        instance = DriverReport.objects.create(origin=origin, destination=destination, driver=driver, **validated_data)

        return instance

    class Meta:
        model = DriverReport
        fields = '__all__'


class DriverNestedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = ('id', 'name', 'vehicle_type')


class OriginDestinationSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    origin = ProfileAddressSerializer()
    destination = ProfileAddressSerializer()
    driver = DriverNestedProfileSerializer(required=False)

    def get_type(self, instance):
        return instance.driver.vehicle_type

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    class Meta:
        model = DriverReport
        fields = ('origin', 'destination', 'type', 'driver')
