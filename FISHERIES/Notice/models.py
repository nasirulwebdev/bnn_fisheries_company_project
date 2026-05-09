from django.db import models
from django.utils import timezone


class Notice(models.Model):
    PRIORITY_CHOICES = (
        ('Normal', 'Normal'),
        ('Important', 'Important'),
        ('Urgent', 'Urgent'),
    )

    title = models.CharField(max_length=250)
    description = models.TextField()
    file = models.FileField(upload_to='notice_files/', blank=True, null=True)
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Normal'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title