# I have created this
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the Text
    djtext = request.GET.get('textarea','default')
    # Check checkbox values
    djremovepunc = request.GET.get('removepunc','Off')
    djcapitalized = request.GET.get('capitalized','off')
    djnewlineremover = request.GET.get('newlineremover','off')
    djcharcount = request.GET.get('charcounter','off')
    analyzed = djtext
    
    # Check removepunc checkbox
    if djremovepunc == 'on':
        analyzed = removepunctuation(analyzed)   
        params = {'analyzed_text' : analyzed,'purpose' : 'Removed Punctuations'}

    if djcapitalized == 'on':
        analyzed = capitalized(analyzed)
        params = {'analyzed_text' : analyzed,'purpose' : 'UPPERCASE'}
        
    if djnewlineremover == 'on':
        analyzed = newlineremover(analyzed)    
        params = {'analyzed_text' : analyzed,'purpose' : 'Removed New Lines'}
        
    if djcharcount == 'on':
        count = charcount(analyzed)
        params = {'analyzed_text' : analyzed,'charcount' : count,'purpose' : 'Count Characters'}
        return render(request,'analyze.html',params)

    if analyzed == '':
        params = {'analyzed_text' : 'Empty Input','purpose' : 'Please Enter Some Text'}
        return render(request,'analyze.html',params)

    return render(request,'analyze.html',params)

def removepunctuation(djtext):
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    return analyzed

def capitalized(djtext):
    return djtext.upper()

def newlineremover(djtext):
    analyzed = ""
    for char in djtext:
        if char != '\n':
            analyzed = analyzed + char      
    return analyzed

def charcount(djtext):
    count = 0 
    for char in djtext:
        if char != " ":
            count = count + 1
    return count