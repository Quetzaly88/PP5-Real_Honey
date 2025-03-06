from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order


@login_required
def profile_view(request):
    """
    Display the user's profile & order history
    """
    profile = request.user.userprofile
    orders = profile.orders.all()  # Fetch associated orders

    context = {
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)
