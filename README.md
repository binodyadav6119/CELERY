# CELERY
# TO RUN MAIN APPLICATION
python3.10 manage.py runserver
# TO RUN CELERY BEAT
celery -A django_celery_project.celery beat --loglevel=debug --scheduler django_celery_beat.schedulers:DatabaseScheduler
# TO RUN CELERY WORKER
celery -A django_celery_project.celery worker -l info -E
