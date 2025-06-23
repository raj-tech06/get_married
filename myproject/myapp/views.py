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
from .models import GirlsProfile, BoysProfile, DisabledProfile, DivorcedProfile, MyUser  # ✅ MyUser import

def admin_dashboard(request):
    if request.session.get('user_email') != 'admin@gmail.com':
        return redirect('user_dashboard')

    user_name = request.session.get('user_name')

    # ✅ Handle form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        caste = request.POST.get('lastname')  # ✅ Map lastname input to caste field
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
            'caste': caste,  # ✅ Saving into caste field
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

    # ✅ Show data based on filter
    if view_type == 'girls':
        context['girls'] = GirlsProfile.objects.all()
    elif view_type == 'boys':
        context['boys'] = BoysProfile.objects.all()
    elif view_type == 'disabled':
        context['disabled'] = DisabledProfile.objects.all()
    elif view_type == 'divorced':
        context['divorced'] = DivorcedProfile.objects.all()
    elif view_type == 'users':
        context['users'] = MyUser.objects.all()  # ✅ Show registered users

    return render(request, 'admin_dashboard.html', context)

# --------------------- USER DASHBOARD ---------------------
from django.shortcuts import render, redirect
from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile, UserPhoto
from .forms import UserPhotoForm

def user_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login_user')

    try:
        user = MyUser.objects.get(id=request.session['user_id'])
    except MyUser.DoesNotExist:
        return redirect('login_user')

    # GET section flags
    show_form = request.GET.get('edit') == '1'
    show_membership = request.GET.get('membership') == '1'
    show_boys = request.GET.get('boys') == '1'
    show_girls = request.GET.get('girls') == '1'
    show_disabled = request.GET.get('disabled') == '1'
    show_divorced = request.GET.get('divorced') == '1'
    show_add_photo = request.GET.get('add_photo') == '1'
        
    if request.method == 'POST' and not show_add_photo:
        category = request.POST.get('category')  # ✅ Get selected category from form

        # --- Update User Model ---
        user.username = request.POST.get('username')
        user.caste = request.POST.get('lastname')
        user.phone = request.POST.get('phone')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.address = request.POST.get('address')
        user.city = request.POST.get('city')
        user.state = request.POST.get('state')
        user.gender = request.POST.get('gender')
        user.category = category  # ✅ Save chosen category

        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
        user.save()

        # --- First: Delete from all other category models ---
        GirlsProfile.objects.filter(email=user.email).delete()
        BoysProfile.objects.filter(email=user.email).delete()
        DisabledProfile.objects.filter(email=user.email).delete()
        DivorcedProfile.objects.filter(email=user.email).delete()

        # --- Then: Save in selected category ---
        profile_data = {
            'name': user.username,
            'caste': user.caste,
            'email': user.email,
            'phone': user.phone,
            'address': user.address,
            'city': user.city,
            'state': user.state,
            'gender': user.gender,
            'image': user.profile_image
        }

        if category == 'girls':
            GirlsProfile.objects.create(**profile_data)
        elif category == 'boys':
            BoysProfile.objects.create(**profile_data)
        elif category == 'disabled':
            DisabledProfile.objects.create(**profile_data)
        elif category == 'divorced':
            DivorcedProfile.objects.create(**profile_data)

        return redirect('user_dashboard')


    # === Handle Photo Upload ===
    photo_form = UserPhotoForm()
    if request.method == 'POST' and show_add_photo:
        photo_form = UserPhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo = photo_form.save(commit=False)
            photo.user = user
            photo.save()
            return redirect('user_dashboard')

    # === User Photos ===
    user_photos = user.photos.all()

    # === GIRLS FILTER ===
    girls_profiles = GirlsProfile.objects.all()
    caste_choices_girls = GirlsProfile.objects.values_list('caste', flat=True).distinct()
    search_query_girls = request.GET.get('search', '') if show_girls else ''
    selected_caste_girls = request.GET.get('caste', '') if show_girls else ''
    if show_girls:
        if search_query_girls:
            girls_profiles = girls_profiles.filter(name__icontains=search_query_girls) | girls_profiles.filter(caste__icontains=search_query_girls)
        if selected_caste_girls:
            girls_profiles = girls_profiles.filter(caste=selected_caste_girls)

    # === BOYS FILTER ===
    boys_profiles = BoysProfile.objects.all()
    caste_choices_boys = BoysProfile.objects.values_list('caste', flat=True).distinct()
    search_query_boys = request.GET.get('search', '') if show_boys else ''
    selected_caste_boys = request.GET.get('caste', '') if show_boys else ''
    if show_boys:
        if search_query_boys:
            boys_profiles = boys_profiles.filter(name__icontains=search_query_boys) | boys_profiles.filter(caste__icontains=search_query_boys)
        if selected_caste_boys:
            boys_profiles = boys_profiles.filter(caste=selected_caste_boys)

    # === DISABLED FILTER ===
    disabled_profiles = DisabledProfile.objects.all()
    caste_choices_disabled = DisabledProfile.objects.values_list('caste', flat=True).distinct()
    search_query_disabled = request.GET.get('search', '') if show_disabled else ''
    selected_caste_disabled = request.GET.get('caste', '') if show_disabled else ''
    if show_disabled:
        if search_query_disabled:
            disabled_profiles = disabled_profiles.filter(name__icontains=search_query_disabled) | disabled_profiles.filter(caste__icontains=search_query_disabled)
        if selected_caste_disabled:
            disabled_profiles = disabled_profiles.filter(caste=selected_caste_disabled)
    # === DIVORCED FILTER ===
    divorced_profiles = DivorcedProfile.objects.all()
    caste_choices_divorced = DivorcedProfile.objects.values_list('caste', flat=True).distinct()
    search_query_divorced = request.GET.get('search', '') if show_divorced else ''
    selected_caste_divorced = request.GET.get('caste', '') if show_divorced else ''
    if show_divorced:
        if search_query_divorced:
            divorced_profiles = divorced_profiles.filter(name__icontains=search_query_divorced) | divorced_profiles.filter(caste__icontains=search_query_divorced)
        if selected_caste_divorced:
            divorced_profiles = divorced_profiles.filter(caste=selected_caste_divorced)

    # ✅ Add this: Match photos by user email
    user_photos_dict = {}
    for u in MyUser.objects.all():
        user_photos_dict[u.email] = u.photos.all()

    for boy in boys_profiles:
        boy.extra_photos = UserPhoto.objects.filter(user__email=boy.email).all()

    for girl in girls_profiles:
        girl.extra_photos = UserPhoto.objects.filter(user__email=girl.email).all()

    for disabled in disabled_profiles:
        disabled.extra_photos = UserPhoto.objects.filter(user__email=disabled.email).all()

    for divorced in divorced_profiles:
        divorced.extra_photos = UserPhoto.objects.filter(user__email=divorced.email).all()


    return render(request, 'dashboard.html', {
        'user': user,
        'show_form': show_form,
        'show_membership': show_membership,
        'show_add_photo': show_add_photo, 
        'show_boys': show_boys,
        'show_girls': show_girls,
        'show_disabled': show_disabled,
        'show_divorced': show_divorced,
        'user_photos': user_photos,
        'users': MyUser.objects.all(),
        'user_photos_dict': user_photos_dict,
        'photo_form': photo_form if show_add_photo else None,

        # Girls
        'girls_profiles': girls_profiles,
        'caste_choices': caste_choices_girls,
        'selected_caste': selected_caste_girls,
        'search_query': search_query_girls,

        # Boys
        'boys_profiles': boys_profiles,
        'caste_choices_boys': caste_choices_boys,
        'selected_caste_boys': selected_caste_boys,
        'search_query_boys': search_query_boys,

        # Disabled
        'disabled_profiles': disabled_profiles,
        'caste_choices_disabled': caste_choices_disabled,
        'selected_caste_disabled': selected_caste_disabled,
        'search_query_disabled': search_query_disabled,

        # Divorced
        'divorced_profiles': divorced_profiles,
        'caste_choices_divorced': caste_choices_divorced,
        'selected_caste_divorced': selected_caste_divorced,
        'search_query_divorced': search_query_divorced,
    })

