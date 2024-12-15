from django.db import models


class About(models.Model):
    full_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')
    image3 = models.ImageField(upload_to='about/')
    # image4 = models.ImageField(upload_to='about/')
    # image5 = models.ImageField(upload_to='about/')
    description = models.TextField()
    telegram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Section(models.Model):
    title = models.CharField(max_length=200)
    numbers = models.IntegerField()

    def __str__(self):
        return self.title