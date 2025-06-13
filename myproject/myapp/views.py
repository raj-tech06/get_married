from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser

# ✅ Registration View

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if MyUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        user = MyUser(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login_user')

    return render(request, 'home.html')


# ✅ Login View
def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = MyUser.objects.get(email=email)

            if user.password == password:
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['user_name'] = user.username

                # ✅ Simple check for admin email
                if email == 'admin@gmail.com':
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
            else:
                messages.error(request, "Incorrect password")
        except MyUser.DoesNotExist:
            messages.error(request, "User does not exist")

    return render(request, 'login.html')

# ✅ Admin Dashboard View
def admin_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login_user')

    if request.session.get('user_email') != 'admin@gmail.com':
        return redirect('dashboard')  # Normal user ko hata do

    user_name = request.session.get('user_name')
    return render(request, 'admin_dashboard.html', {'user_name': user_name})



# ✅ Normal Dashboard View
from django.shortcuts import render, redirect
from .models import MyUser



# def user_dashboard(request):
#     if 'user_id' not in request.session:
#         return redirect('login_user')

#     try:
#         user = MyUser.objects.get(id=request.session['user_id'])
#     except MyUser.DoesNotExist:
#         return redirect('login_user')

#     if request.method == 'POST':
#         user.username = request.POST.get('username')
#         user.email = request.POST.get('email')
#         user.password = request.POST.get('password')
#         user.address = request.POST.get('address')
#         user.city = request.POST.get('city')
#         user.state = request.POST.get('state')
#         user.gender = request.POST.get('gender')

#         if 'profile_image' in request.FILES:
#             user.profile_image = request.FILES['profile_image']

#         user.save()
#         return redirect('user_dashboard')  # Or 'user_dashboard' depending on your URL name

#     context = {
#         'user': user,
#         'show_form': False  # show profile by default
#     }
#     return render(request, 'dashboard.html', context)


# def user_dashboard(request):
#     if 'user_id' not in request.session:
#         return redirect('login_user')

#     try:
#         user = MyUser.objects.get(id=request.session['user_id'])
#     except MyUser.DoesNotExist:
#         return redirect('login_user')

#     if request.method == 'POST':
#         user.username = request.POST.get('username')
#         user.email = request.POST.get('email')
#         user.password = request.POST.get('password')
#         user.address = request.POST.get('address')
#         user.city = request.POST.get('city')
#         user.state = request.POST.get('state')
#         user.gender = request.POST.get('gender')

#         if 'profile_image' in request.FILES:
#         # Delete old image file if not default
#             if user.profile_image and user.profile_image.name != 'default.jpg':
#                 user.profile_image.delete(save=False)
#             user.profile_image = request.FILES['profile_image']

#         user.save()

#         # Update session username if changed
#         request.session['user_name'] = user.username

#         return redirect('user_dashboard')  # reload without POST

#     return render(request, 'dashboard.html', {
#         'user': user,
#         'show_form': False  # form hidden by default
#     })


def user_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login_user')

    try:
        user = MyUser.objects.get(id=request.session['user_id'])
    except MyUser.DoesNotExist:
        return redirect('login_user')

    # Flags from GET parameters
    show_form = request.GET.get('edit') == '1'
    show_membership = request.GET.get('membership') == '1'

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.address = request.POST.get('address')
        user.city = request.POST.get('city')
        user.state = request.POST.get('state')
        user.gender = request.POST.get('gender')

        if 'profile_image' in request.FILES:
            if user.profile_image and user.profile_image.name != 'profiles/default.png':
                user.profile_image.delete(save=False)
            user.profile_image = request.FILES['profile_image']

        user.save()
        request.session['user_name'] = user.username
        return redirect('user_dashboard')

    return render(request, 'dashboard.html', {
        'user': user,
        'show_form': show_form,
        'show_membership': show_membership,
    })



def logout_view(request):
    request.session.flush()  # session clear kar do
    return redirect('login_user')



# -------------------------user dashboard ke andar=================

def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('login_user')

    try:
        user = MyUser.objects.get(id=request.session['user_id'])
    except MyUser.DoesNotExist:
        return redirect('login_user')

    return render(request, 'dashboard.html', {
        'user': user,
        'show_form': True  # this will show the form
    })
