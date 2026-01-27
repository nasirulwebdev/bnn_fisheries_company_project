from django.db import models


class Project(models.Model):
    STATUS_CHOICES = (
        ('ongoing', 'চলমান'),
        ('completed', 'সম্পন্ন'),
        ('upcoming', 'আসন্ন'),
    )

    title = models.CharField(
        max_length=200,
        verbose_name="প্রকল্পের নাম"
    )
    short_description = models.CharField(
        max_length=300,
        verbose_name="সংক্ষিপ্ত বিবরণ"
    )
    description = models.TextField(
        verbose_name="বিস্তারিত বিবরণ"
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        verbose_name="প্রকল্পের ছবি"
    )
    video = models.FileField(
        upload_to='projects/videos/',
        blank=True,
        null=True,
        verbose_name="প্রকল্পের ভিডিও"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ongoing',
        verbose_name="প্রকল্পের অবস্থা"
    )
    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="শুরুর তারিখ"
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="শেষ তারিখ"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="প্রকাশিত"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
