from ..models import RegisterUser

def get_registers():
    registers = RegisterUser.objects.all()
    return registers
