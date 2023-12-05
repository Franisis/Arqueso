from ..models import User

def get_users():
    users = User.objects.all()
    return users

def get_user(user_pk):
    user = User.objects.get(pk=user_pk)
    return user

def get_user_by_identification(user_pk):
    user = User.objects.get(identification=user_pk)
    return user

def update_rol(user_pk, new_role):
    user = get_user_by_identification(user_pk) #Aqui es donde se muere
    user.role = new_role
    user.save()
    return user
