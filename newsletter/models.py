from django.db import models


class NewsLetterUser(models.Model):
    email = models.EmailField(null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=150)
    body = models.TextField(null=True, blank=True)
    email = models.ManyToManyField(NewsLetterUser)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=EMAIL_STATUS_CHOICES)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


