from django.db import models


# Create your models here.

class Todaysspecial(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name


class starters(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Maindishes(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Deserts(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Drinks(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return '{}'.format(self.name)


class Restaurant(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Restaurant', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return '{}'.format(self.name)


class restaurantfooderna(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dishes', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'rester'
        verbose_name_plural = 'resterna'

    def __str__(self):
        return '{}'.format(self.name)


class restaurantfoodthris(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dishes', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'restthri'
        verbose_name_plural = 'restthris'

    def __str__(self):
        return '{}'.format(self.name)


class restaurantfoodtrivan(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dishes', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'resttri'
        verbose_name_plural = 'resttriva'

    def __str__(self):
        return '{}'.format(self.name)


class booking(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    quantity = models.TextField()
    phone = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
