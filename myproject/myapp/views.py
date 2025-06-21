from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile

# --------------------- REGISTRATION ---------------------
# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect('register')

#         if MyUser.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered!")
#             return redirect('register')

#         MyUser.objects.create(username=username, email=email, password=password)
#         messages.success(request, "Registration successful! Please log in.")
#         return redirect('login_user')

#     return render(request, 'home.html')


# # --------------------- LOGIN ---------------------
# def login_user(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = MyUser.objects.get(email=email)

#             if user.password == password:
#                 request.session['user_id'] = user.id
#                 request.session['user_email'] = user.email
#                 request.session['user_name'] = user.username

#                 if email == 'admin@gmail.com':
#                     return redirect('admin_dashboard')
#                 return redirect('user_dashboard')
#             else:
#                 messages.error(request, "Incorrect password")
#         except MyUser.DoesNotExist:
#             messages.error(request, "User does not exist")

#     return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser

# --------------------- REGISTER ---------------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Check if email is blocked
        blocked_email = MyUser.objects.filter(email=email, is_blocked=True).exists()
        if blocked_email:
            messages.error(request, "This email is blocked. You cannot register.")
            return redirect('register')

        if MyUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        # Save user
        MyUser.objects.create(username=username, email=email, password=password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login_user')

    return render(request, 'home.html')


# --------------------- LOGIN ---------------------
def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = MyUser.objects.get(email=email)

            # Block check
            if user.is_blocked:
                messages.error(request, "Your account has been blocked. Contact admin.")
                return redirect('login_user')

            if user.password == password:
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['user_name'] = user.username

                if email == 'admin@gmail.com':
                    return redirect('admin_dashboard')
                return redirect('user_dashboard')
            else:
                messages.error(request, "Incorrect password")
        except MyUser.DoesNotExist:
            messages.error(request, "User does not exist")

    return render(request, 'login.html')

# --------------------- LOGOUT ---------------------
def logout_view(request):
    request.session.flush()
    return redirect('login_user')


# --------------------- ADMIN DASHBOARD ---------------------
# from .models import GirlsProfile, BoysProfile, DisabledProfile, DivorcedProfile

# def admin_dashboard(request):
#     if request.session.get('user_email') != 'admin@gmail.com':
#         return redirect('user_dashboard')

#     user_name = request.session.get('user_name')

#     # If profile form is submitted
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         gender = request.POST.get('gender')
#         category = request.POST.get('category')
#         image = request.FILES.get('image')

#         profile_data = {
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'address': address,
#             'city': city,
#             'state': state,
#             'gender': gender,
#             'image': image,
#         }

#         if category == 'girls':
#             GirlsProfile.objects.create(**profile_data)
#         elif category == 'boys':
#             BoysProfile.objects.create(**profile_data)
#         elif category == 'disabled':
#             DisabledProfile.objects.create(**profile_data)
#         elif category == 'divorced':
#             DivorcedProfile.objects.create(**profile_data)

#         return redirect('admin_dashboard')

#     # GET Request → Check view param
#     view_type = request.GET.get('view', '')

#     context = {
#         'user_name': user_name,
#     }

#     # Add profile lists according to view
#     if view_type == 'girls':
#         context['girls'] = GirlsProfile.objects.all()
#     elif view_type == 'boys':
#         context['boys'] = BoysProfile.objects.all()
#     elif view_type == 'disabled':
#         context['disabled'] = DisabledProfile.objects.all()
#     elif view_type == 'divorced':
#         context['divorced'] = DivorcedProfile.objects.all()

#     return render(request, 'admin_dashboard.html', context)

from django.shortcuts import render, redirect
from .models import GirlsProfile, BoysProfile, DisabledProfile, DivorcedProfile, MyUser  # ✅ MyUser import karo

def admin_dashboard(request):
    if request.session.get('user_email') != 'admin@gmail.com':
        return redirect('user_dashboard')

    user_name = request.session.get('user_name')

    # ✅ Handle form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        profile_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'city': city,
            'state': state,
            'gender': gender,
            'image': image,
        }

        if category == 'girls':
            GirlsProfile.objects.create(**profile_data)
        elif category == 'boys':
            BoysProfile.objects.create(**profile_data)
        elif category == 'disabled':
            DisabledProfile.objects.create(**profile_data)
        elif category == 'divorced':
            DivorcedProfile.objects.create(**profile_data)

        return redirect('admin_dashboard')

    view_type = request.GET.get('view', '')
    context = {
        'user_name': user_name,
    }

    # ✅ Filter based on view
    if view_type == 'girls':
        context['girls'] = GirlsProfile.objects.all()
    elif view_type == 'boys':
        context['boys'] = BoysProfile.objects.all()
    elif view_type == 'disabled':
        context['disabled'] = DisabledProfile.objects.all()
    elif view_type == 'divorced':
        context['divorced'] = DivorcedProfile.objects.all()
    elif view_type == 'users':
        context['users'] = MyUser.objects.all()  # ✅ All registered users

    return render(request, 'admin_dashboard.html', context)

