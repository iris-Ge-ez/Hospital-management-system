from django.contrib import admin
from core.models import (Hospital, Laboratory, Patient, Disease, Medicine, DoctorDiseaseDiagnosis, DoctorPrescribeMedicine, 
                        ReferToHospital, PatientAppointment, PatientNurseVitalTracking, LaboratoryResults, HospitalAdmissionCard, HospitalBed, Report)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('name', 'address', 'city', 'state', 'phone', 'email', 'zipcode')
    search_fields = ('name', 'city', 'state')
    
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'hospital')
    list_filter = ('name', 'hospital', 'address', 'city', 'state', 'phone', 'email', 'zipcode')
    search_fields = ('name', 'city', 'state')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_filter = ('name', 'age', 'created_at', 'updated_at')
    search_fields = ('name', 'age', 'created_at', 'updated_at')

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_filter = ('name', 'description')
    search_fields = ('name')

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'madein')
    list_filter = ('name', 'description', 'producer', 'brand', 'madein', 'production_date', 'expiry_date')
    search_fields = ('name', 'description', 'brand', 'madein')

class DoctorDiseaseDiagnosisAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'disease')
    list_filter = ('patient', 'doctor', 'disease', 'diagnosis', 'created_at', 'updated_at')
    search_fields = ('patient', 'doctor', 'disease',  'created_at')

class DoctorPrescribeMedicineAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'medicine')
    list_filter = ('patient', 'doctor', 'medicine', 'dosage', 'duration', 'created_at', 'updated_at')
    search_fields = ('patient', 'doctor', 'medicine', 'created_at')

class ReferToHospitalAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'hospital')
    list_filter = ('patient', 'doctor', 'hospital', 'reason', 'created_at', 'updated_at')
    search_fields = ('patient', 'doctor', 'hospital', 'created_at')

class PatientAppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor')
    list_filter = ('patient', 'doctor', 'date', 'time', 'created_at', 'updated_at')
    search_fields = ('patient', 'doctor', 'date', 'time', 'created_at')

class PatientNurseVitalTrackingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'nurse')
    list_filter = ('patient', 'nurse', 'bp_systolic', 'bp_diastolic', 'heart_rate', 'temperature', 'weight', 'height', 'blood_glucose', 'blood_oxygen', 'respiratory_rate', 'bmi', 'bmi_category', 'notes', 'created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('patient', 'nurse', 'created_at')

class LaboratoryResultsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'laboratory')
    list_filter = ('patient', 'laboratory', 'result', 'laboratory_technician', 'date', 'time', 'created_at', 'updated_at')
    search_fields = ('patient', 'laboratory', 'date', 'time', 'created_at')

class HospitalAdmissionCardAdmin(admin.ModelAdmin):
    list_display = ('patient', 'hospital')
    list_filter = ('patient', 'hospital', 'receptionist', 'created_at', 'updated_at')
    search_fields = ('patient', 'hospital', 'receptionist', 'created_at')

class HospitalBedAdmin(admin.ModelAdmin):
    list_display = ('patient', 'hospital', 'bed_number', 'receptionist')
    list_filter = ('patient', 'hospital', 'bed_number', 'receptionist', 'created_at', 'updated_at')
    search_fields = ('name', 'hospital', 'created_at')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('user')
    list_filter = ('user', 'report', 'created_at', 'updated_at')
    search_fields = ('user', 'laboratory', 'created_at')


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(DoctorDiseaseDiagnosis, DoctorDiseaseDiagnosisAdmin)
admin.site.register(DoctorPrescribeMedicine, DoctorPrescribeMedicineAdmin)
admin.site.register(ReferToHospital, ReferToHospitalAdmin)
admin.site.register(PatientAppointment, PatientAppointmentAdmin)
admin.site.register(PatientNurseVitalTracking, PatientNurseVitalTrackingAdmin)
admin.site.register(LaboratoryResults, LaboratoryResultsAdmin)
admin.site.register(HospitalAdmissionCard, HospitalAdmissionCardAdmin)
admin.site.register(HospitalBed, HospitalBedAdmin)
admin.site.register(Report, ReportAdmin)
