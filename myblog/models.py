from django.db import models

# Create your models here.
class MyBlog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    # to show the name of blog an admin DB
    def __str__(self):

        return self.title


    def summary(self):
        return self.body[:100]

    #create custom date
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')