from django.db import models

# Create your models here.
class Task(models.Model):

    task_status = [
        ("D", "Done"),
        ("P", "In Progress"),
        ("Q", "Queued"),
    ]

    time = models.DateTimeField(auto_created=True, auto_now=True)
    title = models.TextField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.CharField(max_length=1, choices=task_status, default="Q")

    def __repr__ (self):
        return self.title
    
