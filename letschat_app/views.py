from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def chatroom(request,room):
    context={
        "roomname":room
    }
    return render(request,'chatroom.html',context=context)