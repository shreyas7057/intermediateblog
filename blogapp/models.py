from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 
# Create your models here.


class BlogCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(BlogCategory)
    description = RichTextField()
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(default='images/default.png')
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.comment+" "+self.blog.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name