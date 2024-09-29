from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission

STATUS_DOCS = [
    ('active', 'Действует'),
    ('deleted', 'Удалено'),
    ('trash', 'В корзине')
]

STATUS_APPS = [
    ('created', 'Создан'),
    ('in_progress', 'В работе'),
    ('completed', 'Завершен'),
    ('canceled', 'Отменен'),
    ('deleted', 'Удален'),
]

class Activities(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'activities'
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name
    
    
class Filial(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=12)

    class Meta:
        db_table = 'filials'
        verbose_name_plural = "Filials"

    def __str__(self):
        return self.name
    
    
class NewUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email адрес", unique=True)
    password = models.CharField(max_length=150, verbose_name="Пароль")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    otchestvo = models.CharField(max_length=150, verbose_name="Отчество")
    is_staff = models.BooleanField(default=False, verbose_name="Является ли пользователь тренером?")
    is_superuser = models.BooleanField(default=False, verbose_name="Является ли пользователь админом?")
    is_active = models.BooleanField(default=True, verbose_name="Активен ли пользователь?")
    groups = models.ManyToManyField(Group, verbose_name="Группы", blank=True, related_name="customuser_groups")
    USERNAME_FIELD = 'email'
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name='coaches', null=True)
    user_permissions = models.ManyToManyField(Permission, verbose_name="Права доступа", blank=True, related_name="customuser_user_permissions")

    objects = NewUserManager()

    class Meta:
        db_table = 'users'

class Schedule(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name='schedules')
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'schedule'
        verbose_name_plural = "Schedule"

    def __str__(self):
        return f"{self.activity} {self.date} {self.start_time}"





class Record(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='client_records')
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'records'
        verbose_name_plural = "Records"




