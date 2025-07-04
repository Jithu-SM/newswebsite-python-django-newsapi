from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=500, default="Unknown URL")
    image_url = models.URLField(blank=True, null=True)
    pub_date = models.DateTimeField()
    source = models.CharField(max_length=100, default="Unknown Source")

    def __str__(self):
        return self.title