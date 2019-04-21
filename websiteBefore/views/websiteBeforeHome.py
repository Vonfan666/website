from  django.shortcuts import render_to_response,render,redirect,HttpResponse
from  websiteBefore import models
import  json

from  websiteBefore.methodAction.PageMethod import Pagination

def  image(image):
    classSayImage2 = image.path
    classSayImage3 = classSayImage2.split("\\")
    print(33, classSayImage3)
    m = classSayImage3.index("static")
    print(classSayImage3[m:])
    classImageCode = "/".join(classSayImage3[m:])
    return classImageCode

def  home(req):
    print(req.method)
    if req.method=="GET":
        list=models.New_message.objects.filter().order_by("id").reverse()
        for  a  in  list:
            print(a.id)
            print(a.title)
            print(a.content)
        print(list)

        classSay=models.ClassSay.objects.filter().order_by("id").reverse()
        classSayImageData=[]
        for   b in  classSay:
            print(b.classSayName)
            print(b.classSayContent)
            print(b.classSayImage)
            classSayImage1=b.classSayImage
            print(type(classSayImage1))
            print(classSayImage1.path)
            classSayImage2=classSayImage1.path
            classSayImage3=classSayImage2.split("\\")
            print(classSayImage3)
            m=classSayImage3.index("static")
            print(classSayImage3[m+1:])
            classImageCode="/".join(classSayImage3[m+1:])
            classSayImageData.append(classImageCode)


            # classSayImage2=classSayImage1.split("/")
            # classSayImage2="/".join(classSayImage2[1:])
            # print(classSayImage2)
            bossMessageList = models.TrickMessage.objects.all()
            print(bossMessageList[0].companyName)



            #底部学院图片以及信息
            studentsMessage=models.StudentMessage.objects.all()
            print("*********************************")
            print(studentsMessage[0])
            print(studentsMessage)

            print("-------------------------------------")
            print(studentsMessage[0].studentImage.path)
            print(type(studentsMessage[0].studentImage))



        return render(req,"home.html",{"list":list,"classSay":classSay,"classImage":classSayImageData,"bossMessage":bossMessageList,"studentsMessage":studentsMessage})

    else:
        return HttpResponse("222")


def  updateStudentMessage(req):
    print(req.POST)
    uid=int(req.POST.get("uid"))

    print(uid,type(uid))
    list=models.StudentMessage.objects.filter(id=uid+1)
    print(list)
    data={}
    for  a  in  list:
        classSayImage2=a.studentImage.path
        classSayImage3 = classSayImage2.split("\\")
        print(33,classSayImage3)
        m = classSayImage3.index("static")
        print(classSayImage3[m:])
        classImageCode = "/".join(classSayImage3[m:])
        print(classImageCode)
        data["studentName"]=a.studentName
        data["studentContent"] = a.studentContent
        data["studentImage"] = classImageCode
        data["studentMoney"] = a.studentMoney
        data["studentCompany"] = a.studentCompany
        data["studentSex"] = a.studentSex

        print(a.studentName)
        print(a.studentContent)
        print(a.studentImage)
        print(a.studentMoney)
        print(a.studentCompany)
        print(data)
    import json
    #
    # from   django.core.serializers import  serialize
    # data=serialize("json",list)
    #
    # print(data)
    data=json.dumps(data)
    return HttpResponse(data)



def  teacherTeam(req):
    data=models.teacherMessage.objects.filter(id__lt=6)

    return render_to_response("teacherTeam.html",locals())

def  studentWork(req):
    return render_to_response("studentwork.html")

def  studentWorkMessage(req):
    data={"list":[]}
    studentsMessage = models.StudentMessage.objects.all()
    i=0
    for  a  in  studentsMessage:
        data["list"].append({})
        data["list"][i]["studentName"]=a.studentName
        data["list"][i]["studentContent"]=a.studentContent
        data["list"][i]["studentImage"]=image(a.studentImage)
        data["list"][i]["studentMoney"]=a.studentMoney
        data["list"][i]["studentCompany"]=a.studentCompany
        data["list"][i]["studentSex"]=a.studentSex
        i += 1

    print(data)


    return HttpResponse(json.dumps(data))

