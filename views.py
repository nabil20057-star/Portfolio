from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})
