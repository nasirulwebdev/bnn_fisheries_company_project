from django.db import models


class Publication(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="শিরোনাম"
    )
    author = models.CharField(
        max_length=150,
        verbose_name="লেখক/প্রকাশক"
    )
    description = models.TextField(
        verbose_name="সংক্ষিপ্ত বিবরণ"
    )
    file = models.FileField(
        upload_to='publications/',
        blank=True,
        null=True,
        verbose_name="ফাইল (PDF, DOC, ইত্যাদি)"
    )
    publication_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="প্রকাশের তারিখ"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="প্রকাশিত"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ['-publication_date', '-created_at']

    def __str__(self):
        return self.title
