from  django.shortcuts import redirect,render_to_response,render,HttpResponse


def  home1(req):
    print(req.method)
    if req.method=="GET":
        return HttpResponse("99")
    else:
        return HttpResponse("222")