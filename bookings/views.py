from django.shortcuts import render, redirect
from .models import Service, Booking
from .forms import BookingForm

def home(request):
    return render(request, 'home.html')

def book(request):
    services = Service.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('confirmation', booking.id)  # Redirect to confirmation page
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form, 'services': services})

def confirmation(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'confirmation.html', {'booking': booking})

def book_appointment(request):
    form = BookingForm()
    return render(request, 'book_appointment.html', {'form': form})

service = Service(name="Haircut", price=25.00)
service.save()  # Save the service (id will be assigned automatically)

booking = Booking(service=service, date='2024-01-15', time='10:00', name="John Doe", email="john@example.com", phone="1234567890")
booking.save() # save the booking (id will be assigned automatically)