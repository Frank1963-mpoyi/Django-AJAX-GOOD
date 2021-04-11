from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentRegistration
from .models import User
from django.views.decorators.csrf import csrf_exempt



def home(request):
    form = StudentRegistration()#(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = StudentRegistration()
    
    student = User.objects.all()    
    template_name = 'blog/index.html'
    context = {'form': form, 'student': student}
    return render(request, template_name, context)



@csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            usr = User(name = name, email= email, password= password)
            usr.save()
            
            stud = User.objects.values()
            # print("\n")
            # print(stud)
            student_data = list(stud)
            
            return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})
        
        
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status':0})