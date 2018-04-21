from django.db import models
from django.utils import timezone

# Create your models here.
class BrewInfo(models.Model):
    bean_text = models.CharField(u'咖啡豆', max_length=50)
    pub_date = models.DateTimeField(u'创建时间', default=timezone.now)

    def __str__(self):
        return '咖啡: ' + self.bean_text

    class Meta:
        verbose_name = '冲煮信息'
        verbose_name_plural = '冲煮信息'
