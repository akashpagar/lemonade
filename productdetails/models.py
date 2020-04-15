from django.db import models

class ProjectType(models.Model):
    category = models.CharField(blank=True, null=True, max_length=25)

class Project(models.Model):
    ProjectID = models.IntegerField(primary_key=True)
    RefProjectType = models.ForeignKey(ProjectType, related_name='ProjecttypeID',
                                       on_delete=models.PROTECT, null=True, blank=True)
    ProjectName = models.CharField(blank=True, null=True, max_length=25)
    ClientID = models.IntegerField(unique=True)

class Task(models.Model):
    TaskID = models.IntegerField(primary_key=True)
    TaskName = models.CharField(blank=True, null=True, max_length=25)
    ProjectRef = models.ForeignKey(Project, related_name='projectID',
                                   on_delete=models.PROTECT, null=True, blank=True)
    TaskSecID = models.IntegerField()
    AssignedTo = models.IntegerField(blank=True, null=True)
    Notes = models.TextField(blank=True, null=False, max_length=1000)


