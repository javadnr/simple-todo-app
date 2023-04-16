from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class PostModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    created =models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):    
        return reverse("post_detail", args=[str(self.id)])