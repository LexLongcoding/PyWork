from django.shortcuts import render, redirect


def index(request):
    context = {
        'locations' : ['San Jose', 'Seattle', 'Chicago', 'Online'],
        'languages' : ['Python', 'JavaScript', 'C#', 'Java']
    }
    return render(request, 'form.html', context)

def process(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
            'name': request.POST['name'], 
            'lang': request.POST['language'],
            'loc': request.POST['location']       
        }
    return redirect('/result')

def result(request):
        context = {
            'result': request.session['result']
        }
        return render(request, 'result.html', context)
    

# Create your views here.
