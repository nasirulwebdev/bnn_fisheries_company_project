from django.db import models


class AboutPage(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="শিরোনাম"
    )
    short_description = models.CharField(
        max_length=300,
        verbose_name="সংক্ষিপ্ত বিবরণ"
    )
    description = models.TextField(
        verbose_name="বিস্তারিত বিবরণ"
    )
    image = models.ImageField(
        upload_to='about/',
        blank=True,
        null=True,
        verbose_name="ছবি"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="সক্রিয়"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
