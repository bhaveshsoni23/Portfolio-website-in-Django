from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    code_language = models.CharField(max_length=200)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/')
    photo_1 = models.ImageField(upload_to='photos/')
    photo_2 = models.ImageField(upload_to='photos/')
    photo_3 = models.ImageField(upload_to='photos/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default = datetime.now , blank = True)

    def __str__(self):
        return self.title 




