from django.shortcuts import render


# Create your views here.
def index(request):
    """
    index of the page
    :param request:
    :return:
    """
    return render(request, 'dashboard.html')

