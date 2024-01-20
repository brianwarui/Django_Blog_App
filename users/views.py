from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages 
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import PasswordResetView
# from django.urls import reverse_lazy
# Create your views here.






# class CustomPasswordResetView(PasswordResetView):
#     success_url = reverse_lazy('password-reset-done')


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created successfully for {username}!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})



@login_required
def profile(request):
	if request.method == "POST":
		u_form = UserProfileForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'{request.user.username} profile update successful!')
			return redirect('profile')

	else:
		u_form = UserProfileForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
	'u_form':u_form,
	'p_form':p_form

	}
	return render(request, 'users/profile.html', context)

@login_required
def delete_user(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)

    # Check if the logged-in user matches the user being deleted
    if request.user != user_to_delete:
       return redirect('home')

    if request.method == 'POST':
       profile = get_object_or_404(Profile, user=user_to_delete)
       profile.delete()
       user_to_delete.delete()

       return redirect('home')  # Redirect to home or any other page after deletion

    return render(request, 'users/delete_user_confirm.html', {'user': user_to_delete})
