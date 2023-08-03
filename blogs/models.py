from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'
    
    def __str__(self) :
        return self.title