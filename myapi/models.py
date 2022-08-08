from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as gismodels

# Create your models here.
class Encroachments(models.Model):
    Encrt_ID = models.CharField(max_length=60)
    Departments = models.CharField(max_length=60)
    Reason_For_Rejection = models.CharField(max_length=60)
    Encroachment_Status = models.CharField(max_length=60)
    Encrt_Type = models.CharField(max_length=60)
    Region = models.CharField(max_length=60)
    Subregion = models.CharField(max_length=60)
    Encrt_Size = models.IntegerField()
    Distance_From_Centre_Of_Asset = models.IntegerField()
    Criticality = models.CharField(max_length=60)
    Assigned_To = models.CharField(max_length=60)
    Date = models.DateField()
    Department_Status = models.CharField(max_length=60)
    Comments = models.CharField(max_length=60, null=True, blank=True)
    Image = models.CharField(max_length=60, null=True, blank=True)
    Updated_By = models.CharField(max_length=60, null=True, blank=True)
    Resolved_By = models.CharField(max_length=60, null=True, blank=True)
    Audited_On = models.DateField(null=True, blank=True)
    centroid = gismodels.PointField(
        srid=4326, null=True, blank=True)
    geometry = gismodels.GeometryCollectionField(
        srid=4326, null=True, blank=True)

    def __str__(self):
        return self.Encrt_ID


class EncroachmentTypeChoice(Encroachments):
    class Meta:
        db_table = 'pl_t_encroachment_type_choice'
        verbose_name = _('Encroachment Type Choice')
        verbose_name_plural = _('Encroachments Type  Choices')
        ordering = ['Date']

    def __str__(self):
        return '%s (%s)' % (self.__class__.__name__, self.Encrt_ID)

class EncroachmentCriticalityChoice(Encroachments):
    class Meta:
        db_table = 'pl_t_encroachment_criticality_choice'
        verbose_name = _('Encroachment Criticality Choice')
        verbose_name_plural = _('Encroachments Criticality Choice')
        ordering = ['Date']

    def __str__(self):
        return '%s (%s)' % (self.__class__.__name__, self.Encrt_ID)

class EncroachmentDetails(Encroachments):
    class Meta:
        db_table = 'pl_t_encroachment_details'
        verbose_name = _('Encroachment Details')
        verbose_name_plural = _('Encroachment Details')
        ordering = ['Date']

    def __str__(self):
        return '%s (%s)' % (self.__class__.__name__, self.Encrt_ID)