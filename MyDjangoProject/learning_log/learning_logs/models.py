from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/5.1/
# https://docs.djangoproject.com/en/4.1/topics/db/queries
# https://docs.djangoproject.com/en/4.1/ref/templates. 
# https://docs.djangoproject.com/en/4.1/topics/db/forms/
class Topic(models.Model):
    """""A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return self.text
        else:
          return f"{self.text[:50]}..."
