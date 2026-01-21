from django.db import models

class Bar_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/bar/')    
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name

class Salad_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/salad/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name

class Additionaldishes_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/additionaldishes/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )    
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name
    
class Burger_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/burger/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )    
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name
    
class Pizza_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/pizza/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name

class Bread_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/bread/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name

class Sup_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/sup/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name

class Fish_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/fish/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name

class BBQ_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/bbq/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name
    
class National_dishes_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/national/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name
    
class Kebab_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/kebab/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name
    
class Sweets_menu(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Tugagan', 'Tugagan'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
    ]
    image = models.ImageField(upload_to='media/menu/sweets/')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'  
    )
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.name


class Comments(models.Model):
    comment = models.TextField()
    image = models.ImageField(upload_to='media/comments/', blank=True)
    name = models.CharField(max_length=100)
    instagram_handle = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Parties(models. Model):
    image = models.ImageField(upload_to='media/parties/')
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name

class Chefs(models.Model):
    image = models.ImageField(upload_to='media/chefs/')
    name = models.CharField(max_length=100)
    facebook = models.URLField(blank=True)
    instagramm = models.URLField(blank=True)
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name