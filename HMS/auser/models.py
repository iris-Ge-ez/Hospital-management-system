from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """User model."""
    class Types(models.TextChoices):
        DOCTOR = 'DR', _('Doctor')
        NURSE = 'NU', _('Nurse')
        LABORATORIST = 'LAB', _('Laboratorist')
        RECEPTIONIST = 'RT', _('Receptionist')
        HOSPITAL_MANAGER = 'HM', _('Hospital Manager')
        DIRECTOR = 'DI', _('Director')
        PHARMACIST = 'PH', _('Pharmacist')
        HMS = 'HMS', _('HMS')
    username = models.CharField(max_length=255, unique=True, default='abs')
    base_type = 'HMS'
    type = models.CharField(_('Type'), choices=Types.choices, max_length=50)

    def get_absolute_url(self):
        return reverse('User', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = self.base_type
        super().save(*args, **kwargs)

class DoctorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Types.DOCTOR)
    
class NurseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Types.NURSE)

class LabManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Types.LABORATORIST)

class ReceptionistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Types.RECEPTIONIST)

class HospitalManagerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Types.HOSPITAL_MANAGER)

class DirectorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Types.DIRECTOR)

class PharmacistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Types.PHARMACIST)


class Doctor(User):
    doctor_objects = DoctorManager()
    base_type = User.Types.DOCTOR
    
    @property
    def more(self):
        return self.doctormore

    class Meta:
        proxy = True
    

class Nurse(User):
    base_type = User.Types.NURSE
    doctor_objects = NurseManager()
    
    @property
    def more(self):
        return self.nursemore
    

    class Meta:
        proxy = True

class Laboratorist(User):
    base_type = User.Types.LABORATORIST
    doctor_objects = LabManager()

    @property
    def more(self):
        return self.labmore

    class Meta:
        proxy = True



class Receptionist(User):
    base_type = User.Types.RECEPTIONIST
    doctor_objects = ReceptionistManager()

    @property
    def more(self):
        return self.receptionistmore

    class Meta:
        proxy = True


class HospitalManager(User):
    base_type = User.Types.HOSPITAL_MANAGER
    doctor_objects = HospitalManagerManager()

    @property
    def more(self):
        return self.hospitalmanagermore

    class Meta:
        proxy = True
        verbose_name = 'Hospital Manager'
    



class Director(User):
    base_type = User.Types.DIRECTOR
    doctor_objects = DirectorManager()

    @property
    def more(self):
        return self.directormore

    class Meta:
        proxy = True
    



class Pharmacist(User):
    base_type = User.Types.PHARMACIST
    doctor_objects = PharmacistManager()

    @property
    def more(self):
        return self.pharmacistmore

    class Meta:
        proxy = True

    
    

class DoctorMore(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta: 
        verbose_name = _('Doctor More')
        verbose_name_plural = _('Doctor\'s More')
        
    def __str__(self) -> str:
        return super().__str__()

class NurseMore(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Nurse More')
        verbose_name_plural = _('Nurse\'s More')
    def __str__(self) -> str:
        return super().__str__()

class LaboratoristMore(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Laboratorist More')
        verbose_name_plural = _('Laboratorist\'s More')

    def __str__(self) -> str:
        return super().__str__()

class ReceptionistMore(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Receptionist More')
        verbose_name_plural = _('Receptionist\'s More')

    def __str__(self) -> str:
        return super().__str__()
    

class HospitalManagerMore(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Hospital Manager More')
        verbose_name_plural = _('Hospital Manager\'s More')
    def __str__(self) -> str:
        return super().__str__()

class DirectorMore(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Director More')
        verbose_name_plural = _('Director\'s More')
    def __str__(self) -> str:
        return super().__str__()

class PharmacistMore(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Pharmacist More')
        verbose_name_plural = _('Pharmacist\'s More')
    def __str__(self) -> str:
        return super().__str__()
