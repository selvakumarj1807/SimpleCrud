from django.shortcuts import redirect, render

from app.models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

# Create a new contact
def contactForm(request):
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        gmail = request.POST['gmail']
        Contact.objects.create(name=name, mobile=mobile, gmail=gmail)
        return redirect('/')
    return render(request, 'ContactForm.html')

# Update a contact
def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.name = request.POST['name']
        contact.mobile = request.POST['mobile']
        contact.gmail = request.POST['gmail']
        contact.save()
        return redirect('/')
    return render(request, 'ContactForm.html', {'contact': contact})

# Delete a contact
def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/')
