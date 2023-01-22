

from django.shortcuts import redirect
from django.http import Http404
from company.models import Job
from django.contrib import messages
from django.contrib.messages import constants

def new_job(request):

    if request.method == 'POST':

        title = request.POST.get('titulo')
        email = request.POST.get('email')
        technology_mastered = request.POST.getlist('tecnologias_domina')
        technology_study = request.POST.getlist('tecnologias_nao_domina')
        level_experience = request.POST.get('experiencia')
        data_end = request.POST.get('data_final')
        company = request.POST.get('empresa')
        status = request.POST.get('status')

        # TODO: validations

        create = Job(
            title = title,
            email = email,
            level_experience = level_experience,
            data_end = data_end,
            company = 2,
            status = status
        )

        create.save()

        # create.technology_study.add(*technology_study)
        # create.technology_mastered.add(*technology_mastered)
        #
        # create.save()
        #
        # messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        # return redirect(f'/home/company/{company}')

    elif request.method == 'GET':
        raise Http404()