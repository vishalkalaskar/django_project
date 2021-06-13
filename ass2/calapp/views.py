from django.shortcuts import render

def calculation(request):

   if request.method == "POST":
     try:
        first_n = int(request.POST.get("f"))
        second_n = int(request.POST.get("s"))
        # button1 = request.POST.get("b1")
        # button2 = request.POST.get("b2")
        # button3 = request.POST.get("b3")
        # button4 = request.POST.get("b4")


        if "b1" in request.POST:
           sum = first_n + second_n
           return render(request, "calculator.html", {"Res": sum})

        elif "b2" in request.POST:
            sub = first_n - second_n
            return render(request, "calculator.html", {"Res": sub})

        elif "b3" in request.POST:
           mul= first_n * second_n
           return render(request, "calculator.html", {"Res": mul})

        if "b4" in request.POST:
            if second_n != 0:
              div = first_n / second_n
              return render(request, "calculator.html", {"Res": div})
            else:
              err= "divisor is zero"
              return render(request, "calculator.html", {"Res": err})
     except ValueError:
         err= "Incorrect value"
         return render(request,"calculator.html",{"Res":err})

   else:
      return render(request, "calculator.html")
















