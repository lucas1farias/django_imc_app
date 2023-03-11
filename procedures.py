

def install():
    """
    pip install django==3.2.13
    django-admin startproject config .
    django-admin startapp imc
    django-admin startapp imc2
    """


def settings():
    """
    * O primeiro aplicativo é para calcular imc usando requisição GET
    * O segundo aplicativo é para calcular imc usando requisição POST

    INSTALLED_APPS = [
        'imc',
        'imc2'
    ]

    TEMPLATES = [
        {
            'DIRS': ['templates'],
        },
    ]
    """


def imc_pp_urls():
    """
    * Configuração dos 2 apps para terem seus próprios módulos "urls"
    * Fazer o registrado de cada app por vez

    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('imc', include('imc.urls')),
        path('imc2', include('imc2.urls')),
    ]
    """


# Do primeiro app
def imc_pa_urls():
    """
    from django.urls import path
    from .views import *


    urlpatterns = [
        path('', imc, name='index'),
        path('imc-app-result', imc_result, name='imc-app-result'),
    ]
    """


# Do segundo app
def imc2_pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('imc2', Imc.as_view(), name='imc2')
    ]
    """


def imc_views():
    """
    from django.shortcuts import render


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
    """


def template_imc_html():
    """
    <form action="{% url 'imc-app-result' %}" method="get">
        <input type="text" name="weight" placeholder="Peso" required>
        <input type="text" name="height" placeholder="Altura" required>
        <input type="submit" value="Calcular">
    </form>
    """


def template_imc_result_html():
    """
    <div id="result">IMC do peso {{ weight }} com a altura {{ height }}: {{ imc }}</div>
    <button><a href="{% url 'index' %}">Retornar</a></button>
    """
