

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import *


class ImcView(TemplateView):
    template_name = 'imc2.html'
    success_url = reverse_lazy('imc2')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Imc.objects.all()
        self.db_empty = len(self.db) == 0
        if self.db_empty:
            mock_result = Imc(result='0')
            mock_result.save()

    def post(self, request):
        if str(request.method) == 'POST':
            weight = request.POST['weight']
            height = request.POST['height']
            print(weight, height)
            imc = f'{float(weight) / float(height) ** 2:.2f}'
            new_result = Imc(result=imc)
            new_result.save()
            return redirect('imc2')

    def last_object(self):
        last_index = len(self.db) - 1
        return self.db[last_index].result

    def get_context_data(self, **kwargs):
        context = super(ImcView, self).get_context_data(**kwargs)
        context['result'] = self.last_object()
        return context
