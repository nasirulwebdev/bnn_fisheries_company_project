from django.db import models

# Create your models here.
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="নাম"
    )
    email = models.EmailField(
        verbose_name="ইমেইল"
    )
    subject = models.CharField(
        max_length=200,
        verbose_name="বিষয়"
    )
    message = models.TextField(
        verbose_name="বার্তা"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="পঠিত হয়েছে"
    )

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
