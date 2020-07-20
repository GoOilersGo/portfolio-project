from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    body=models.TextField()
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# Create a blog models
#Needs a AuthenticationMiddleware
#pub_date
#body
#Image


#Add the Blog app to the settings
#Create a migration
#Do a migrate
#Add to the admin
