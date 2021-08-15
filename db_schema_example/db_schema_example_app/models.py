from django.db import models

# Create your models here.
class User(models.Model):

   firstname = models.CharField(max_length=50)
   lastname = models.CharField(max_length=50)
   username = models.CharField(unique=True, max_length=50)


   class Meta:
      db_table = "user"

class EmailAddress(models.Model):
    address = models.CharField(max_length = 50)
    user = models.ForeignKey(
       'User', 
       null=True, 
       on_delete=models.SET_NULL,
       max_length=64)

    class Meta:
      db_table = "emailAddress"
