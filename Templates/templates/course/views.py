from django.shortcuts import render

# Create your views here.
def courseList(req):
    return render(req, 'course/django.html')

def FastAPI(req):
    return render(req, 'course/fastapi.html')



