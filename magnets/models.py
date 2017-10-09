from django.db import models

# Create your models here.
class SpeciesType(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    
    def __str__(self):
        return self.name
    
    
class Attributes(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    
    def __str__(self):
        return self.name
    
    
class SpeciesAttributes(models.Model):
    species = models.ForeignKey(SpeciesType, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    
    
class SpeciesInstance(models.Model):
    type = models.ForeignKey(SpeciesType, on_delete=models.CASCADE)
    xPosition = models.FloatField(default=0.0)
    yPosition = models.FloatField(default=0.0)
    
    class Meta:
        unique_together = ('xPosition', 'yPosition')
        
    def __str__(self):
        return str.format(
            "{} at {},{}", self.type, str(self.xPosition), str(self.yPosition))
    
    
class Bonds(models.Model):
    species1 = models.ForeignKey(
        SpeciesInstance, on_delete=models.CASCADE, related_name='species1')
    species2 = models.ForeignKey(
        SpeciesInstance, on_delete=models.CASCADE, related_name='species2')
    
    class Meta:
        unique_together = ('species1', 'species2')