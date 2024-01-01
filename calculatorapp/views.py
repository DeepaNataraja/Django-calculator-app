from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CalculatorForm
from .models import CalculatorOperation
import math

# Create your views here.


def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            try:
                result = eval(expression)
                CalculatorOperation.objects.create(expression=expression, result=result)
            except Exception as e:
                result = f"Error: {e}"
    else:
        form = CalculatorForm()
        result = None

    operations = CalculatorOperation.objects.all().order_by('-id')[:5]

    return render(request, 'calculator_app/calculator.html', {'form': form, 'result': result, 'operations': operations})