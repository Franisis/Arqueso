from ..models import User

def get_users():
    users = User.objects.all()
    return users

def get_user(var_pk):
    user = User.objects.get(pk=var_pk)
    return user

def update_rol(user_pk, new_var):
    user = get_user(user_pk)
    user.role = new_var["role"]
    user.save()
    return user
