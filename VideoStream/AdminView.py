from django.shortcuts import render
from . import pool
def AdminLogin(request):
    return render(request,"AdminLogin.html",{'msg':""})
def CheckLogin(request):
 try:
    db,cmd=pool.connectionpooling()

    emailid = request.POST['emailid']
    password = request.POST['password']
    q="select * from adminlogin where emailid='{}' and password='{}'".format(emailid,password)
    cmd.execute(q)
    row=cmd.fetchone()
    if(row):
       return render(request, "Dashboard.html",{'row':row})
    else:
       return render(request, "AdminLogin.html", {'msg': 'Please Input Valid Email Id/Password'})
 except Exception as e:
     print("error in check login",e)
     return render(request, "AdminLogin.html", {'msg': "Server Error.."})