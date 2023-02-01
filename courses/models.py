from django.db import models

# Create your models here.
class Courses(models.Model):

    Trainer=models.CharField(max_length=150)
    Course_Fee=models.FloatField(max_length=150)
    Available_Seats=models.IntegerField(max_length=50)
    Schedule=models.CharField(max_length=150)
    desc = models.TextField(max_length=400)

    def __str__(self):
        return self.Trainer



class Clasa(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length= 200, null=True)
    img = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg')




    def __str__(self):
        return self.title