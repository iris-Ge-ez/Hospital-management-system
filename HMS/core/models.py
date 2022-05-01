from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Laboratory(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    madein = models.CharField(max_length=100)
    production_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class DoctorDiseaseDiagnosis(models.Model):
    """
    This class is used to track disease diagnosis of a patient.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    disease = models.ForeignKey('Disease', on_delete=models.CASCADE)
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class DoctorPrescribeMedicine(models.Model):
    """
    This class is used to track medicine prescription of a patient.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class ReferToHospital(models.Model):
    """
    This class is used to track hospital referral of a patient.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class PatientAppointment(models.Model):
    """
    This class is used to track patient appointment.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class PatientNurseVitalTracking(models.Model):
    """
    This class is used to track vital signs of a patient.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    nurse = models.ForeignKey('Nurse', on_delete=models.CASCADE)
    bp_systolic = models.IntegerField()
    bp_diastolic = models.IntegerField()
    heart_rate = models.IntegerField()
    temperature = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()
    blood_glucose = models.IntegerField()
    blood_oxygen = models.FloatField()
    respiratory_rate = models.IntegerField()
    bmi = models.FloatField()
    bmi_category = models.CharField(max_length=10)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class LaboratoryResults(models.Model):
    """
    This class is used to track laboratory results of a patient.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    laboratory_technician = models.ForeignKey('LaboratoryTechnician', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    laboratory = models.ForeignKey('Laboratory', on_delete=models.CASCADE)
    results = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class HospitalAdmissionCard(models.Model):
    """
    This class is used to track hospital admission card of a patient.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    receptionist = models.ForeignKey('Receptionist', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class HospitalBed(models.Model):
    """
    This class is used to track hospital bed of a patient.
    """
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    bed_number = models.IntegerField()
    receptionist = models.ForeignKey('Receptionist', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Report(models.Model):
    """
    This class is used to track report of a patient.
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) 


