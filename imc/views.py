

from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def imc(request):
    return render(request, 'imc.html')


def imc_result(request):

    weight = request.GET['weight']
    height = request.GET['height']
    imc_calculus = f'{float(weight) / float(height) ** 2:.2f}'

    context = {
        'weight': weight,
        'height': height,
        'imc': imc_calculus
    }

    return render(request, 'imc_result.html', context=context)
