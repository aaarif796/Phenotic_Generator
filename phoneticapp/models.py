from django.db import models

# Create your models here.
class Translation(models.Model):
    id = models.AutoField(primary_key=True)
    original_text = models.CharField(max_length=255)
    nepali_translation = models.CharField(max_length=255,default='')
    hindi_translation = models.CharField(max_length=255)
    urdu_translation = models.CharField(max_length=255)
    telugu_translation = models.CharField(max_length=255,default='')
    original_phonetic = models.CharField(max_length=255)
    hindi_phonetic = models.CharField(max_length=255)
    urdu_phonetic = models.CharField(max_length=255)
    nepali_phonetic = models.CharField(max_length=255,default='')
    telugu_phonetic = models.CharField(max_length=255,default = '')