from django.shortcuts import render
from recipeapp import models
# Create your views here.
# 웹관련 모든 서버는 => request,response
def index(request):

    return render(request,"recipe/index.html")
#render = forword
def recipeList(request):
    page=request.GET['page']
    #reguest.getParameter("page")
    #request.POST['fd']
    curpage=int(page)
    #오라클로부터 데이터받기
    list,totalpage=models.recipeListData(curpage)

    recipe_list=[]
    for r in list:
        rr={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
        recipe_list.append(rr)
        #닥트형으로 변경 => 튜플
        #list :[] , set:{}, , tuple : ()
    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage -1) / BLOCK*BLOCK)+BLOCK

    if endPage<totalpage:
        endPage=totalpage
    return render(request,"recipe/list.html",
                  {"rd":recipe_list,"curpage":curpage,
                   "startPage":int(startPage),"endPage":int(endPage),
                   "totalpage":int(totalpage),"range":range(int(startPage),int(endPage+1))})


