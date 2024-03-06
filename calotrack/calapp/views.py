from django.shortcuts import render,redirect,HttpResponse
from calapp.models import calmodel,savemodel,finalmodel
from calapp.forms import caloform,saveform

# Create your views here.

def favour(request,pk=0):
        is_fav=False
        res=request.POST.get("food_id")
        var=calmodel.objects.get(id=res)
        if var:
            is_fav=True
        return is_fav
def calview(request):
    print(favour(request))
    isfav=favour(request)
    cal_model=calmodel.objects.all()
        # print("should have done")
    
    return render (request,'index.html',{'cal_model':cal_model,"is_fav":isfav})

def addcontent(request):
    # cal_model=calmodel.objects.all()
    calo_form=caloform()
    if request.method=="POST":
        calo_form=caloform(request.POST)
        if calo_form.is_valid():
            calo_form.save()
        print("should be updated")

    return render(request,'addcontent.html',{'caloform':calo_form})


# def trackcontent(request):
#     form1=calform()
#     consumed_food=caloform()
#     food_item={}
#     save_model_instance=[]
#     saved_data={}
#     if request.method=="POST":
#         form1=calform(request.POST)
#         if form1.is_valid():
#             print("valid")
#             food_name = form1.cleaned_data['name']
#             print(food_name)
#             # to filter the data
#             food_item = calmodel.objects.filter(name=food_name).first()
#             quantity = form1.cleaned_data['quantity']
#             save_model_instance=savemodel(name=food_item.name,quantity=quantity,
#                     protien=food_item.protien * quantity,
#                     carbs=food_item.carbs * quantity,
#                     fat=food_item.fat * quantity,
#                     nutrients=food_item.nutrients, 
#                     vitamins=food_item.vitamins)
#             print(save_model_instance,type(save_model_instance))
#             save_model_instance.save()
#             pass

#     saved_data=savemodel.objects.all()

#     return render(request,"track.html",{'form1':form1,"food_item":saved_data,"consumed_food":consumed_food})

def trackcontent(request):
    form = saveform()
    if request.method=="POST":
        form=saveform(request.POST)
        if form.is_valid():
            print("valid")
        food_name=form.cleaned_data['consumedfood']
        quantity=form.cleaned_data['quantity']
        # to filter the data
        food_item = calmodel.objects.filter(name=food_name).first()
        quantity = form.cleaned_data['quantity']
        save_model_instance=finalmodel(name=food_item.name,quantity=quantity,
                protien=food_item.protien * quantity,
                carbs=food_item.carbs * quantity,
                fat=food_item.fat * quantity,  
                nutrients=food_item.nutrients, 
                vitamins=food_item.vitamins,
                img=food_item.img,
                type=food_item.type)
        print(save_model_instance,type(save_model_instance))
        save_model_instance.save()
    saved_data=finalmodel.objects.all()
    totalp,totalf,totalc=0,0,0
    for i in saved_data:
        totalp+=i.protien
        totalf+=i.fat
        totalc+=i.carbs
        
    return render(request,'track.html',{'form':form,'food_item':saved_data,'totalp':totalp,"totalf":totalf,"totalc":totalc})

def delete1(request,pk):
    res=finalmodel.objects.get(id=pk)
    res.delete()
    return redirect('track')

def update(request,pk):
    res=finalmodel.objects.get(id=pk)
    if request.method == 'POST':
        form=caloform(request.POST,instance=res)
        if form.is_valid():
            instanc=form.save(commit=False)
            quant=form.cleaned_data['quantity']
            instanc.protien*=quant
            instanc.fat*=quant
            instanc.carbs*=quant
            instanc.save()
    
    form=caloform(instance=res)
    return render(request,'update.html',{"form":form})

def view(request,pk):
    res=calmodel.objects.filter(id=pk)
    return render(request,'view.html',{'res':res})


