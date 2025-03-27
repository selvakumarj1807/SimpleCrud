from django.shortcuts import redirect, render

from app.forms import ContactForm
from app.models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

# Create a new contact
def contactForm(request):
    form = ContactForm(request.POST)
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'ContactForm.html', {'form': form})

# Update a contact
def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(instance=contact)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'ContactForm.html', {'form': form})

# Delete a contact
def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/')
