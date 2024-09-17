from django.shortcuts import render, redirect
from .models import PageContent, Product, Service, Contact
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect back to home after successful submission
    else:
        form = ContactForm()

    content = PageContent.objects.first()  # Assumes a single content instance
    products = Product.objects.all()
    services = Service.objects.all()

    # Preprocess the features for each product
    for product in products:
        product.features_list = product.features.split(',')

    return render(request, 'home/templates/home.html', {'form': form, 'content': content, 'products': products, 'services': services})