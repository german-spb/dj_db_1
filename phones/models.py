from django.db import models
from django.urls import reverse

class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.URLField()
    price = models.IntegerField(null=False)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', blank=True)

    # def get_absolute_url(self):
    #     return reverse('phone', kwargs={'slug': self.slug})

