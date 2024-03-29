from django.shortcuts import render, redirect
from .models import Doctor, PatientTime
import datetime
from .doctor_model import Doctor, PatientTime
from django.http import HttpResponse
def generate_all_hours():
    all_hours = []
    start_time = datetime.datetime.strptime('09:00', '%H:%M')
    end_time = datetime.datetime.strptime('18:00', '%H:%M')
    current_time = start_time
    while current_time < end_time:
        all_hours.append(current_time.strftime('%H:%M'))
        current_time += datetime.timedelta(minutes=30)
    return all_hours



from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, PatientTime

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})
def doctor_schedule(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    patient_times = PatientTime.objects.filter(doctor=doctor).values_list('time', flat=True)
    all_hours = generate_all_hours()  # Assuming this function generates all possible time slots
    booked_times = list(patient_times)
    return render(request, 'doctor_schedule.html', {'doctor': doctor, 'all_hours': all_hours, 'booked_times': booked_times})




def book_appointment(request, doctor_id, time):
    # Retrieve the doctor object
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    # Check if the time slot is available
    if doctor.patient_times.filter(time=time).exists():
        # Time slot is already booked
        return HttpResponse("The selected time slot is not available")
    else:
        # Time slot is available, so book the appointment
        appointment_time = PatientTime.objects.create(time=time)
        doctor.patient_times.add(appointment_time)  # Associate the appointment time with the doctor
        doctor.save()  # Save the doctor object to persist the changes
        return redirect('doctor_list') 