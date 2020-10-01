from django.db import models

class PuppyModel(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_breed(self):
        return f'{self.name} belongs to {self.breed} breed.'
    
    def __repr__(self):
        return f'{self.name} id added'