from django.shortcuts import render
from django.http import HttpResponse
from .models import Technology, Company, Job
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants


def new_company(request):

    if request.method == 'GET':
        techs = Technology.objects.all()
        return render(request, 'new_company.html', {'techs': techs})

    elif request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        city = request.POST.get('cidade')
        address = request.POST.get('endereco')
        type_market = request.POST.get('nicho')
        feature_company = request.POST.get('caracteristicas')
        technology = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

        if (len(name.strip()) == 0 or len(email.strip()) == 0 or len(city.strip()) == 0 or len(
                address.strip()) == 0 or len(type_market.strip()) == 0 or len(feature_company.strip()) == 0 or (not logo)):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/new_company')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/home/new_company')

        if type_market not in [i[0] for i in Company.choices_type_market]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/home/new_company')

        company = Company(
            logo=logo,
            name=name,
            email=email,
            city=city,
            address=address,
            type_market=type_market,
            feature_company=feature_company
        )
        company.save()

        company.technology.add(*technology)
        company.save()

        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso.')
        return redirect('/home/new_company')

def companies(request):
    tecnologies_filter = request.GET.get('tecnologias')
    name_filter = request.GET.get('nome')

    companies = Company.objects.all()
    tecnologies = Technology.objects.all()

    if tecnologies_filter:
        companies = companies.filter(technology = tecnologies_filter)

    if name_filter:
        companies = companies.filter(name__icontains = name_filter)

    return render(request, 'companies.html', {
        'companies': companies,
        'tecnologies': tecnologies
    })

def destroy(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa deletada com sucesso.')
    return redirect('/home/companies')

def findOne(request, id):
    company = get_object_or_404(Company, id = id)
    companies = Company.objects.all()
    technologies = Technology.objects.all()
    jobs = Job.objects.filter(company = id)
    return render(request, 'company_view.html', {
        'company': company,
        'technologies': technologies,
        'companies': companies,
        'jobs': jobs
    })