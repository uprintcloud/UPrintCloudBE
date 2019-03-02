from django.shortcuts import render, HttpResponse
from Data.models import Jobs


def submit(requests):
    if requests.method == 'POST':
        file = requests.FILES.get('file', None)
        if not file:
            return HttpResponse('Empty file')
        job = Jobs(
            jobId='123',
            account='123',
            file_name=file.name,
            file=file,
        )
        job.save()

    return HttpResponse('Success!')

