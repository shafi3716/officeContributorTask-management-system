from django.db import models
from django.conf import settings

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_created_by_user',on_delete=models.CASCADE, default=1)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_updated_by_user',on_delete=models.CASCADE, default=1)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_deleted_by_user',on_delete=models.CASCADE, default=1)

    class Meta:
        abstract = True