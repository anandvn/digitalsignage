from django.db import models

class ItemsFile(models.Model):
    store = models.PositiveIntegerField()
    upload_date = models.DateTimeField()
    activate = models.BooleanField()
    specifications = models.FileField(upload_to='csv')

    def __str__(self):
        return str(self.store) + ': ' + str(self.upload_date)