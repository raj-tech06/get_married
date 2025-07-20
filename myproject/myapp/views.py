from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile
from .models import RegistrationNotification


# --------------------- REGISTER ---------------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        number = request.POST.get('number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if len(number) != 10 or not number.isdigit():
            messages.error(request, "Mobile number must be exactly 10 digits.")
            return redirect('register')


        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # ✅ Notification save (optional)
        RegistrationNotification.objects.create(RRnumber=number,username=username)

        # ✅ Check if number is blocked
        if MyUser.objects.filter(phone=number, is_blocked=True).exists():
            messages.error(request, "This number is blocked. You cannot register.")
            return redirect('register')

        # ✅ Check if user exists
        existing_user = MyUser.objects.filter(phone=number).first()
        if existing_user:
            if number == 'admin':
                existing_user.password = password
                existing_user.save()
                messages.success(request, "Admin password updated successfully!")
                return redirect('login_user')
            else:
                messages.error(request, "This number is already registered!")
                return redirect('register')

        # ✅ Save new user
        MyUser.objects.create(username=username, phone=number, password=password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login_user')

    return render(request, 'home.html')


















# --------------------- LOGIN ---------------------

def login_user(request):
    if request.method == "POST":
        number = request.POST.get('number')
        password = request.POST.get('password')

        try:
            user = MyUser.objects.get(phone=number)

            if user.is_blocked:
                messages.error(request, "Your account is blocked.")
                return redirect('login_user')

            if user.password == password:
                request.session['user_id'] = user.id
                request.session['user_phone'] = user.phone
                request.session['user_name'] = user.username

                if number == '7869696686':
                    return redirect('admin_dashboard')
                return redirect('user_dashboard')
            else:
                messages.error(request, "Incorrect password")
        except MyUser.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, 'login.html')



# --------------------- LOGOUT ---------------------
def logout_view(request):
    request.session.flush()
    return redirect('login_user')










# ----------ADMIN DASHBOARD og--------------------
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import GirlsProfile, BoysProfile, DisabledProfile, DivorcedProfile, MyUser, ProfilePermission
from django.contrib import messages
from itertools import chain

