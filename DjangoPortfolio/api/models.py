from django.db import models
import os

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    posted = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')
    thumbnail = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    #caption = models.Charfield(max_length=50)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title + ": " + os.path.basename(self.image.name)

class Tag(models.Model):
    TYPE_TOOL=[
        ('T', 'Tool'),
        ('L', 'Language'),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE_TOOL)

    def __str__(self):
        return self.name

class DetailBody(models.Model):
    intro = models.TextField()
    body = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE)