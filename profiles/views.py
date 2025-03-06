from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@login_required
def profile_view(request):
    """
    Display the user's profile & order history
    """
    profile = request.user.userprofile
    orders = profile.orders.all()  # Fetch associated orders

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        password_form = PasswordChangeForm(request.user, request.POST)

        if 'update_profile' in request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the errors')

        elif 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password updated successfully')
                return redirect('profile')
        else:
            messages.error(request, 'Error updating password. Try again.')

    else:
        form = UserProfileForm(instance=profile)
        password_form = PasswordChangeForm(request.user)

    context = {
        'profile': profile,
        'orders': orders,
        'form': form,
        'password_form': password_form,
    }
    return render(request, 'profiles/profile.html', context)


def order_detail_view(request, order_number):
    """
    Display the details of a specific order
    """
    order = get_object_or_404(Order, order_number=order_number, user_profile=request.user.userprofile)

    context = {
        'order': order,
    }
    return render(request, 'profiles/order_detail.html', context)
