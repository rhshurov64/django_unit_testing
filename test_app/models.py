from django.db import models


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