# from django.shortcuts import render, redirect
# from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile

# def user_dashboard(request):
#     if 'user_id' not in request.session:
#         return redirect('login_user')

#     try:
#         user = MyUser.objects.get(id=request.session['user_id'])
#     except MyUser.DoesNotExist:
#         return redirect('login_user')

#     # GET section flags
#     show_form = request.GET.get('edit') == '1'
#     show_membership = request.GET.get('membership') == '1'
#     show_boys = request.GET.get('boys') == '1'
#     show_girls = request.GET.get('girls') == '1'
#     show_disabled = request.GET.get('disabled') == '1'
#     show_divorced = request.GET.get('divorced') == '1'

#     # ✅ Form submission
#     if request.method == 'POST':
#         user.username = request.POST.get('username')
#         user.caste = request.POST.get('lastname')   # ✅ lastname from form -> caste field
#         user.email = request.POST.get('email')
#         user.password = request.POST.get('password')
#         user.address = request.POST.get('address')
#         user.city = request.POST.get('city')
#         user.state = request.POST.get('state')
#         user.gender = request.POST.get('gender')
#         if 'profile_image' in request.FILES:
#             user.profile_image = request.FILES['profile_image']
#         user.save()
#         return redirect('user_dashboard')

#     # === GIRLS FILTER ===
#     girls_profiles = GirlsProfile.objects.all()
#     caste_choices_girls = GirlsProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_girls = request.GET.get('search', '') if show_girls else ''
#     selected_caste_girls = request.GET.get('caste', '') if show_girls else ''

