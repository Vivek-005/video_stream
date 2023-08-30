from django.shortcuts import render
from . import pool
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import  JsonResponse
import os

@xframe_options_exempt
def EpisodeInterface(request):
    return render(request,"EpisodeInterface.html")

@xframe_options_exempt
def SubmitEpisode(request):
    try:
        db,cmd=pool.connectionpooling()
        categoryid = request.POST['categoryid']
        showid = request.POST['showid']
        episodenumber = request.POST['episodenumber']
        description=request.POST['description']
        poster=request.FILES['poster']
        trailer = request.FILES['trailer']
        video = request.FILES['video']
        q="insert into episodes(categoryid,showid,episodenumber,description,poster,trailer,video)values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryid,showid,episodenumber,description,poster.name,trailer.name,video.name)
        print(q)
        cmd.execute(q)
        db.commit()
        # wb(write bytes)
        G = open("G:/VideoStream/assets/" + poster.name, "wb")
        for chunk in poster.chunks():
         G.write(chunk)
        G.close()

        G = open("G:/VideoStream/assets/" + trailer.name, "wb")
        for chunk in trailer.chunks():
         G.write(chunk)
        G.close()

        G = open("G:/VideoStream/assets/" + video.name, "wb")
        for chunk in video.chunks():
         G.write(chunk)
        G.close()
        db.close()
        return render(request, "EpisodeInterface.html", {'status': True})
    except Exception as e:
        return render(request, "EpisodeInterface.html", {'status': False})

@xframe_options_exempt
def DisplayAll(request):
    try:
          db, cmd = pool.connectionpooling()
          q = "select * from episodes"
          cmd.execute(q)
          rows = cmd.fetchall()
          return render(request, "DisplayAllEpisode.html", {'rows': rows})
    except Exception as e:
          print("error in showall",e)
          return render(request, "DisplayAllEpisode.html", {'rows': []})

@xframe_options_exempt
def EpisodeById(request):
    try:
          eid=request.GET['eid']
          db, cmd = pool.connectionpooling()
          q = "select * from episodes where episodeid={}".format(eid)
          cmd.execute(q)
          print(q)
          row = cmd.fetchone()
          db.close()
          return render(request, "EpisodeById.html", {'row': row})
    except Exception as e:
          print("ERROR!@#",e)
          return render(request, "EpisodeById.html", {'row': []})

@xframe_options_exempt
def EditDeleteEpisodeData(request):
    try:
      btn = request.GET['btn']
      if (btn == "Edit"):
        categoryid = request.GET['categoryid']
        showid = request.GET['showid']
        episodeid=request.GET['episodeid']
        episodenumber = request.GET['episodenumber']
        description=request.GET['description']
        db, cmd = pool.connectionpooling()
        q="update episodes set categoryid='{}',showid='{}',episodenumber='{}',description='{}' where episodeid='{}'".format(categoryid,showid,episodenumber,description,episodeid)
        cmd.execute(q)
        db.commit()
        db.close()
      elif (btn == "Delete"):
        db, cmd = pool.connectionpooling()
        episodeid = request.GET['episodeid']
        q = "delete from episodes where episodeid={} ".format(episodeid)
        cmd.execute(q)
        db.commit()
        db.close()
      return render(request,"EpisodeById.html", {'status': True})
    except Exception as e:
      print("error!!!", e)
      return render(request,"EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditEpisodePoster(request):
  try:
      db, cmd = pool.connectionpooling()

      episodeid = request.POST['episodeid']
      filename = request.POST['filename']
      poster = request.FILES['poster']
      q = "update episodes set poster='{0}' where episodeid={1}".format(poster.name, episodeid)
      print(q)
      cmd.execute(q)
      db.commit()
      # wb(write bytes)
      G = open("G:/VideoStream/assets/" + poster.name, "wb")
      for chunk in poster.chunks():
          G.write(chunk)
      G.close()
      os.remove("G:/VideoStream/assets/" + filename)
      db.close()
      return render(request, "EpisodeById.html", {'status': True})

  except Exception as e:
      print("error in edit poster", e)
      return render(request, "EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditEpisodeTrailer(request):
 try:
    db, cmd = pool.connectionpooling()

    episodeid=request.POST['episodeid']
    filename = request.POST['filename']
    trailer=request.FILES['trailer']
    q="update episodes set trailer='{0}' where episodeid={1}".format(trailer.name,episodeid)
    print(q)
    cmd.execute(q)
    db.commit()
    #wb(write bytes)
    G=open("G:/VideoStream/assets/"+trailer.name,"wb")
    for chunk in trailer.chunks():
        G.write(chunk)
    G.close()
    os.remove("G:/VideoStream/assets/"+filename)
    db.close()
    return render(request,"EpisodeById.html",{'status':True})

 except Exception as e:
    print("error in edit trailer",e)
    return render(request, "EpisodeById.html",{'status':False})

@xframe_options_exempt
def EditEpisodeVideo(request):
 try:
    db, cmd = pool.connectionpooling()

    episodeid=request.POST['episodeid']
    filename = request.POST['filename']
    video=request.FILES['video']
    q="update episodes set video='{0}' where episodeid={1}".format(video.name,episodeid)
    print(q)
    cmd.execute(q)
    db.commit()
    #wb(write bytes)
    G=open("G:/VideoStream/assets/"+video.name,"wb")
    for chunk in video.chunks():
        G.write(chunk)
    G.close()
    os.remove("G:/VideoStream/assets/"+filename)
    db.close()
    return render(request,"EpisodeById.html",{'status':True})

 except Exception as e:
    print("error in edit video",e)
    return render(request, "EpisodeById.html",{'status':False})

