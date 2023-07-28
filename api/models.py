from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, passward2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email,  name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class State(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    ts = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Area_Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    state = models.ManyToManyField(State)
    ts = models.TimeField(auto_now=True)
    def __str__(self):
        return ",".join([str(p) for p in self.state.all()])


class Destination(models.Model):
    name = models.CharField(max_length=50)
    area_cities = models.ForeignKey(Area_Cities, on_delete=models.CASCADE, related_name='area_cities')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state')
    id = models.IntegerField(primary_key=True)
    ts = models.TimeField(auto_now=True)
    def __str__(self):
        return self.name

class Pick_Up(models.Model):
    name = models.CharField(max_length=50)

class Drop(models.Model):
    name = models.CharField(max_length=50)

class Transfer(models.Model):
    cab_name = models.CharField(max_length=50)
    capacity = models.IntegerField()

class Activities(models.Model):
    name = models.CharField(max_length=50)
    durations = models.DurationField()
    description = models.CharField(max_length=200)

class Trip_Detail(models.Model):
    id = models.IntegerField(primary_key=True)
    heading =  models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    image = models.ImageField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='trip_detail_state')
    area_cities = models.ForeignKey(Area_Cities, on_delete=models.CASCADE, related_name='trip_detail_area_cities')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='trip_detail_destination')
    def __str__(self):
        return self.name

