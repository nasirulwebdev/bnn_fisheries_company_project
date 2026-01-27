from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200, help_text="Banner এর শিরোনাম লিখুন")
    description = models.TextField(help_text="Banner এর বিবরণ লিখুন")
    image = models.ImageField(upload_to='banners/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class যেমন: fa-solid fa-fish")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
