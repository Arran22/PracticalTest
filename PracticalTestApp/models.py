from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    cat_num = models.IntegerField(default = 0)

    def __string__(self):
        return first_name + " " + last_name
    

class Cats(models.Model):
    cat_name = models.CharField(max_length=35)

    def __string__(self):
        return self.cat_name