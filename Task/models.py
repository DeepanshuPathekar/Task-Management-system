from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    Pending = 'Pending'
    Done = 'Done'
    TASK_TYPES = [
        (Pending, 'Pending'),
        (Done, 'Done'),
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_detail = models.TextField()
    task_type = models.CharField(max_length=10, choices=TASK_TYPES)

    def __str__(self):
        return f"Task for {self.user.name}: {self.task_detail}"
