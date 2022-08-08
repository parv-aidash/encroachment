from rest_framework import serializers

from .models import *

class EncroachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encroachments
        fields = ['Encrt_ID', 'Departments', 'Reason_For_Rejection', 
        'Encroachment_Status', 'Encrt_Type', 'Region', 'Subregion', 
        'Encrt_Size', 'Distance_From_Centre_Of_Asset', 'Criticality', 
        'Assigned_To', 'Date', 'Department_Status', 'Comments', 'Image', 
        'Updated_By', 'Resolved_By', 'Audited_On','centroid' ,'geometry']

class EncroachmentTypeChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncroachmentTypeChoice
        fields = [
            'Encrt_ID', 'Encrt_Type', 'Region', 'Subregion',
            'Encrt_Size', 'Distance_From_Centre_Of_Asset', 'Criticality']


class EncroachmentCriticalityChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncroachmentCriticalityChoice
        ffields = [
            'Encrt_ID', 'Encrt_Type', 'Region', 'Subregion',
            'Encrt_Size', 'Distance_From_Centre_Of_Asset', 'Criticality']


class EncroachmentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncroachmentDetails
        ffields = [
            'Encrt_ID', 'Encrt_Type', 'Region', 'Subregion',
            'Encrt_Size', 'Distance_From_Centre_Of_Asset', 'Criticality',
            'Date', 'Department_Status', 'Comments', 'Image', 
            'Updated_By']

