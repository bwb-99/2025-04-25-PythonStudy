from django.shortcuts import render
from recipeapp import models
# Create your views here.
# 웹관련 모든 서버는 => request,response
def index(request):

    return render(request,"recipe/index.html")
#render = forword


