from django.db import models

# Create your models here.

class Appointment(models.Model):

    TIME_CHOICES = (
    ("9AM to 10AM", "9AM to 10AM"),
    ("11am to 12pm", "11am to 12pm"),
    ("1pm to 2pm", "1pm to 2pm"),
    ("4pm to 5pm", "4pm to 5pm"),
    ("6pm to 7pm", "6pm to 7pm"),
    ("7pm to 8pm", "7pm to 8pm"),
                    )

    time = models.CharField(max_length=15,
                  choices=TIME_CHOICES,
                  default="Choose Your Schedule")
    patient_name = models.CharField(max_length= 100, null = False, blank=False)
    phone_no = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    message = models.TextField()