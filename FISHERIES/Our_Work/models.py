from django.db import models


class OurWork(models.Model):
    author_name = models.CharField(
        max_length=100,
        verbose_name="লেখকের নাম"
    )
    position = models.CharField(
        max_length=100,
        verbose_name="পদবী/পদ"
    )
    message = models.TextField(
        verbose_name="বার্তা/বক্তব্য"
    )
    image = models.ImageField(
        upload_to='our_work/',
        blank=True,
        null=True,
        verbose_name="লেখকের ছবি"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="প্রকাশিত"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Our Work"
        verbose_name_plural = "Our Works"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author_name} - {self.position}"
