from django.shortcuts import render,redirect
from libraryapp.models  import bookdb

# Create your views here.

def indexpage(req):
    return render(req,"indexpage.html")
def books(req):
    book=bookdb.objects.all()
    return render (req,"books.html",{"book":book})
def bookdetails(req,bookid):
    book=bookdb.objects.get(id=bookid)
    return render (req,"Bookdetails.html",{"book":book})
def addbooks(req):
    return render(req,"addbook.html")
def savebook(req):
    if req.method=="POST":
        t=req.POST.get('title')
        a=req.POST.get('author')
        p=req.POST.get('publication_date')
        g=req.POST.get('genre')
        ad=req.POST.get('available_copies')
        obj=bookdb(title=t,author=a,publication_date=p,genre=g,available_copies=ad)
        obj.save()
        return redirect(addbooks)
def loginpage(req):
    return render (req,"loginpage.html")