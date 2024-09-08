from django.db import models

# Create your models her
class Employee(models.Model):
    first_name=models.CharField(max_length=100);
    last_name=models.CharField(max_length=100);
    Photo=models.ImageField(upload_to='images');
    designation=models.CharField(max_length=100);
    email_address=models.CharField(max_length=100);
    Phone_Number=models.CharField(max_length=10);
    

    def __str__(self):
        return self.first_name