def  onlineVideo(req):
    uid = req.GET.get("uid")
    cid = req.GET.get("cid")
    lid = req.GET.get("lid")
    currentPage=req.GET.get("pid")


    pid=int(currentPage)
    print("cid",cid)
    print(uid)
    print(type(uid))

    if uid=="0":
        uid = int(req.GET.get("uid"))
    # data=models.classification.objects.fi
        list_direction_data = models.Direction.objects.all()

        list_direction_nub = models.Direction.objects.all().values("classification__id")
        print(list_direction_nub)
        list_classification = models.Direction.objects.all().values("classification__name",
                                                                             "classification__id", "id")
        list_classification_data = models.Classification.objects.all()
        list_level = models.Level.objects.all()
        if  int(cid)==0:
            if  int(lid)==0:
                # cid_list_code=models.Direction.objects.all().values("classification__id")
                # for a  in  cid_list_code:
                #     print("--------",a)
                # print("cid_list_code",cid_list_code)
                list_video = models.Video.objects.filter(status=1)
            else:
                list_video = models.Video.objects.filter(level_id=int(lid),status=1)
        else:
            if int(lid) == 0:
                list_video = models.Video.objects.filter(classification_id=int(cid), status=1)
            else:

                list_video = models.Video.objects.filter(classification_id=int(cid),level_id=int(lid),status=1)
    else:

        uid = int(req.GET.get("uid"))
        # data=models.classification.objects.fi
        list_direction_data=models.Direction.objects.all()

        list_direction_nub = models.Direction.objects.filter(id=uid).values("classification__id")
        print(list_direction_nub)
        list_classification=models.Direction.objects.filter(id=uid).values("classification__name","classification__id","id")
        list_classification_data = models.Classification.objects.all()
        list_level = models.Level.objects.all()
        if  int(cid)==0:
            if  int(lid)==0:
                cid_list_code = models.Direction.objects.filter(id=uid).values("classification__id")
                list_cid=[]
                for a in cid_list_code:
                    cid_code=a['classification__id']
                    print(cid_code)
                    list_cid.append(cid_code)
                    print("--------", a)
                print("cid_list_code", cid_list_code)
                list_video = models.Video.objects.filter(status=1,classification_id__in=list_cid)
            else:
                list_video = models.Video.objects.filter(level_id=int(lid),status=1)
        else:
            if int(lid) == 0:
                list_video = models.Video.objects.filter(classification_id=int(cid),status=1)
            else:

                list_video = models.Video.objects.filter(classification_id=int(cid),level_id=int(lid),status=1)



    print(type(uid),type(cid),type(lid))
    print(uid,cid,lid)
    print("list_video",list_video)
    textNumber=len(list_video)
    pageNumber=len(list_video)

    classPage=Pagination(pageNumber,pid)  #实例化

    pageNub=classPage.foot_all_page()   #底部页码
    print(pageNub)
    if  pid>classPage.all_page():
        pid = classPage.all_page()
        if classPage.all_page()==0:
            pid=1

    list_video=list_video[(pid-1)*classPage.currentPageNum:pid*classPage.currentPageNum]
    print(list_video)
    print(pid)

    first_page=pid-1  #上一页
    if first_page==0:
        first_page=1

    last_page=pid+1   #下一页
    if last_page>=classPage.all_page():
        last_page=classPage.all_page()

    totalPage=classPage.all_page()  #总页数
    if  classPage.all_page() ==0:
        totalPage=1


    return render_to_response("onlineVideo.html",locals(),{"uid":uid,"cid":int(cid),"lid":int(lid),'pid':pid})



def  aboutSelf(req):
    return render(req,"aboutself.html")