# --------------------- USER DASHBOARD ---------------------
def user_dashboard(request):
    # Block admin login from using this dashboard
    # if request.session.get('user_email') == 'admin@gmail.com':
    #     return redirect('admin_dashboard')

    if 'user_id' not in request.session:
        return redirect('login_user')

    try:
        user = MyUser.objects.get(id=request.session['user_id'])
    except MyUser.DoesNotExist:
        return redirect('login_user')

    # Show sections based on GET parameters
    show_form = request.GET.get('edit') == '1'
    show_membership = request.GET.get('membership') == '1'
    show_boys = request.GET.get('boys') == '1'
    show_girls = request.GET.get('girls') == '1'
    show_disabled = request.GET.get('disabled') == '1'
    show_divorced = request.GET.get('divorced') == '1'

    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.address = request.POST['address']
        user.city = request.POST['city']
        user.state = request.POST['state']
        user.gender = request.POST['gender']
        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
        user.save()
        return redirect('user_dashboard')

    return render(request, 'dashboard.html', {
        'user': user,
        'show_form': show_form,
        'show_membership': show_membership,
        'show_boys': show_boys,
        'show_girls': show_girls,
        'show_disabled': show_disabled,
        'show_divorced': show_divorced,
        'boys_profiles': BoysProfile.objects.all(),
        'girls_profiles': GirlsProfile.objects.all(),
        'disabled_profiles': DisabledProfile.objects.all(),
        'divorced_profiles': DivorcedProfile.objects.all(),
    })


# --------------------- PROFILE EDIT SHORTCUT ---------------------
def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('login_user')

    try:
        user = MyUser.objects.get(id=request.session['user_id'])
    except MyUser.DoesNotExist:
        return redirect('login_user')

    return render(request, 'dashboard.html', {
        'user': user,
        'show_form': True
    })


# ==================================
def delete_profile(request, category, id):
    if category == 'girls':
        GirlsProfile.objects.filter(id=id).delete()
    elif category == 'boys':
        BoysProfile.objects.filter(id=id).delete()
    elif category == 'disabled':
        DisabledProfile.objects.filter(id=id).delete()
    elif category == 'divorced':
        DivorcedProfile.objects.filter(id=id).delete()

    return redirect(f'/admin_dashboard/?view={category}')


# views.py

from django.shortcuts import get_object_or_404, redirect
from .models import MyUser
from django.contrib import messages

def delete_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(MyUser, id=user_id)
        user.delete()
        messages.success(request, "User deleted successfully.")
    return redirect('admin_dashboard')


# views.py
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import MyUser

def block_user(request, user_id):
    user = get_object_or_404(MyUser, id=user_id)
    user.is_blocked = not user.is_blocked  # Toggle block/unblock
    user.save()
    if user.is_blocked:
        messages.success(request, f"{user.username} has been blocked.")
    else:
        messages.success(request, f"{user.username} has been unblocked.")
    return redirect('/admin_dashboard/?view=users')


# def block_user(request, user_id):
#     if request.method == 'POST':
#         user = get_object_or_404(MyUser, id=user_id)
#         user.is_blocked = True
#         user.save()
#         messages.warning(request, "User has been blocked.")
#     return redirect('admin_dashboard')

