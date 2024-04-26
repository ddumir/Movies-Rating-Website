from .models import signup
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,auth
from .models import movies
from .models import gonor
from django.db import connection

def user_signup(request):
    msg={"msg":""}
    if request.method == "POST":
         if request.POST.get("username") and request.POST.get("email") and request.POST.get("password") and request.POST.get("password2"):

            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")

            if password == password2:
                # Create and save a new user in the database
                my_user = signup(username=username, email=email, password=password)
                my_user.save()
                return redirect('login')
            
            else:
                msg={"msg":"Your passwords should be the same"}
            

        # Redirect to the login page
        # Assuming you have a 'login' URL pattern defined

    return render(request, "signup.html",msg)

def login(request):
    msg={"msg":""}
    if request.method == "POST":
        if request.POST.get("username") and request.POST.get("password"):
            username = request.POST.get("username")
            pass1 = request.POST.get("password")
            print(username)
            print(pass1)
            rec=signup.objects.all()
        
            flag=0
            for r in rec:
                if (username==r.username and pass1==r.password):
                    msg={"msg":"login ok"}
                    flag=1
            if flag==1:
                return redirect('home')
            else:
                print("incorrect")
                msg={"msg":"Password Incorrect!!"}
    return render(request,"login.html",msg)
        

def home(request):

    show_modal = True
    return render(request,"home.html", {'show_modal': show_modal})
def news(request):
    return render(request,"news.html")
# GENRES
def genres(request):
    return render(request,"genres.html")

def g_action(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select m_img from movies where genre='action'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_action.html',{"ac":ac})


def g_advanture(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='adventure'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_advanture.html',{"ac":ac})


def g_comedy(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='comedy'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_comedy.html',{"ac":ac})


def g_doc(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='documentary'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_doc.html',{"ac":ac})


def g_drama(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='drama'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_drama.html',{"ac":ac})


def g_horror(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='horror'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_horror.html',{"ac":ac})


def g_romance(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='romance'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_romance.html',{"ac":ac})


def g_sifi(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='sci-fi'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_sifi.html',{"ac":ac})


def g_thriller(request):
    ac={}
    cursor=connection.cursor()
    cursor.execute("select * from movies where genre='thriller'")
    ac=cursor.fetchall()
    print(ac)
    return render(request,'g_thriller.html',{"ac":ac})


# Side nav Page render
def anime(request):
    return render(request,"anime.html")
def tvshows(request):
    return render(request,"tvshow.html")
def about(request):
    return render(request,'about.html')




'''
# Movies Pages
# this is left not complited yet
def m_display(request):
    m = movies.objects.all()
    #if m == request.GET.get("m_name"):
    if request.GET.get("name") == request.GET.get("m_name"):
        t = "m_name"
    
    return render(request, "m_display.html", {"t": t})

def m_display(request):
    m_name = request.GET.get("name")
    t = None  # Set a default value for t
    
    if m_name:
        # Filter movies based on the user input
        m = movies.objects.filter(m_name=m_name).first()

        if m:
            # If a movie is found, set t to the movie's name
            t = m.m_name

    return render(request, "m_display.html", {"t": t})

    def m_display(request):
 #   Data = request.data
    id = request.GET.get('name')

    try:
        m_display = movies.objects.get(m_name=id)
        if m_display:
            return render('m_display.html',context = m_display)
        else:
            return('404.html')
    except:
        print(" ")
'''

def m_display(request):
    id_param = request.GET.get('id')

    try:
        record = movies.objects.filter(m_name=id_param).values()
        #all_rec = movies.objects.filter(m_name=record).values()
        # If a record with the matching m_name is found, render the m_display.html page
        # {'all_rec':all_rec}
        return render(request, 'm_display.html', {'record': record},)
    except movies.DoesNotExist:
        # Handle the case where the record doesn't exist or the id doesn't match
        return redirect('home.html')  # Redirect to another page if needed






# Rough work
def admovies(request):
    if request.POST.get("m_name") and request.POST.get("year") and request.POST.get("hour") and request.POST.get("image") and request.POST.get("link") and request.POST.get("disc") and request.POST.get("director") and request.POST.get("genre"):
        rec=movies(m_name = request.POST.get("m_name"),m_year = request.POST.get("year"), m_hour = request.POST.get("hour"), m_img = request.POST.get("image"),m_link = request.POST.get("link"),disc = request.POST.get("disc"),director = request.POST.get("director"),genre=request.POST.get("genre"))
        rec.save()
    return render(request,"admovies.html")
def adgonor(request):
    if request.POST.get("movie_name") and request.POST.get("go_name"):
        rec=gonor(movie_name=request.POST.get("movie_name"),go_name=request.POST.get("go_name"))
        rec.save()
    return render(request,"adgonor.html")