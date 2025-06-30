from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category}: {self.name}"