# tasks/models.py
from django.db import models
import datetime

class Task(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('overdue', 'Overdue'),
        ('due_today', 'Due Today'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        today = datetime.date.today()

        # If the task is being created, automatically set the status based on due_date
        if not self.id:
            if self.due_date < today:
                self.status = 'Overdue'
            elif self.due_date == today:
                self.status = 'Due Today'
            else:
                self.status = 'Upcoming'
        else:
            # If the task is being updated, check if the due_date has changed
            original_task = Task.objects.get(id=self.id)
            if self.due_date != original_task.due_date:
                if self.due_date < today:
                    self.status = 'Overdue'
                elif self.due_date == today:
                    self.status = 'Due today'
                else:
                    self.status = 'Upcoming'
        
        # Save the task with updated status
        super().save(*args, **kwargs)
