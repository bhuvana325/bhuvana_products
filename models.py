from django.db import models


# Create your models here.
class items(models.Model):
    name = models.CharField(max_length=20)
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField(null=True)

    def calc_volume(self):
        volume = self.cost_per_item * self.stock_quantity
        return volume

    def save(self, *args, **kwargs):
        self.volume = self.calc_volume()
        super(items, self).save()
