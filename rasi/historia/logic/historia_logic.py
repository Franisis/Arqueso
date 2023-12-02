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
        history: json history
    """
    history = Historia.objects.get(cc = iden)
    return history


