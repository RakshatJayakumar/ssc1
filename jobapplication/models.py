from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('AP', 'Applied'),
        ('IN', 'Interviewing'),
        ('OF', 'Offer Received'),
        ('AC', 'Accepted'),
        ('RE', 'Rejected'),
    ]
    
    REFERRAL_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]

    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    referral = models.CharField(max_length=3, choices=REFERRAL_CHOICES)
    people = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"
