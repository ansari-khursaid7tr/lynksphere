from django.db import models

class PageContent(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    about_us = models.TextField()
    about_us2 = models.TextField(blank=True, default="")
    about_us3 = models.TextField(blank=True, default="")
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    contact_address = models.CharField(max_length=255)
    contact_header_text = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    features = models.TextField()  # Store features as comma-separated list

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

