from django.db import models

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.image), filename])

class GlobalInventory(models.Model):
    item_name = models.CharField(max_length=20, null=False, unique=True)
    description = models.TextField(max_length=100, null=True)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to=nameFile, max_length=254, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    # image2 = models.


    class Meta:
        db_table = 'GlobalInventory'

    # def delete(self, using=None, keep_parents=False):
    #
    #     return super(GlobalInventory, self).delete()