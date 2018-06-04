from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    (1, 'Open'),
    (2, 'Resolved'),
    (3, 'Closed'),
)

PRIORITY_CHOICES = (
    (1, 'Critical'),
    (2, 'High'),
    (3, 'Low'),
)

# category
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural= 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

# issue
class Issue(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    submitted_date = models.DateField(auto_now_add=True)
    submitter = models.ForeignKey(User, related_name="submitter", on_delete=models.PROTECT)
    solver = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=1, choices=PRIORITY_CHOICES)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'issue'
        verbose_name_plural = 'issues'
        ordering = ('status', 'submitted_date', 'title')

    def __str__(self):
        return self.title
