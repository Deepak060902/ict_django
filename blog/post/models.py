from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to="blog_images/")
    content = models.TextField()   
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    likes = models.IntegerField()

    def __str__(self):
        return self.title
    