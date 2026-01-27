from django.db import models


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('seminar', 'সেমিনার'),
        ('workshop', 'ওয়ার্কশপ'),
        ('training', 'প্রশিক্ষণ'),
        ('conference', 'কনফারেন্স'),
        ('other', 'অন্যান্য'),
    )

    title = models.CharField(
        max_length=200,
        verbose_name="ইভেন্টের নাম"
    )
    short_description = models.CharField(
        max_length=300,
        verbose_name="সংক্ষিপ্ত বিবরণ"
    )
    description = models.TextField(
        verbose_name="বিস্তারিত বিবরণ"
    )
    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True,
        verbose_name="ইভেন্টের ছবি"
    )
    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPE_CHOICES,
        default='other',
        verbose_name="ইভেন্টের ধরন"
    )
    event_date = models.DateField(
        verbose_name="ইভেন্টের তারিখ"
    )
    event_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name="ইভেন্টের সময়"
    )
    location = models.CharField(
        max_length=200,
        verbose_name="স্থান"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="প্রকাশিত"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-event_date']

    def __str__(self):
        return self.title
