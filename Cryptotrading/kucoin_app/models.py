from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


# Create your models here.



class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)



class Kline(models.Model):
    market = models.TextField()
    timestamp = models.IntegerField()
    datetime = models.DateTimeField()
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    def __str__(self):
        s='<Kline {} {} {}>'.format(
            self.d,
            self.market,
            self.open,
        )
        return s

    def __repr__(self):
        return str(self)


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dateadded = models.DateTimeField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    telefon = models.TextField()
    password = models.TextField()
    group = ArrayField(models.IntegerField(), blank=True, default=list)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)