#     if show_girls:
#         if search_query_girls:
#             girls_profiles = girls_profiles.filter(name__icontains=search_query_girls) | girls_profiles.filter(caste__icontains=search_query_girls)
#         if selected_caste_girls:
#             girls_profiles = girls_profiles.filter(caste=selected_caste_girls)

#     # === BOYS FILTER ===
#     boys_profiles = BoysProfile.objects.all()
#     caste_choices_boys = BoysProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_boys = request.GET.get('search', '') if show_boys else ''
#     selected_caste_boys = request.GET.get('caste', '') if show_boys else ''

#     if show_boys:
#         if search_query_boys:
#             boys_profiles = boys_profiles.filter(name__icontains=search_query_boys) | boys_profiles.filter(caste__icontains=search_query_boys)
#         if selected_caste_boys:
#             boys_profiles = boys_profiles.filter(caste=selected_caste_boys)

#     # === DISABLED FILTER ===
#     disabled_profiles = DisabledProfile.objects.all()
#     caste_choices_disabled = DisabledProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_disabled = request.GET.get('search', '') if show_disabled else ''
#     selected_caste_disabled = request.GET.get('caste', '') if show_disabled else ''

#     if show_disabled:
#         if search_query_disabled:
#             disabled_profiles = disabled_profiles.filter(name__icontains=search_query_disabled) | disabled_profiles.filter(caste__icontains=search_query_disabled)
#         if selected_caste_disabled:
#             disabled_profiles = disabled_profiles.filter(caste=selected_caste_disabled)

#     # === DIVORCED FILTER ===
#     divorced_profiles = DivorcedProfile.objects.all()
#     caste_choices_divorced = DivorcedProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_divorced = request.GET.get('search', '') if show_divorced else ''
#     selected_caste_divorced = request.GET.get('caste', '') if show_divorced else ''

#     if show_divorced:
#         if search_query_divorced:
#             divorced_profiles = divorced_profiles.filter(name__icontains=search_query_divorced) | divorced_profiles.filter(caste__icontains=search_query_divorced)
#         if selected_caste_divorced:
#             divorced_profiles = divorced_profiles.filter(caste=selected_caste_divorced)

#     return render(request, 'dashboard.html', {
#         'user': user,
#         'show_form': show_form,
#         'show_membership': show_membership,
#         'show_boys': show_boys,
#         'show_girls': show_girls,
#         'show_disabled': show_disabled,
#         'show_divorced': show_divorced,

#         # Girls
#         'girls_profiles': girls_profiles,
#         'caste_choices': caste_choices_girls,
#         'selected_caste': selected_caste_girls,
#         'search_query': search_query_girls,

#         # Boys
#         'boys_profiles': boys_profiles,
#         'caste_choices_boys': caste_choices_boys,
#         'selected_caste_boys': selected_caste_boys,
#         'search_query_boys': search_query_boys,

#         # Disabled
#         'disabled_profiles': disabled_profiles,
#         'caste_choices_disabled': caste_choices_disabled,
#         'selected_caste_disabled': selected_caste_disabled,
#         'search_query_disabled': search_query_disabled,

#         # Divorced
#         'divorced_profiles': divorced_profiles,
#         'caste_choices_divorced': caste_choices_divorced,
#         'selected_caste_divorced': selected_caste_divorced,
#         'search_query_divorced': search_query_divorced,
#     })

