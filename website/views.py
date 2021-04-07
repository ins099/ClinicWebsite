from website.forms import AppointmentForm
from DentalClinic.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings as conf_settings

def home(request):
    return render(request, 'website/home.html', {
        'form':AppointmentForm()
    })

def about(request):
    return render(request, 'website/about.html')
        
def service(request):
    return render(request, 'website/service.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        
        #send email to default address
        send_mail(
            'Follow up required for - ' + name,
            message + f"\n \n Contact Email: {email}",
            email,
            [EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, f'Hi {name}, Thanks for contacting us. We will follow up with you within next few business days.')
        return redirect('contact')
    else:
        return render(request, 'website/contact.html')

def bookingAppointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        print(request.POST['email'])
        if form.is_valid():
            form.save()


            subject = "Dental Appointment Confirmation"
            message = f"Hi! {request.POST['patient_name']} This email is to inform you that your appointment at our Clinic has been confirmed. \n Kindly visit the clinic within the mentioned time. \n Thanks!"
            recipent = request.POST['email']

            send_mail(
                subject,message,EMAIL_HOST_USER, [recipent], fail_silently=True    
            )


            messages.success(request, f'Hi, Thanks for booking your appointment we will get connected to you shortly.')
            return redirect('home')