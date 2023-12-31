from django.contrib.auth.base_user import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, eamil ,password=None, password2=None):   
        if not eamil:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=eamil
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email ,password=None):
        user = self.create_user(
            email,
            password = password ,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user