from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})