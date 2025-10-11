from django.db import models
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length = 250)    
    option_a = models.CharField(max_length = 250)    
    option_b = models.CharField(max_length = 250)    
    option_c = models.CharField(max_length = 250)    
    option_d = models.CharField(max_length = 250)
    correct_option = models.CharField(max_length = 250)

    def __str__(self):
        return self.title()
