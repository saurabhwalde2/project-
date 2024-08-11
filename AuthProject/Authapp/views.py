from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import Reg

# Create your views here.
def home(r):
    return render(r,'Authapp/index.html')

@login_required()
def java(r):
    return render(r,'Authapp/java.html')

@login_required()
def python(r):
    return render(r,'Authapp/python.html')

# signup form
# Import the custom form Reg which is a ModelForm for the User model

def signup(r):
    # Check if the request method is POST, indicating that form data has been submitted
    if r.method == 'POST':
        form = Reg(r.POST)  # Create an instance of the Reg form with the submitted data
        if form.is_valid():  # Validate the form data
            user = form.save(commit=False)  # Create a user object but don't save it to the database yet
            user.set_password(form.cleaned_data['password'])  # Hash the password before saving
            user.save()  # Save the user object to the database
            return HttpResponseRedirect('/')  # Redirect the user to the home page after successful signup
        else:
            # If the form is not valid, render the signup page with the form and error messages
            return render(r, 'Authapp/signup.html', {'form': form})
    else:
        form = Reg()  # If the request method is not POST, create an empty form instance
    return render(r, 'Authapp/signup.html', {'form': form})  # Render the signup page with the empty form


#logout function:
"""def logout_view(request):
    return render(request, 'registration/logout.html')"""

