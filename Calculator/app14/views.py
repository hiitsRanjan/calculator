from django.shortcuts import render

def calculate(request):
    return render(request,"index.html")

def count(request):
    no1 = int(request.POST.get("t1"))
    no2 = int(request.POST.get("t2"))
    val = request.POST.get("b1")
    result=0
    if val == "add":
        result = no1+no2
    elif val == "sub":
        result = no1-no2
    elif val == "mul":
        result = no1*no2
    else:
        result = no1/no2


    return render(request,"index.html",{"res":result})