from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})


# models에서 만든 모든걸 html에 띄워주세요