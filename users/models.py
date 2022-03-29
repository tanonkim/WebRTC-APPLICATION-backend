from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db                  import models

class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, first_name, last_name, password):        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email      = self.normalize_email(email),            
            first_name = first_name,
            last_name  = last_name        
        ) 
        user.set_password(password)
        return user     

class User(AbstractBaseUser):
    objects = UserManager()

    email      = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=25)
    last_name  = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    USERNAME_FIELD  = 'email'

    class Meta:
        db_table='users'