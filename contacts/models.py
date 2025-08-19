from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    first_name = models.CharField("Ism", max_length=50)
    last_name = models.CharField("Familiya", max_length=50)
    phone = models.CharField("Telefon raqami", max_length=20)
    email = models.EmailField("Email manzil")
    message = models.TextField("Yuborilgan xabar")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    