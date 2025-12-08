import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from membership.models import Membership
from dateutil.relativedelta import relativedelta


# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('no especificaste email valido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', 'user')  # ← AGREGADO
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')  # ← AGREGADO
        return self._create_user(email, password, **extra_fields)
    
    def create_recepcionist(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', 'receptionist')  # ← AGREGADO
        return self._create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    # ← NUEVO: Definir las opciones de roles
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('receptionist', 'Recepcionista'),
        ('user', 'Usuario'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    
    # ← NUEVO: Campo de rol
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
    # avatar= models.ImageField(upload_to='uploads/avatars')
    membership = models.ForeignKey(Membership, related_name='membership', on_delete=models.CASCADE, null=True, blank=True)
    date_pay = models.DateTimeField(null=True, blank=True)
    date_expiration = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.is_staff = True
            self.is_superuser = True
            self.is_active = True
        elif self.role == 'receptionist':
            self.is_staff = True
            self.is_superuser = False
            self.is_active = True
        else:  
            self.is_staff = False
            self.is_superuser = False
        
        # Calcular fecha de expiración
        if self.role == 'user' and self.membership:
            if not self.date_expiration and self.date_pay:
                duration = self.membership.duration_membership
                if duration == "mensual":
                    self.date_expiration = self.date_pay + relativedelta(months=1)
                elif duration == "anual":
                        self.date_expiration = self.date_pay + relativedelta(years=1)
        
        super().save(*args, **kwargs)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def avatar_url(self):   
        if self.avatar:
            return f'{settings.WEBSITE_URL}{self.avatar.url}'
        else:
            return ''
    
    
    def get_role_display_es(self):
        role_map = {
            'admin': 'Administrador',
            'receptionist': 'Recepcionista',
            'user': 'Usuario'
        }
        return role_map.get(self.role, 'Usuario')