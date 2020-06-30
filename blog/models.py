from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    body=models.TextField(max_length=200)
    pub_date=models.DateTimeField()


# Create a blog models
#Needs a AuthenticationMiddleware
#pub_date
#body
#Image


#Add the Blog app to the settings
#Create a migration
#Do a migrate
#Add to the admin
