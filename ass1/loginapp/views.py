from django.shortcuts import render

def loginpage(request):
 if request.method =="POST":
    username=request.POST.get("sname")
    pas = request.POST.get("pass")
    list = request.POST.get("list")
    b1 = request.POST.get("b1")
    b2 = request.POST.get("b2")
    b3 = request.POST.get("b3")


    if username == "Ravi" and pas == "ravi1234@" and list == b1:
         mass1 = "Admin Page"
         return render(request, "login.html", {"massage": "valid","mass1": mass1})

    elif username == "Ravi" and pas == "kumar@123" and list == b2:
        mass2 = "Employee Page"
        return render(request, "login.html", {"massage":"valid","mass1": mass2})
    elif username == "Ravi" and pas == "ravikumar@123" and list == b3:
        mass3 = "Customer Page"
        return render(request, "login.html", {"massage": "valid","mass1":mass3})
    else:
        return render(request, "login.html", {"massage": "invalid"})



 else:
    return render(request, "login.html")
 # the above else part is similar to the
 #if request.method =="get":
 # return render(request,"login.html")
