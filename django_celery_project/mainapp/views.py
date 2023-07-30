from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
# Create your views here.
def test(request):
    print("inside test")
    test_func.delay()
    return HttpResponse("DONE")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 14, minute = 5)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task5_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")