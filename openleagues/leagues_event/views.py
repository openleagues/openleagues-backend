from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openleagues.leagues_event.models import LeaguesEvent
from openleagues.leagues_event.serializer import LeaguesEventSerializer


@csrf_exempt
def leagues_event_list(request):
    
    if request.method == "GET":
        events = LeaguesEvent.objects.all()
        serializer = LeaguesEventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)
