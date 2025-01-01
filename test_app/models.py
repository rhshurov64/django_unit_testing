from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


"""This model is for explore the unit testing of model"""


class DummyData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def is_adult(self):
        return self.age >= 18

    class Meta:
        verbose_name = "Dummy Data"
        verbose_name_plural = "Dummy Data"

        unique_together = ["first_name", "last_name"]

    def __str__(self):
        return self.first_name + " " + self.last_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def update_negative_price(sender, instance, **kwargs):
    if instance.price < 0:
        instance.price = 0
        instance.save()
