from django.shortcuts import render
import mysql.connector as sql

username = ''
Password = ''



# Create your views here.
# this is the loginaction
def home(request):
    return render(request,'home.html')


def loginaction(request):
    global username, Password,role
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
            "select * from users where username ='{}' and Password = '{}' ".format(username, Password))

        user_data = cursor.fetchone()
        # print(user_data)
        if user_data is None:
            return render(request, 'error.html')
        else:
            role = user_data[3]
            if role =='HR':
                return render(request, 'admin.html')
            elif role == 'Candidate':
                return render(request, 'Fresher.html')

    return render(request, 'login.html')



