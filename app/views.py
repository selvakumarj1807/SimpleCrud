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

