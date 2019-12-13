from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.

class Assignment(models.Model):
    status = models.IntegerField(default = 1)
    student = models.ForeignKey(User, related_name="student",on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='tasks_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    assignments = models.ManyToManyField(Assignment, related_name="assignments")
    owner = models.ForeignKey(User, related_name="owner",on_delete=models.CASCADE)

    def __str__(self):
        return "title:{} date posted:{}".format(self.title,self.date_posted)


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user)


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)