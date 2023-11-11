from ..models import Result

def getResults():
    queryset = Result.objects.all()
    return queryset


def createResult(form):
    result = form.save()
    result.save()
    return ()