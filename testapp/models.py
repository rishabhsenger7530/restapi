from django.db import models

# Create your models here.



class TestModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    phone = models.PositiveBigIntegerField()
    is_alve = models.BooleanField(default=True)
    extra_name = models.CharField(max_length=250)
    amount  = models.FloatField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    # def save(self):
    #     return f"{self.extra_name} = {self.name} {self.phone}" 