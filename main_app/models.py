from django.db import models
from django.urls import reverse
from datetime import date

BODIES = (
    ('C', 'Carolina'),
    ('B', 'Blaine'),
    ('A', 'Amy'),
    ('S', 'Shaw'),
    ('M', 'Marco'),
    ('N', 'Morgan'),
    ('H', 'Chris')
)

class Sin(models.Model):
  name = models.CharField(max_length=50)
  level = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sins_detail', kwargs={'pk': self.id})

# Create your models here.
class Demon(models.Model):
    name = models.CharField(max_length=250)
    classification = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    age = models.CharField(max_length=20)
    sins = models.ManyToManyField(Sin)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'demon_id': self.id})

    def fed_for_today(self):
        return self.soul_set.filter(date=date.today()).count() >= len(BODIES)

class Soul(models.Model):
    date = models.DateField('Snack date')
    body = models.CharField(
        max_length=1,
        choices=BODIES,
        default=BODIES[0][0]
    )
    demon = models.ForeignKey(Demon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_body_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    demon = models.ForeignKey(Demon, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for demon_id: {self.demon_id} @{self.url}"