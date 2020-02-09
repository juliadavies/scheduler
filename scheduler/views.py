from django.shortcuts import render
from django.utils import timezone
from .models import Meeting
# Create your views here.
def meeting_list(request):
    current_user = request.user
    meetings = Meeting.objects.order_by('title')
    return render(request, 'scheduler/meeting_list.html', {'meetings': meetings})