# ------------------------------------------------
# from django.shortcuts import render, redirect
# from django.db.models import Q
# from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile

# def user_dashboard(request):
#     if 'user_id' not in request.session:
#         return redirect('login_user')

#     try:
#         user = MyUser.objects.get(id=request.session['user_id'])
#     except MyUser.DoesNotExist:
#         return redirect('login_user')

#     # Show sections based on GET parameters
#     show_form = request.GET.get('edit') == '1'
#     show_membership = request.GET.get('membership') == '1'
#     show_boys = request.GET.get('boys') == '1'
#     show_girls = request.GET.get('girls') == '1'
#     show_disabled = request.GET.get('disabled') == '1'
#     show_divorced = request.GET.get('divorced') == '1'

#     # Handle Profile Edit Form Submit
#     if request.method == 'POST':
#         user.username = request.POST['username']
#         user.email = request.POST['email']
#         user.password = request.POST['password']
#         user.address = request.POST['address']
#         user.city = request.POST['city']
#         user.state = request.POST['state']
#         user.gender = request.POST['gender']
#         if 'profile_image' in request.FILES:
#             user.profile_image = request.FILES['profile_image']
#         user.save()
#         return redirect('user_dashboard')

#     # ---- Girls Profile Filter ----
#     girls_profiles = GirlsProfile.objects.all()
#     caste_choices = GirlsProfile.objects.values_list('caste', flat=True).distinct()
#     selected_caste = request.GET.get('caste', '').strip()
#     search_query = request.GET.get('search', '').strip()

#     if show_girls:
#         if search_query and selected_caste:
#             girls_profiles = GirlsProfile.objects.filter(
#                 Q(name__icontains=search_query) | Q(caste__icontains=search_query),
#                 caste=selected_caste
#             )
#         elif search_query:
#             girls_profiles = GirlsProfile.objects.filter(
#                 Q(name__icontains=search_query) | Q(caste__icontains=search_query)
#             )
#         elif selected_caste:
#             girls_profiles = GirlsProfile.objects.filter(caste=selected_caste)
#         else:
#             girls_profiles = GirlsProfile.objects.all()  # show all when no filter
#     else:
#         girls_profiles = GirlsProfile.objects.none()  # hide if not show_girls

#     return render(request, 'dashboard.html', {
#         'user': user,
#         'show_form': show_form,
#         'show_membership': show_membership,
#         'show_boys': show_boys,
#         'show_girls': show_girls,
#         'show_disabled': show_disabled,
#         'show_divorced': show_divorced,
#         'boys_profiles': BoysProfile.objects.all(),
#         'girls_profiles': girls_profiles,
#         'disabled_profiles': DisabledProfile.objects.all(),
#         'divorced_profiles': DivorcedProfile.objects.all(),
#         'caste_choices': caste_choices,
#         'selected_caste': selected_caste,
#         'search_query': search_query,
#     })

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

# =========================================other========================================================



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import MyUser

# # --------------------- REGISTER ---------------------
# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect('register')

#         # Check if email is blocked
#         blocked_email = MyUser.objects.filter(email=email, is_blocked=True).exists()
#         if blocked_email:
#             messages.error(request, "This email is blocked. You cannot register.")
#             return redirect('register')

#         if MyUser.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered!")
#             return redirect('register')

#         # Save user
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

#             # Block check
#             if user.is_blocked:
#                 messages.error(request, "Your account has been blocked. Contact admin.")
#                 return redirect('login_user')

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

# # --------------------- LOGOUT ---------------------
# def logout_view(request):
#     request.session.flush()
#     return redirect('login_user')


# # --------------------- ADMIN DASHBOARD ---------------------

# from django.shortcuts import render, redirect
# from .models import GirlsProfile, BoysProfile, DisabledProfile, DivorcedProfile, MyUser  # ✅ MyUser import

# def admin_dashboard(request):
#     if request.session.get('user_email') != 'admin@gmail.com':
#         return redirect('user_dashboard')

#     user_name = request.session.get('user_name')

#     # ✅ Handle form submission
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         caste = request.POST.get('lastname')  # ✅ Map lastname input to caste field
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
#             'caste': caste,  # ✅ Saving into caste field
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

#     view_type = request.GET.get('view', '')
#     context = {
#         'user_name': user_name,
#     }

