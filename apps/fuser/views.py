from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib import messages
from .models import Photo, Comment, User
from .forms import UploadPhoto, CombinePhoto
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    return redirect('/dashboard')

def dashboard(request):
    context = {
        "img": Photo.objects.all()
    }
    return render(request, "fuser/index.html", context)

def profile(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/signuplog")
    userid = request.session["id"]
    context = {
        "img": Photo.objects.filter(creator=userid)
    }
    return render(request, "fuser/profile.html", context)

def viewimage(request, id):
    if request.method == "POST":
        if "id" not in request.session:
            messages.error(request, 'You must be logged in to do that!') 
            return redirect("/signuplog")
        print("I am posting comment")
        com = request.POST["comment"]
        pid = request.POST["userid"]
        mid = request.POST["photoid"]
        uid = User.objects.get(id=pid)
        meid = Photo.objects.get(id=mid)
        postcom = Comment.objects.create(comment=com, user=uid, photo=meid)
        return redirect("/wall")
    context = {
        "img": Photo.objects.filter(id=id),
        "all_comments": Comment.objects.filter(photo=id),
    }
    return render(request, "fuser/viewimage.html", context, id)



def createimage(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/signuplog")
    form = UploadPhoto()
    if request.method == "POST":
        form = UploadPhoto(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Valid form")
            clean = form.cleaned_data
            photo1 = clean["photo1"]
            photo2 = clean["photo2"]
        else:
            print("Invalid form")
    context = {
        'form': form,
    }
    return render(request, "fuser/fuser.html", context)

def finalize(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/signuplog")
    form = CombinePhoto()
    if request.method == "POST":
        user = User.objects.get(id=request.session["id"])
        form = CombinePhoto(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Valid form")
            clean = form.cleaned_data
            newimage = clean["image"]
            newphoto = Photo.objects.create(**form.cleaned_data, imagethumb=newimage, creator=user)
            thumbroot = settings.MEDIA_ROOT_THUMB
            directory = os.listdir(thumbroot)
            print(directory)
            for p in directory:
                if p.endswith(".png"):
                    print("foundme")
                    path = os.path.join(thumbroot, p)
                    i = Image.open(path)
                    i.thumbnail((300,300))
                    i.save(path)#settings.MEDIA_ROOT + '/new' + p
            return redirect ("/profile")
        else:
            print("Invalid form")
            #return redirect("/profile")
    context = {
        'form': form,
    }
    return render(request, "fuser/finalize.html", context)

def delete(request, type, deleteid):
    delete =int(deleteid)
    if type == "comment":
            com = Comment.objects.get(id=delete)
            if request.session["id"] == com.user.id:
                Comment.objects.get(id=delete).delete()
                return redirect("/viewimage/"+ deleteid)
            else:
                messages.error(request, 'That does not belong to you!')
                return redirect("/signuplog")
    else:
        messages.error(request, 'That is illegal!')
        return redirect("/")
    # delete = Trip.objects.get(id=delete).delete()
    # print(delete)
    # return redirect("/dashboard")

# def editpage(request, id):
#     tripid = int(id)
#     if "id" not in request.session:
#         messages.error(request, 'You must be logged in to access that information') 
#         return redirect("/")
#     context = {
#         "trip": Trip.objects.get(id=tripid),
#     }
#     return render(request, "main/editpage.html", context)

# def delete(request, id, tripid):
#     hostid = int(id)
#     trip =int(tripid)
#     if "name" not in request.session and request.session["id"] != hostid:
#         messages.error(request, 'You can not do that') 
#         return redirect("/")
#     delete = Trip.objects.get(id=trip).delete()
#     print(trip)
#     return redirect("/dashboard")


# def dashboard(request):
#     form = UploadPhoto()
#     if request.method == "POST":
#         form = UploadPhoto(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             newphoto = Photo.objects.create(**form.cleaned_data)
#     context = {
#         'form': form,
#         "img": Photo.objects.all()
#     }
#     print(context['img'])
#     return render(request, "fuser/index.html", context)

