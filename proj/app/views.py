from django.shortcuts import render,redirect
from app.forms import SignupForm, MusicUploadForm,EmailForm
from app.models import MusicFile,MyUser
from django.contrib.auth.decorators import login_required
from app.thread import CustomThread
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


# Create your views here.

@login_required
def home(request):
    public_musics = MusicFile.objects.filter(Q(visibility='Public')).all()
    private_music = MusicFile.objects.filter(Q(visibility='Private') & Q(uploader=request.user)).all()
    protected_music = MusicFile.objects.filter(Q(visibility='Protected') & Q(emails=request.user)).all()


    musics = list(
            sorted(
                chain(public_musics,private_music,protected_music),
                key=lambda objects: objects.title,
            ))
    
    paginator  = Paginator(musics, 2 ,orphans=1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context ={
        'all_musics':page_obj,
        'private_music':private_music,
    }
    return render(request,'app/index.html',context=context)

@login_required
def upload(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        form2=EmailForm(request.POST)
        if form.is_valid() and form2.is_valid():
            em_list = form2.cleaned_data['emails']
            object=form.save(commit=False)
            object.uploader = request.user
            object.save()
            if object.visibility=='Protected':
                object.emails.add(request.user)
                CustomThread(object,em_list).start()
            return redirect('home')
    else:
        form = MusicUploadForm()
        form2=EmailForm()
    return render(request,'app/upload.html',{'form':form,'form2':form2} )

def delete(request,id):
    obj = get_object_or_404(MusicFile, pk=id)
    obj.delete()
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'app/signup.html',{'form':form})
