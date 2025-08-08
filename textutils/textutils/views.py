from django.http import HttpResponse
from django.shortcuts import render
# ------------------code for video (6)-----------------------------
# def index(request):
#     return HttpResponse("<h1>hello SIYA GOEL</h1> <a href='https://github.com/'>github</a>")

# def about(request):
#     return HttpResponse("about--> SIYA GOEL")


# ------------------code for video (7)-----------------------------
def index(request):
    return render(request , 'index.html')



# ------------perform multiple functionality of checkbutton at a  time-------------
def analyze(request):
    # Get input text
    djtext = request.POST.get('text', '')
    
    # Get checkbox states
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countcharacter = request.POST.get('countcharacter', 'off')

    # Store original for re-use in sequence
    analyzed = djtext
    operations = []  # To store list of applied features

    # 1. Remove punctuation
    if removepunc == 'on':
        punctuations = '''!()-[]{}:;'"\,<>./@#$%^&*_~'''
        analyzed = ''.join(char for char in analyzed if char not in punctuations)
        operations.append("Removed Punctuation")

    # 2. Convert to Uppercase
    if fullcaps == 'on':
        analyzed = analyzed.upper()
        operations.append("Converted to UPPERCASE")

    # 3. Remove Newlines
    if newlineremover == 'on':
        analyzed = ''.join(char for char in analyzed if char != '\n' and char != '\r')
        operations.append("Removed New Lines")

    # 4. Remove Extra Spaces
    if extraspaceremover == 'on':
        new_text = ""
        for index in range(len(analyzed)):
            if not (analyzed[index] == " " and index + 1 < len(analyzed) and analyzed[index + 1] == " "):
                new_text += analyzed[index]
        analyzed = new_text
        operations.append("Removed Extra Spaces")

    # 5. Count Characters
    char_count = 0
    if countcharacter == 'on':
        char_count = sum(1 for char in analyzed if char != " " and char != "\n")
        operations.append("Character Count")

    # If no option was selected
    if not operations:
        return HttpResponse("⚠️ Please select at least one operation!")

    # Send data to HTML
    params = {
        'purpose': ', '.join(operations),
        'analyzed_text': analyzed if countcharacter != 'on' else f"{analyzed}\n\nTotal characters: {char_count}"
    }

    return render(request, 'analyze.html', params)


