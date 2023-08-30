from django.shortcuts import render
from . import pool
import os
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import  JsonResponse

@xframe_options_exempt
def ShowInterface(request):
    return render(request,"ShowInterface.html")

@xframe_options_exempt
def SubmitShow(request):
  try:
      db,cmd=pool.connectionpooling()
      categoryid=request.POST['categoryid']
      showname=request.POST['showname']
      showdescription=request.POST['showdescription']
      showtype=request.POST['showtype']
      showrating=request.POST['showrating']
      showyear=request.POST['showyear']
      showartist=request.POST['showartist']
      shownew=request.POST['shownew']
      showepisode=request.POST['showepisode']
      showstatus=request.POST['showstatus']
      showposter=request.FILES['showposter']
      showtrailer=request.FILES['showtrailer']
      showvideo=request.FILES['showvideo']
      q="insert into shows(categoryid,showname,showdescription,showtype,showrating,showyear,showartist,shownew,showepisode,showstatus,showposter,showtrailer,showvideo) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(categoryid,showname,showdescription,showtype,showrating,showyear,showartist,shownew,showepisode,showstatus,showposter.name,showtrailer.name,showvideo.name)
      print(q)
      cmd.execute(q)
      db.commit()
      #wb(write bytes)

      G=open("G:/VideoStream/assets/"+showposter.name,"wb")
      for chunk in showposter.chunks():
          G.write(chunk)
      G.close()

      G = open("G:/VideoStream/assets/" + showtrailer.name, "wb")
      for chunk in showtrailer.chunks():
          G.write(chunk)
      G.close()

      G = open("G:/VideoStream/assets/" + showvideo.name, "wb")
      for chunk in showvideo.chunks():
          G.write(chunk)
      G.close()

      db.close()
      return render(request, "ShowInterface.html",{'status':True})
  except Exception as e:
      return render(request, "ShowInterface.html", {'status':False})

@xframe_options_exempt
def ShowAll(request):
    try:
          db, cmd = pool.connectionpooling()
          q = "select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid)  from shows S"
          cmd.execute(q)
          rows = cmd.fetchall()
          return render(request, "DisplayAllShow.html", {'rows': rows})
    except Exception as e:
          print("error in showall",e)
          return render(request, "DisplayAllShow.html", {'rows': []})

@xframe_options_exempt
def ShowById(request):
    try:
          sid=request.GET['sid']
          db, cmd = pool.connectionpooling()
          q = "select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid)  from shows S where S.showid={}".format(sid)
          cmd.execute(q)
          print(q)
          row = cmd.fetchone()
          db.close()
          return render(request, "ShowById.html", {'row': row})
    except Exception as e:
          print("ERROR!@#",e)
          return render(request, "ShowById.html", {'row': []})

@xframe_options_exempt
def EditDeleteShowData(request):
    try:
       btn=request.GET['btn']
       if(btn=="Edit"):
          categoryid = request.GET['categoryid']
          showid = request.GET['showid']
          showname = request.GET['showname']
          showdescription=request.GET['showdescription']
          showtype=request.GET['showtype']
          showrating = request.GET['showrating']
          showyear = request.GET['showyear']
          showartist = request.GET['showartist']
          shownew=request.GET['shownew']
          showepisode = request.GET['showepisode']
          showstatus = request.GET['showstatus']
          db, cmd = pool.connectionpooling()
          q="update shows set categoryid='{}',showname='{}',showdescription='{}',showtype='{}',showrating='{}',showyear='{}',showartist='{}',shownew='{}',showepisode='{}',showstatus='{}' where showid='{}'".format(categoryid,showname,showdescription,showtype,showrating,showyear,showartist,shownew,showepisode,showstatus,showid)
          cmd.execute(q)
          db.commit()
          db.close()
       elif(btn=="Delete"):
          db, cmd = pool.connectionpooling()
          showid = request.GET['showid']
          q="delete from shows where showid={} ".format(showid)
          cmd.execute(q)
          db.commit()
          db.close()
       return render(request, "ShowById.html", {'status': True})
    except Exception as e:
       print("error!!!",e)
       return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditPoster(request):
  try:
      db, cmd = pool.connectionpooling()

      showid = request.POST['showid']
      filename = request.POST['filename']
      showposter = request.FILES['showposter']
      q = "update shows set showposter='{0}' where showid={1}".format(showposter.name, showid)
      print(q)
      cmd.execute(q)
      db.commit()
      # wb(write bytes)
      G = open("G:/VideoStream/assets/" + showposter.name, "wb")
      for chunk in showposter.chunks():
          G.write(chunk)
      G.close()
      os.remove("G:/VideoStream/assets/" + filename)
      db.close()
      return render(request, "ShowById.html", {'status': True})

  except Exception as e:
      print("error", e)
      return render(request, "ShowById.html", {'status': True})

@xframe_options_exempt
def EditTrailer(request):
 try:
    db, cmd = pool.connectionpooling()

    showid=request.POST['showid']
    filename = request.POST['filename']
    showtrailer=request.FILES['showtrailer']
    q="update shows set showtrailer='{0}' where showid={1}".format(showtrailer.name,showid)
    print(q)
    cmd.execute(q)
    db.commit()
    #wb(write bytes)
    G=open("G:/VideoStream/assets/"+showtrailer.name,"wb")
    for chunk in showtrailer.chunks():
        G.write(chunk)
    G.close()
    os.remove("G:/VideoStream/assets/"+filename)
    db.close()
    return render(request,"ShowById.html",{'status':True})

 except Exception as e:
    print("error",e)
    return render(request, "ShowById.html",{'status':True})

@xframe_options_exempt
def EditVideo(request):
 try:
    db, cmd = pool.connectionpooling()

    showid=request.POST['showid']
    filename = request.POST['filename']
    showvideo=request.FILES['showvideo']
    q="update shows set showvideo='{0}' where showid={1}".format(showvideo.name,showid)
    print(q)
    cmd.execute(q)
    db.commit()
    #wb(write bytes)
    G=open("G:/VideoStream/assets/"+showvideo.name,"wb")
    for chunk in showvideo.chunks():
        G.write(chunk)
    G.close()
    os.remove("G:/VideoStream/assets/"+filename)
    db.close()
    return render(request,"ShowById.html",{'status':True})

 except Exception as e:
    print("error",e)
    return render(request, "ShowById.html",{'status':True})

@xframe_options_exempt
def DisplayAllShowJSON(request):
    try:
        cid=request.GET['cid']
        db, cmd = pool.connectionpooling()
        q="select * from shows where categoryid={}".format(cid)
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)