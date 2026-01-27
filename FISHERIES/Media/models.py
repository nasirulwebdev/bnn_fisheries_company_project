from django.db import models


class Media(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'ছবি'),
        ('video', 'ভিডিও'),
        ('news', 'সংবাদ'),
    )

    title = models.CharField(
        max_length=200,
        verbose_name="শিরোনাম"
    )
    short_description = models.CharField(
        max_length=300,
        verbose_name="সংক্ষিপ্ত বিবরণ"
    )
    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPE_CHOICES,
        verbose_name="মিডিয়ার ধরন"
    )
    image = models.ImageField(
        upload_to='media/images/',
        blank=True,
        null=True,
        verbose_name="ছবি"
    )
    video_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="ভিডিও লিংক (YouTube/Facebook/Instagram)"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="প্রকাশিত"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
