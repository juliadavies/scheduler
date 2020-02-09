from django.shortcuts import render

# Create your views here.
def meeting_list(request):
    return render(request, 'scheduler/meeting_list.html', {})