#     # ✅ Show data based on filter
#     if view_type == 'girls':
#         context['girls'] = GirlsProfile.objects.all()
#     elif view_type == 'boys':
#         context['boys'] = BoysProfile.objects.all()
#     elif view_type == 'disabled':
#         context['disabled'] = DisabledProfile.objects.all()
#     elif view_type == 'divorced':
#         context['divorced'] = DivorcedProfile.objects.all()
#     elif view_type == 'users':
#         context['users'] = MyUser.objects.all()  # ✅ Show registered users

#     return render(request, 'admin_dashboard.html', context)

# # --------------------- USER DASHBOARD ---------------------

# from django.shortcuts import render, redirect
# from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile
# from .models import GirlProfilePhoto, BoyProfilePhoto, DisabledProfilePhoto, DivorcedProfilePhoto  # ✅

# def user_dashboard(request):
#     if 'user_id' not in request.session:
#         return redirect('login_user')

#     try:
#         user = MyUser.objects.get(id=request.session['user_id'])
#     except MyUser.DoesNotExist:
#         return redirect('login_user')

#     # GET section flags
#     show_form = request.GET.get('edit') == '1'
#     show_add_photo = request.GET.get('add_photo') == '1'
#     show_membership = request.GET.get('membership') == '1'
#     show_boys = request.GET.get('boys') == '1'
#     show_girls = request.GET.get('girls') == '1'
#     show_disabled = request.GET.get('disabled') == '1'
#     show_divorced = request.GET.get('divorced') == '1'

#     # ✅ Profile Update Form Submission
#     if request.method == 'POST' and 'add_photo' not in request.POST:
#         user.username = request.POST.get('username')
#         user.caste = request.POST.get('lastname')   # ✅ lastname = caste
#         user.email = request.POST.get('email')
#         user.password = request.POST.get('password')
#         user.address = request.POST.get('address')
#         user.city = request.POST.get('city')
#         user.state = request.POST.get('state')
#         user.gender = request.POST.get('gender')
#         if 'profile_image' in request.FILES:
#             user.profile_image = request.FILES['profile_image']
#         user.save()
#         return redirect('user_dashboard')

#     # ✅ Add More Photo Logic
#     if request.method == 'POST' and 'add_photo' in request.POST:
#         image = request.FILES.get('image')
#         typ = request.POST.get('type')
#         profile_id = request.POST.get('profile_id')

#         if image and typ and profile_id:
#             model_map = {
#                 'girls': (GirlsProfile, GirlProfilePhoto, 'girl'),
#                 'boys': (BoysProfile, BoyProfilePhoto, 'boy'),
#                 'disabled': (DisabledProfile, DisabledProfilePhoto, 'disabled'),
#                 'divorced': (DivorcedProfile, DivorcedProfilePhoto, 'divorced'),
#             }
#             ProfileModel, PhotoModel, fk = model_map[typ]
#             instance = ProfileModel.objects.get(id=profile_id)
#             PhotoModel.objects.create(**{fk: instance, 'image': image})
#             return redirect(f'?{typ}=1')

#     # === GIRLS FILTER ===
#     girls_profiles = GirlsProfile.objects.all().prefetch_related('photos')
#     caste_choices_girls = GirlsProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_girls = request.GET.get('search', '') if show_girls else ''
#     selected_caste_girls = request.GET.get('caste', '') if show_girls else ''

#     if show_girls:
#         if search_query_girls:
#             girls_profiles = girls_profiles.filter(name__icontains=search_query_girls) | girls_profiles.filter(caste__icontains=search_query_girls)
#         if selected_caste_girls:
#             girls_profiles = girls_profiles.filter(caste=selected_caste_girls)

#     # === BOYS FILTER ===
#     boys_profiles = BoysProfile.objects.all().prefetch_related('photos')
#     caste_choices_boys = BoysProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_boys = request.GET.get('search', '') if show_boys else ''
#     selected_caste_boys = request.GET.get('caste', '') if show_boys else ''

#     if show_boys:
#         if search_query_boys:
#             boys_profiles = boys_profiles.filter(name__icontains=search_query_boys) | boys_profiles.filter(caste__icontains=search_query_boys)
#         if selected_caste_boys:
#             boys_profiles = boys_profiles.filter(caste=selected_caste_boys)

