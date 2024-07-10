from django.db import models
from .user_model import User


class Poll(models.Model):
    CATEGORY_CHOICES = [
        ('ENTERTAINMENT', 'Entretenimento'),
        ('TECHNOLOGY', 'Tecnologia'),
        ('SPORTS', 'Esportes'),
        ('FOOD', 'Alimentação'),
        ('TRAVEL', 'Viagens'),
        ('CULTURE_ART', 'Cultura e Arte'),
        ('POLITICS_SOCIAL', 'Política e Sociedade'),
        ('SCIENCE_EDUCATION', 'Ciência e Educação'),
        ('FASHION_BEAUTY', 'Moda e Beleza'),
        ('OTHER', 'Outros')
    ]

    criation_date = models.DateField()
    finish_date = models.DateField()
    status = models.CharField(max_length=255, choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('BANNED', 'Banned'), ('ARCHIVED', 'Archived')])
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    privacy = models.CharField(max_length=255, choices=[('PUBLIC', 'Public'), ('HIDDEN', 'Hidden'), ('RESTRICTED', 'Restricted')])
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='OTHER')

    @property
    def questions(self):
        return self.questionfield_set.all()

    def __str__(self):
        return self.title