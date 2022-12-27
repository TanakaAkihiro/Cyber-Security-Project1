from django.db import models


class User(models.Model):
    username = models.TextField()
    password = models.TextField()

    def __str__(self) -> str:
        return self.username

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    iban = models.TextField()
    
    def __str__(self):
        return self.iban
