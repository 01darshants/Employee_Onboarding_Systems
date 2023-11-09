from django.shortcuts import render
import mysql.connector as sql

username = ''
Password = ''
role =''


# Create your views here.
# this is the loginaction
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
            if key == "role":
                role = value

        cursor.execute(
            "select * from users where username ='{}' and Password = '{}' and role = '{}' ".format(username, Password,role))

        user_data = cursor.fetchone()

        if user_data is None:
            return render(request, 'error.html')
        else:
            role = user_data[3]

            if role =='HR':
                return render(request, 'admin.html')
            elif role == 'Fresher':
                return render(request, 'Fresher.html')
            elif role == 'Experienced':
                return render(request, 'Experienced.html')

    return render(request, 'login.html')



