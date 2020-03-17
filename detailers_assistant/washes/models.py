from django.db import models

# Create your models here.
class Wash(models.Model):
    """Model representing a wash"""
    name = models.CharField(max_length=200,
                            help_text="Enter a name for the wash")
    description = models.TextField(help_text="Enter a description")

    steps = models.ForeignKey('Steps', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for represting the Model object"""
        return self.name

class Steps(models.Model):
    """Model represeting a single step in a wash"""
    name = models.CharField(
            max_length=100,
            help_text="Short, friendly, display name for the step")
    description = models.TextField(
                    help_text="Description of the step")
