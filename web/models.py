from django.db import models

class ItemsFile(models.Model):
    store = models.PositiveIntegerField()
    upload_date = models.DateTimeField()
    activate = models.BooleanField()
    specifications = models.FileField(upload_to='csv')

    def __str__(self):
        return str(self.store) + ': ' + str(self.upload_date)
    
class HotItem(models.Model):
    store = models.PositiveIntegerField()
    item_num = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default='')
    reg_price = models.DecimalField(decimal_places=2, max_digits=12)
    sale_price = models.DecimalField(decimal_places=2, max_digits=12)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return str(self.store) + ': ' + str(self.item_num)
    