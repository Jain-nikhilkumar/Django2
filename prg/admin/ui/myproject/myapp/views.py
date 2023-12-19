# myapp/views.py
from django.shortcuts import render
from .forms import MyForm
from .forms import issue_credentials
from .forms import *
import qrcode  
from io import BytesIO
def my_form(request):
    button_clicked = None

    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            # Check which button was clicked
            if 'issue_credentials' in request.POST:
                button_clicked = 'issue_credentials'
            elif 'create_presentation_template' in request.POST:
                button_clicked = 'create_presentation_template'
            elif 'create_schema' in request.POST:
                button_clicked = 'create_schema'

    else:
        form = MyForm()

    return render(request, 'myapp/my_form.html', {'form': form, 'button_clicked': button_clicked})


def issue_credentials2(request):
    button_clicked = None

    # Your view logic for issuing credentials
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Check which button was clicked
            if 'issue_credentials' in request.POST:
                button_clicked = 'issue_credentials'
            elif 'create_presentation_template' in request.POST:
                button_clicked = 'create_presentation_template'
            elif 'create_schema' in request.POST:
                button_clicked = 'create_schema'
        else:
            form = issue_credentials()
            
            
        return render(request, 'myapp/issue_credentials.html')
    from django.shortcuts import render
from django.http import HttpResponse


def generate_qr_code(request, data):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image or return it in the HTTP response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response