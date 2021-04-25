from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=this_passcard)
    for visit in this_passcard_visits:
      visit.duration = visit.format_duration()
      visit.is_strange = visit.is_visit_long()
    
    context = {
        "passcard": this_passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
