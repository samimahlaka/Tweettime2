import random
from django.shortcuts import render
from django.http import HttpResponse , Http404 , JsonResponse
from .models import Tweet
from .forms import Tweetform
# Create your views here.

def home_view(request):
    return render (request, 'tweets/home.html');

def tweet_list_view(request, *args, **kwargs):
    qs =   Tweet.objects.all();
    data = [{"id" : x.id , "content" : x.content , "likes" : random.randint(0,200)} for x in qs]
    return JsonResponse (data , safe = False)

def tweet_detail_view(request, tweet_id , *args , **kwargs):

    data = {
        'id' : tweet_id
        }
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content 
    except:
        data['message'] = "Not found"
        status = 404
    
    return JsonResponse(data, status=status)
    
def tweet_create_view(request):
    if request.method == 'POST':
        form = Tweetform(request.POST)
        if form.is_valid:
            form.save()
            form = Tweetform()
            return render(request , 'tweets/forms.html' , {'form' : form})

  