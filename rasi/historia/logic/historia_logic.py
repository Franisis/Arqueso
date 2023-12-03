import json
from ..models import Historia

def get_histories():
    """
    params:
        -
    returns:
        histories: list of json histories
    """
    histories = Historia.objects.all()
    return histories

def get_history_by_cc(iden):
    """
    params:
        iden: citizenship card number
    returns:
        object: history updated
    """
    history = Historia.objects.get(cc = iden)
    return history


def update_history_reason(iden, request):
    """
    params:
        iden: citizenship card number
    returns:
        object: history updated
    """
    history = get_history_by_cc(iden)
    history.motivo = json.loads(request.body)['motivo']
    history.save()
    return history






