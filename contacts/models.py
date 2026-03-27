from django.db import models

STATUS_CHOICES = [
    ('P', 'Pending'),
    ('W', 'In Progress'),
    ('F', 'Finished'),
]

class ContactMessage(models.Model):
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')