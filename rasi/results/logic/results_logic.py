from ..models import Results

def get_results():
    results = Results.objects.all()
    return results

def get_result(cc): #citizenship card
    result = Results.objects.get(identification=cc)
    return result