#     # === DISABLED FILTER ===
#     disabled_profiles = DisabledProfile.objects.all().prefetch_related('photos')
#     caste_choices_disabled = DisabledProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_disabled = request.GET.get('search', '') if show_disabled else ''
#     selected_caste_disabled = request.GET.get('caste', '') if show_disabled else ''

#     if show_disabled:
#         if search_query_disabled:
#             disabled_profiles = disabled_profiles.filter(name__icontains=search_query_disabled) | disabled_profiles.filter(caste__icontains=search_query_disabled)
#         if selected_caste_disabled:
#             disabled_profiles = disabled_profiles.filter(caste=selected_caste_disabled)

#     # === DIVORCED FILTER ===
#     divorced_profiles = DivorcedProfile.objects.all().prefetch_related('photos')
#     caste_choices_divorced = DivorcedProfile.objects.values_list('caste', flat=True).distinct()
#     search_query_divorced = request.GET.get('search', '') if show_divorced else ''
#     selected_caste_divorced = request.GET.get('caste', '') if show_divorced else ''

#     if show_divorced:
#         if search_query_divorced:
#             divorced_profiles = divorced_profiles.filter(name__icontains=search_query_divorced) | divorced_profiles.filter(caste__icontains=search_query_divorced)
#         if selected_caste_divorced:
#             divorced_profiles = divorced_profiles.filter(caste=selected_caste_divorced)

#     return render(request, 'dashboard.html', {
#         'user': user,
#         'show_form': show_form,
#         'show_add_photo': show_add_photo,
#         'show_membership': show_membership,
#         'show_boys': show_boys,
#         'show_girls': show_girls,
#         'show_disabled': show_disabled,
#         'show_divorced': show_divorced,

#         # Girls
#         'girls_profiles': girls_profiles,
#         'caste_choices': caste_choices_girls,
#         'selected_caste': selected_caste_girls,
#         'search_query': search_query_girls,

#         # Boys
#         'boys_profiles': boys_profiles,
#         'caste_choices_boys': caste_choices_boys,
#         'selected_caste_boys': selected_caste_boys,
#         'search_query_boys': search_query_boys,

#         # Disabled
#         'disabled_profiles': disabled_profiles,
#         'caste_choices_disabled': caste_choices_disabled,
#         'selected_caste_disabled': selected_caste_disabled,
#         'search_query_disabled': search_query_disabled,

#         # Divorced
#         'divorced_profiles': divorced_profiles,
#         'caste_choices_divorced': caste_choices_divorced,
#         'selected_caste_divorced': selected_caste_divorced,
#         'search_query_divorced': search_query_divorced,
#     })


# # --------------------- PROFILE EDIT SHORTCUT ---------------------
# def edit_profile(request):
#     if 'user_id' not in request.session:
#         return redirect('login_user')

#     try:
#         user = MyUser.objects.get(id=request.session['user_id'])
#     except MyUser.DoesNotExist:
#         return redirect('login_user')

#     return render(request, 'dashboard.html', {
#         'user': user,
#         'show_form': True
#     })


# # ==================================
# def delete_profile(request, category, id):
#     if category == 'girls':
#         GirlsProfile.objects.filter(id=id).delete()
#     elif category == 'boys':
#         BoysProfile.objects.filter(id=id).delete()
#     elif category == 'disabled':
#         DisabledProfile.objects.filter(id=id).delete()
#     elif category == 'divorced':
#         DivorcedProfile.objects.filter(id=id).delete()

#     return redirect(f'/admin_dashboard/?view={category}')


# # views.py

# from django.shortcuts import get_object_or_404, redirect
# from .models import MyUser
# from django.contrib import messages

# def delete_user(request, user_id):
#     if request.method == 'POST':
#         user = get_object_or_404(MyUser, id=user_id)
#         user.delete()
#         messages.success(request, "User deleted successfully.")
#     return redirect('admin_dashboard')


# # views.py
# from django.contrib import messages
# from django.shortcuts import redirect, get_object_or_404
# from .models import MyUser

# def block_user(request, user_id):
#     user = get_object_or_404(MyUser, id=user_id)
#     user.is_blocked = not user.is_blocked  # Toggle block/unblock
#     user.save()
#     if user.is_blocked:
#         messages.success(request, f"{user.username} has been blocked.")
#     else:
#         messages.success(request, f"{user.username} has been unblocked.")
#     return redirect('/admin_dashboard/?view=users')

