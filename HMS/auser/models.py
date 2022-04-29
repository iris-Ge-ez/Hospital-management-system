from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Profile(AbstractUser):
    
    class Types(models.TextChoices):
        DOCTOR = 'DR', _('Doctor')
        NURSE = 'NU', _('Nurse')
        SPECIALIST = 'SP', _('Specialist')
        PATIENT = 'PA', _('Patient')
        LABORATORIST = 'LAB', _('LaboratorIST')
        RECEPTIONIST = 'RT', _('Receptionist')
        ADMIN = 'AD', _('Admin')
        DIRECTOR = 'DI', _('Director')
        PHARMACIST = 'PH', _('Pharmacist')
    base_type = Types.PATIENT
    type = models.CharField(_('Type'), choices=Types.choices, max_length=50)
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.username})
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        super().save(*args, **kwargs)

class DoctorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.DOCTOR)
    
class NurseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.NURSE)

class SpecialistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.SPECIALIST)    

class PatientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.PATIENT)

class LabManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.LABORATORIST)

class ReceptionistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.RECEPTIONIST)

class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.ADMIN)

class DirectorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.DIRECTOR)

class PharmacistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Profile.Types.PHARMACIST)


class Doctor(Profile):
    objects = DoctorManager()

    @property
    def more(self):
        return self.doctormore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.DOCTOR
        super().save(*args, **kwargs)

class Nurse(Profile):
    objects = NurseManager()

    @property
    def more(self):
        return self.nursemore
    

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.NURSE
        super().save(*args, **kwargs)

class Specialist(Profile):
    objects = SpecialistManager()

    @property
    def more(self):
        return self.specialistmore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.SPECIALIST
        super().save(*args, **kwargs)


class Patient(Profile):
    objects = PatientManager()

    @property
    def more(self):
        return self.patientmore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.PATIENT
        super().save(*args, **kwargs)


class Laboratorist(Profile):
    objects = LabManager()

    @property
    def more(self):
        return self.labmore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.LABORATORIST
        super().save(*args, **kwargs)


class Receptionist(Profile):
    objects = ReceptionistManager()

    @property
    def more(self):
        return self.receptionistmore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.RECEPTIONIST
        super().save(*args, **kwargs)


class Admin(Profile):
    objects = AdminManager()

    @property
    def more(self):
        return self.adminmore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.ADMIN
        super().save(*args, **kwargs)


class Director(Profile):
    objects = DirectorManager()

    @property
    def more(self):
        return self.directormore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.DIRECTOR
        super().save(*args, **kwargs)


class Pharmacist(Profile):
    objects = PharmacistManager()

    @property
    def more(self):
        return self.pharmacistmore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.PHARMACIST
        super().save(*args, **kwargs)

class DoctorMore(models.Model):
    profile = models.OneToOneField(Doctor, on_delete=models.CASCADE, primary_key=True)

    class Meta: 
        verbose_name = _('Doctor More')
        verbose_name_plural = _('Doctor\'s More')

class NurseMore(models.Model):
    profile = models.OneToOneField(Nurse, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Nurse More')
        verbose_name_plural = _('Nurse\'s More')

class SpecialistMore(models.Model):
    profile = models.OneToOneField(Specialist, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Specialist More')
        verbose_name_plural = _('Specialist\'s More')

class PatientMore(models.Model):
    profile = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Patient More')
        verbose_name_plural = _('Patient\'s More')

class LaboratoristMore(models.Model):
    profile = models.OneToOneField(Laboratorist, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Laboratorist More')
        verbose_name_plural = _('Laboratorist\'s More')

class ReceptionistMore(models.Model):
    profile = models.OneToOneField(Receptionist, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Receptionist More')
        verbose_name_plural = _('Receptionist\'s More')

class AdminMore(models.Model):
    profile = models.OneToOneField(Admin, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Admin More')
        verbose_name_plural = _('Admin\'s More')

class DirectorMore(models.Model):
    profile = models.OneToOneField(Director, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Director More')
        verbose_name_plural = _('Director\'s More')

class PharmacistMore(models.Model):
    profile = models.OneToOneField(Pharmacist, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('Pharmacist More')
        verbose_name_plural = _('Pharmacist\'s More')

