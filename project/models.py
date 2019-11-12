from django.db import models
from MainModule.CommonModels import CommonInfo
from django.conf import settings

# Create your models here.

class Project(CommonInfo):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'projects'

class Project_detail(CommonInfo):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_id')
    project_type = models.CharField(max_length=255)
    time = models.CharField(max_length=200, null=True)
    budget = models.CharField(max_length=255, null=True)
    dev_platfrom = models.CharField(max_length=255, null=True)
    server_platform = models.CharField(max_length=255, null=True)
    project_status = models.CharField(max_length=255, null=True)
    payment_status = models.CharField(max_length=255, null=True)
    payment_method = models.CharField(max_length=255, null=True)
    supervised_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='supervised_by',default=1)
    project_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_manager',default=1)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client',default=1)

    class Meta:
        db_table = 'project_details'
