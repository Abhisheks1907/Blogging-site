
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile





class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('post-detail',kwargs={'pk':self.pk})

    


class user_Profile(models.Model):

    # user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg',upload_to='pics')
    about = models.TextField(default=' ')
    

    def __str__(self):
        return f'{self.user} user_Profile'
    
