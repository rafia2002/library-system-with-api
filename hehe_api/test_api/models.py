from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=20)
    published_date = models.DateField()
    cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.title
