from django.db import models



class Company(models.Model):
    name = models.CharField(max_length = 200)
    creation_time = models.DateTimeField()


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length = 100)
    creation_time = models.DateTimeField()


    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length = 300)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    rating = models.FloatField()
    creation_time = models.DateTimeField()


    def __str__(self):
        return self.name
    


class Review(models.Model):
    author = models.CharField(max_length = 200)
    author_ip = models.CharField(max_length = 32)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    text = models.TextField()
    rating = models.FloatField()
    creation_time = models.DateTimeField()


    def __str__(self):
        return self.author + ': ' + self.text[:20] 

