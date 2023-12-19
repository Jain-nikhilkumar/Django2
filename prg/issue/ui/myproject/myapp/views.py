# myapp/views.py
from django.shortcuts import render
from .forms import MyForm
from .forms import issue_credentials

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