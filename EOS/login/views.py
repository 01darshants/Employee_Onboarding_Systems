from django.shortcuts import render
import mysql.connector as sql

username = ''
Password = ''


# Create your views here.
def loginaction(request):
    global username, Password
    if request.method == "POST":
        sqlconnection = sql.connect(host="localhost", user="dts", passwd="dts", database='onboarding')
        cursor = sqlconnection.cursor()
        userinfo = request.POST
        for key, value in userinfo.items():
            if key == "username":
                username = value
            if key == "Password":
                Password = value

        cursor.execute(
            "select * from users where username ='{}' and Password = '{}'".format(username, Password))

        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, "welcome.html")

    return render(request, 'login.html')



