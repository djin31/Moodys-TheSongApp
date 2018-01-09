# Libraries for mood detection #
import httplib, urllib, base64, json, operator, sys
from collections import Counter
from bs4 import BeautifulSoup as BS
from random import shuffle
import time
from moodDetection import work

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from SongsApp.forms import UploadFileForm
import datetime

def playlist(request):
	if request.method == 'POST':
            # form = UploadFileForm(request.POST, request.FILES)
            # if form.is_valid():
	        search_id = request.POST.get('file', None)
	        try :
	        	(finalList, mood) = work(search_id)
	        except Exception as e :
	        	finalList = []
	        	mood = ""

                #inImg = request.FILES["file"].read()
	        #encoded = base64.b64encode(inImg)
	        #mime = "image/jpg"
	        #mime = mime + ";" if mime else ";"
	        #input_image = "data:%sbase64,%s" % (mime, encoded)
	        return render(request, 'playlist.html', { 'playList' : finalList, 'mood' : mood})
            #else :
            #    return HttpResponse("Server Error")
	else :
	    return HttpResponseRedirect('/index/')

def index(request):
    form = UploadFileForm()
    return render(request, 'index.html', {'form' : form})