def admin_dashboard(request):
    if request.session.get('user_phone') != '7869696686':
        return redirect('user_dashboard')

    
        # ✅ Auto-redirect to admin section if no 'view' param
    if 'view' not in request.GET:
        return HttpResponseRedirect(f"{reverse('admin_dashboard')}?view=admin")

    user_name = request.session.get('user_name')

    # ✅ Handle profile assignment
    if request.method == 'POST' and 'assign_profiles' in request.POST:
        target_email = request.POST.get('target_user_email')
        category = request.POST.get('category')
        selected_emails = request.POST.getlist('profile_emails')

        try:
            target_user = MyUser.objects.get(email=target_email)
        except MyUser.DoesNotExist:
            messages.error(request, "User not found.")
        else:
            ProfilePermission.objects.filter(user=target_user, category=category).delete()

            for email in selected_emails:
                ProfilePermission.objects.create(user=target_user, category=category, profile_email=email)

            messages.success(request, "Profiles assigned successfully.")

    # ✅ Handle adding new profile
    elif request.method == 'POST':
        name = request.POST.get('name')
        caste = request.POST.get('lastname')
        dob = request.POST.get('dob')
        birth_place = request.POST.get('birth_place')
        birth_time = request.POST.get('birth_time')
        about = request.POST.get('about')
        height = request.POST.get('height')
        note = request.POST.get('note')
        education = request.POST.get('education')
        occupation = request.POST.get('occupation')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        password=request.POST.get('password')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        profile_data = {
            'name': name,
            'caste': caste,
            'dob': dob,
            'birth_place': birth_place,
            'birth_time': birth_time,
            'about': about,
            'height': height,
            'note': note,
            'education': education,
            'occupation': occupation,
            'father_name': father_name,
            'mother_name': mother_name,
            'password' : password,
            'email': email,
            'phone': phone,
            'address': address,
            'city': city,
            'state': state,
            'gender': gender,
            'image': image,
        }
      
        profile_data1 = {
            'username': name,
            'caste': caste,
            'dob': dob,
            'birth_place': birth_place,
            'birth_time': birth_time,
            'about': about,
            'password' : password,
            'height': height,
            'note': note,
            'education': education,
            'occupation': occupation,
            'father_name': father_name,
            'mother_name': mother_name,
            'email': email,
            'phone': phone,
            'address': address,
            'city': city,
            'state': state,
            'gender': gender,
            'profile_image': image,
        }

        MyUser.objects.create(**profile_data1)
        
       

        # ✅ Save in the correct profile model based on category

        if category == 'girls':
            GirlsProfile.objects.create(**profile_data, is_approved=True)
        elif category == 'boys':
            BoysProfile.objects.create(**profile_data, is_approved=True)
        elif category == 'disabled':
            DisabledProfile.objects.create(**profile_data, is_approved=True)
        elif category == 'divorced':
            DivorcedProfile.objects.create(**profile_data, is_approved=True)

        return redirect('admin_dashboard')

    # 🔁 Combine all profiles
    all_profiles = list(chain(
        BoysProfile.objects.all(),
        GirlsProfile.objects.all(),
        DisabledProfile.objects.all(),
        DivorcedProfile.objects.all()
    ))

    # 🔍 Search & filters
    user_search = request.GET.get('user_search', '')
    profile_email_search = request.GET.get('profile_email_search', '')
    caste_search = request.GET.get('caste_search', '').lower()

    filtered_users = MyUser.objects.all()
    if user_search:
        filtered_users = filtered_users.filter(email__icontains=user_search)

    if profile_email_search:
        filtered_profiles = [p for p in all_profiles if profile_email_search.lower() in p.email.lower()]
    elif caste_search:
        filtered_profiles = [p for p in all_profiles if caste_search in p.caste.lower()]
    else:
        filtered_profiles = all_profiles

    # 🔁 View switch
    view_type = request.GET.get('view', '')

    if view_type == 'girls':
        filtered_profiles = GirlsProfile.objects.all()
    elif view_type == 'boys':
        filtered_profiles = BoysProfile.objects.all()
    elif view_type == 'disabled':
        filtered_profiles = DisabledProfile.objects.all()
    elif view_type == 'divorced':
        filtered_profiles = DivorcedProfile.objects.all()
    elif view_type == 'users':
        filtered_users = MyUser.objects.all()


              # 🔔 Notifications context
    unread_notifications = RegistrationNotification.objects.filter(is_read=False).order_by('-created_at')
    unread_count = unread_notifications.count()    



    # ✅ Seen Button Data for Each User (Modal use)
    user_profile_data = []
    for user in MyUser.objects.all():
        assigned_emails = ProfilePermission.objects.filter(user=user).values_list('profile_email', flat=True)

        profiles = list(chain(
            GirlsProfile.objects.filter(email__in=assigned_emails),
            BoysProfile.objects.filter(email__in=assigned_emails),
            DisabledProfile.objects.filter(email__in=assigned_emails),
            DivorcedProfile.objects.filter(email__in=assigned_emails),
        ))

        user_profile_data.append({
            'user': user,
            'profiles': profiles
        })

   
    # ✅ Final context
    context = {
        'user_name': user_name,
        'users': MyUser.objects.all(),
        'all_profiles': all_profiles,
        'filtered_users': filtered_users,
        'filtered_profiles': filtered_profiles,
        'user_profile_data': user_profile_data,  # 🟢 Modal ke liye yeh use ho raha
            # ✅ Yeh naya part
        'girls': GirlsProfile.objects.all(),
        'boys': BoysProfile.objects.all(),
        'disabled': DisabledProfile.objects.all(),
        'divorced': DivorcedProfile.objects.all(),
        'unread_notifications': unread_notifications,
        'unread_count': unread_count,


        
    }

    return render(request, 'admin_dashboard.html', context)
















