from django.shortcuts import render
from .forms import ImageUpload
from django.contrib import messages
from .models import Image
 
# Create your views here.
def image_upload(request):
	stu = Image.objects.all()
	if request.method=='POST':
		fm = ImageUpload(request.POST,request.FILES)
		if fm.is_valid():
			fm.save()
			messages.success(request,'Image Upload successfully!!!')
	else:
		fm = ImageUpload()
	return render(request,'home.html',{'form':fm,'st':stu})
