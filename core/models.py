from django.db import models
from django.shortcuts import reverse

class AidRecord(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200, unique=True)
    whatsapp = models.CharField(max_length=200)
    residents = models.CharField(max_length=200)
    rooms = models.CharField(max_length=200)
    room1 = models.ImageField(upload_to='images')
    room2 = models.ImageField(upload_to='images')
    room3 = models.ImageField(upload_to='images')
    livingrooms = models.CharField(max_length=200)
    livingroom1 = models.ImageField(upload_to='images')
    livingroom2 = models.ImageField(upload_to='images')
    kitchen = models.ImageField(upload_to='images')
    national_id = models.ImageField(upload_to='images', blank=True, null=True)
    occupation = models.CharField(max_length=200)
    income = models.CharField(max_length=200)
    age = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('aid_record_detail', kwargs={'id': self.id})




class Offer(models.Model):
    aid = models.ForeignKey(AidRecord, related_name='offers', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    description = models.TextField()