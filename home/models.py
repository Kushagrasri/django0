from django.db import models

# Create your models here.
# makemigrations matlab create changes and store in a file
# migrate matlab apply pending changes created by make migrations
# migrate matlab write changes into database

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + self.phone