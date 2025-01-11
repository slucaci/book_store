from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """ A view to display the user's profile """
    return render(request, 'profiles/profile.html')