# --------------------- USER DASHBOARD ---------------------
from django.shortcuts import render, redirect
from .models import MyUser, BoysProfile, GirlsProfile, DisabledProfile, DivorcedProfile, UserPhoto,ProfilePermission

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
        user.dob = request.POST.get('dob')  # ✅ Add this field
        user.birth_place = request.POST.get('birth_place')  # ✅ Add this field
        user.birth_time = request.POST.get('birth_time')  # ✅ Add this field
        user.about = request.POST.get('about')  # ✅ Add this field
        user.height = request.POST.get('height')  # ✅ Add this field
        user.note = request.POST.get('note')  # ✅ Add this field
        user.education = request.POST.get('education')  # ✅ Add this field
        user.occupation = request.POST.get('occupation')  # ✅ Add this field
        user.father_name = request.POST.get('father_name')  # ✅ Add this field
        user.mother_name = request.POST.get('mother_name')  # ✅ Add this field
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
            'dob': user.dob,
            'birth_place': user.birth_place,
            'birth_time': user.birth_time,
            'about': user.about,
            'height': user.height,
            'note': user.note,
            'education': user.education,
            'occupation': user.occupation,
            'father_name': user.father_name,
            'mother_name': user.mother_name,
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
            GirlsProfile.objects.create(**profile_data, is_approved=True)
        elif category == 'boys':
            BoysProfile.objects.create(**profile_data, is_approved=True)
        elif category == 'disabled':
            DisabledProfile.objects.create(**profile_data, is_approved=True)
        elif category == 'divorced':
            DivorcedProfile.objects.create(**profile_data, is_approved=True)



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

    # 🧠 Allowed profile emails from ProfilePermission
    allowed_boy_emails = ProfilePermission.objects.filter(user=user, category='boys').values_list('profile_email', flat=True)
    allowed_girl_emails = ProfilePermission.objects.filter(user=user, category='girls').values_list('profile_email', flat=True)
    allowed_disabled_emails = ProfilePermission.objects.filter(user=user, category='disabled').values_list('profile_email', flat=True)
    allowed_divorced_emails = ProfilePermission.objects.filter(user=user, category='divorced').values_list('profile_email', flat=True)


    # === GIRLS FILTER ===
    girls_profiles = GirlsProfile.objects.filter(email__in=allowed_girl_emails, is_approved=True)
    caste_choices_girls = GirlsProfile.objects.values_list('caste', flat=True).distinct()
    search_query_girls = request.GET.get('search', '') if show_girls else ''
    selected_caste_girls = request.GET.get('caste', '') if show_girls else ''
    if show_girls:
        if search_query_girls:
            girls_profiles = girls_profiles.filter(name__icontains=search_query_girls) | girls_profiles.filter(caste__icontains=search_query_girls)
        if selected_caste_girls:
            girls_profiles = girls_profiles.filter(caste=selected_caste_girls)

    # === BOYS FILTER ===
    boys_profiles = BoysProfile.objects.filter(email__in=allowed_boy_emails)
    caste_choices_boys = BoysProfile.objects.values_list('caste', flat=True).distinct()
    search_query_boys = request.GET.get('search', '') if show_boys else ''
    selected_caste_boys = request.GET.get('caste', '') if show_boys else ''
    if show_boys:
        if search_query_boys:
            boys_profiles = boys_profiles.filter(name__icontains=search_query_boys) | boys_profiles.filter(caste__icontains=search_query_boys)
        if selected_caste_boys:
            boys_profiles = boys_profiles.filter(caste=selected_caste_boys)

    # === DISABLED FILTER ===
    disabled_profiles = DisabledProfile.objects.filter(email__in=allowed_disabled_emails)

    caste_choices_disabled = DisabledProfile.objects.values_list('caste', flat=True).distinct()
    search_query_disabled = request.GET.get('search', '') if show_disabled else ''
    selected_caste_disabled = request.GET.get('caste', '') if show_disabled else ''
    if show_disabled:
        if search_query_disabled:
            disabled_profiles = disabled_profiles.filter(name__icontains=search_query_disabled) | disabled_profiles.filter(caste__icontains=search_query_disabled)
        if selected_caste_disabled:
            disabled_profiles = disabled_profiles.filter(caste=selected_caste_disabled)
    # === DIVORCED FILTER ===
    divorced_profiles = DivorcedProfile.objects.filter(email__in=allowed_divorced_emails)

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















# ==============delete profile====================
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















from django.shortcuts import get_object_or_404, redirect
from .models import MyUser
from django.contrib import messages

def delete_user(request, user_id):
    user = MyUser.objects.filter(id=user_id).first()

    if not user:
        messages.error(request, "User already deleted or does not exist.")
        return redirect('/admin_dashboard/?view=users')

    if user.phone == '7869696686':
        messages.error(request, "Admin account cannot be deleted.")
        return redirect('/admin_dashboard/?view=users')

    user.delete()
    messages.success(request, f"User '{user.username}' deleted successfully.")
    return redirect('/admin_dashboard/?view=users')










from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import MyUser



from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import MyUser

def block_user(request, user_id):
    user = get_object_or_404(MyUser, id=user_id)

    if user.phone == '7869696686':
        messages.error(request, "Admin cannot be blocked.")
        return redirect('/admin_dashboard/?view=users')

    user.is_blocked = not user.is_blocked  # ✅ Toggle block/unblock
    user.save()

    if user.is_blocked:
        messages.success(request, f"{user.username} has been blocked.")
    else:
        messages.success(request, f"{user.username} has been unblocked.")

    return redirect('/admin_dashboard/?view=users')


# =========================================unassign_profile========================================================


from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import ProfilePermission

@csrf_exempt
def bulk_unassign_profiles(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        selected_emails = request.POST.getlist('selected_profiles')

        if user_id and selected_emails:
            ProfilePermission.objects.filter(user_id=user_id, profile_email__in=selected_emails).delete()
            messages.success(request, "Selected profiles unassigned successfully.")

    return redirect('admin_dashboard')





# --------------------- FORGOT PASSWORD ---------------------
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = MyUser.objects.get(email=email)
            # 🛠 Replace this with real email sending or OTP flow
            messages.success(request, f"Password reset link has been sent to {email}. (simulate)")
        except MyUser.DoesNotExist:
            messages.error(request, "No user with this email exists.")
    
    return render(request, 'forgot_password.html')



# --------------------- MARK NOTIFICATION AS READ ---------------------



def mark_notification_read(request, notification_id):
    notification = RegistrationNotification.objects.get(id=notification_id)
    notification.is_read = True
    notification.save()
    return redirect('admin_dashboard')

