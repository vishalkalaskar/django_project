from django.shortcuts import render

def loginpage(request):
    return render(request, "loginpage.html")

def succesfull(request):
    username = request.POST.get("sname")
    pas = request.POST.get("pass")

    if username == "ravi" and pas == "kumar":
         return render(request, "succesfull.html")

    else:
       return render(request, "error.html")
#value
