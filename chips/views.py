from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ChipStatus
import re

STATUS_FORMAT = '''<?xml version="1.0" encoding="UTF-8" ?>
<clients>
    <name>{name}</name>
    <upload>{lost}</upload>
    <chipId>{chip}</chipId>
    <email>{email}</email>
</clients>
'''

@login_required
def activate(request):
    user = request.user
    (status, created) = ChipStatus.objects.get_or_create(user=user)
    chip = request.POST['chip']
    chip = re.sub(r'[^a-zA-Z0-9_-]', '', chip)
    status.activate(chip)
    return HttpResponse('Recovery Initiated')

@login_required
def deactivate(request):
    user = request.user
    user.chipstatus.deactivate()
    return HttpResponse('Recovery Status Reset')

def status(request):
    username = request.GET['username']
    chip = ChipStatus.objects.get(user__username=username)

    data = {'name': chip.user.username,
        'lost': chip.lost,
        'chip': chip.chip,
        'email': chip.user.email}

    return HttpResponse(STATUS_FORMAT.format(**data), content_type="text/xml")
