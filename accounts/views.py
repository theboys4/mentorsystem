from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *




def home(request):


	return render(request,'accounts/last.html')

def acb(request):
	if request.method == 'POST':
		name = request.POST['name']
		reg= request.POST.get('reg')
		roll= request.POST.get('roll')
		post = Student(name = name, reg = reg,roll = roll)
		post.save()
		print('hi')
		akjh = Student.objects.all()
		return render(request,'accounts/abc.html',{'akjh':akjh})

			

	


def cont(request):
	return render(request,'accounts/dam.html')


def abc(request):
	akjh = Student.objects.all()

	return render(request,'accounts/abc.html',{'akjh':akjh})
def login(request):
	if request.method == 'POST':
		mid = request.POST['mid']
		pwd = request.POST['pwd']
		lt = Login.objects.all()
		lis = []
		for i in lt:
			lis.append(i.mid)
		if mid in lis:
			logm = Login.objects.get(mid = mid)
			logp = logm.pwd
			if pwd == logp :
				
				akjh = Sbio.objects.filter(mid=logm.id)
				
				

				return render(request,'accounts/abc.html',{'akjh':akjh})
				
			else:
				return HttpResponse('login faild')
		else:
			return HttpResponse('login faild')
def bd(request,pk1):
	pk2 = Sbio.objects.get(id = pk1)



	return render(request,'accounts/temp.html',{'pk2':pk2})
def ach(request,pk3):
	if request.method == 'POST':
		ach2 = request.POST['ach']
		ach1 = Sbio.objects.get(id = pk3)
		ach1.ach = ach2
		ach1.save()
		pk2 = Sbio.objects.get(id = pk3)
		return render(request,'accounts/temp.html',{'pk2':pk2})

def rm(request,pk4):
	if request.method == 'POST':
		rm2 = request.POST['rm']
		rm1 = Sbio.objects.get(id = pk4)
		rm1.rm = rm2
		rm1.save()
		pk2 = Sbio.objects.get(id = pk4)
		return render(request,'accounts/temp.html',{'pk2':pk2})

def sam(request):
	return render(request,'accounts/dam.html')



	

