from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    cat_num = models.IntegerField(default = 0)


    class Meta:
        verbose_name_plural = 'People'
        
    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Cat(models.Model):
    cat_name = models.CharField(max_length=35)
    owners = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat_name
    
