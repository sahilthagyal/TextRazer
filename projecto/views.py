from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')


def analyze(request):
    #get the text
    djtext  = request.POST.get('text', 'default')
    status  = request.POST.get('removepunc', 'off')
    status2 = request.POST.get('capitalize', 'off')
    status3 = request.POST.get('newlineremover', 'off')
    status4 = request.POST.get('extraspaceremover','off')
    status5 = request.POST.get('charactercounter','off')

    if status =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param={'Purpose':'Removed punctuation','Analyzed_text':analyzed}
        djtext = analyzed


    if status2 == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'Purpose':'YOUR CAPITALIZED TEXT','Analyzed_text':analyzed}
        djtext = analyzed




    if status3 == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        print(analyzed)
        param = {'Purpose':'Text after removing Lines', 'Analyzed_text':analyzed}
        djtext = analyzed


    if status4 == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed = analyzed + char
        param = {'Purpose':'Text after removing extra spaces', 'Analyzed_text':analyzed}
        djtext = analyzed


    if status5 == 'on':
        analyzed = len(djtext)
        param = {'Purpose':'Number of characters are','Analyzed_text':analyzed }
    if(status !='on' and status2 !='on' and status3 !='on' and status4 !='on' and status5 !='on'):
        return HttpResponse('ERROR')


    return render(request,'removepunctuation.html',param)
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')






