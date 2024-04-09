from django.db import models

#Import from othr apps
from apps.users.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    init_date = models.DateField()
    end_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.name
        
class Task(models.Model):
    TYPE_OF_PRIORITY = (
        ("H", "High"),
        ("M", "Medium"),
        ("S", "Small"),
    )
    
    description = models.CharField(max_length=250)
    end_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete = models.DO_NOTHING)
    priority = models.CharField(max_length=60, choices=TYPE_OF_PRIORITY, default = "M")
    
    def __str__(self) -> str:
        return self.description
    
class Comment(models.Model):
    init_date = models.DateTimeField()
    content = models.CharField(max_length=120)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
class Member(models.Model):
    # Specifying the choices
    ROLS_OF_THE_MEMBER = (
        ("OP", "Operator"),
        ("SL", "Seller"),
        ("PR", "President"),
        ("TR", "Transport"),
    )
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete = models.DO_NOTHING)
    rol = models.CharField(max_length = 20, choices = ROLS_OF_THE_MEMBER, default = 'OP')
    date = models.DateTimeField()
    
class Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    

    