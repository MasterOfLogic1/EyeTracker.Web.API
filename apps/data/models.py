from django.db import models
from apps.accounts.models import User  # adjust path if needed

class Efis(models.Model):
    section_id = models.CharField(max_length=50)
    recording_id = models.CharField(max_length=50)
    fixation_id = models.CharField(max_length=50)
    start_timestamp = models.FloatField()
    end_timestamp = models.FloatField()
    duration = models.FloatField()
    fixation_detected_on_surface = models.BooleanField()
    fixation_x = models.FloatField()
    fixation_y = models.FloatField()
    # Link to the user; Django will create a column named "user_id" in the DB.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="efis_data")
    owner_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email} - Fixation {self.fixation_id}"
    
    class Meta:
        db_table = 'EfisData'
        verbose_name = 'EfisData'
        verbose_name_plural = 'EfisData'

class Pfd(models.Model):
    section_id = models.CharField(max_length=50)
    recording_id = models.CharField(max_length=50)
    fixation_id = models.CharField(max_length=50)
    start_timestamp = models.FloatField()
    end_timestamp = models.FloatField()
    duration = models.FloatField()
    fixation_detected_on_surface = models.BooleanField()
    fixation_x = models.FloatField()
    fixation_y = models.FloatField()
    # Link to the user; Django will create a column named "user_id" in the DB.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pfd_data")
    owner_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email} - Fixation {self.fixation_id}"
    
    class Meta:
        db_table = 'PfdData'
        verbose_name = 'PfdData'
        verbose_name_plural = 'PfdData'


class Ecam(models.Model):
    section_id = models.CharField(max_length=50)
    recording_id = models.CharField(max_length=50)
    fixation_id = models.CharField(max_length=50)
    start_timestamp = models.FloatField()
    end_timestamp = models.FloatField()
    duration = models.FloatField()
    fixation_detected_on_surface = models.BooleanField()
    fixation_x = models.FloatField()
    fixation_y = models.FloatField()
    # Link to the user; Django will create a column named "user_id" in the DB.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ecam_data")
    owner_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email} - Fixation {self.fixation_id}"
    
    class Meta:
        db_table = 'EcamData'
        verbose_name = 'EcamData'
        verbose_name_plural = 'EcamData'
