from django.shortcuts import render

# Create your views here.
def demo1(request):
    return render(request,"demo1.html")

def demo2(request):
    d={'data':"Ramesh","fruits":["apple","banana","mango","orange"]}
    return render(request,"demo2.html")