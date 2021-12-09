from django.db import models as md

# Create your models here.
class Bb(md.Model):
    title = md.CharField(max_length = 50, verbose_name = 'product')
    content = md.TextField(null = True, blank = True, verbose_name = 'description')
    price = md.FloatField(null = True, blank = True, verbose_name = 'price')
    published = md.DateTimeField(auto_now_add = True, db_index = True, verbose_name = 'published at')

    class Meta:
        verbose_name_plural = 'announcements'
        verbose_name = 'announcement'
        ordering = ['-published']