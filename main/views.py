from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateList
# Create your views here.
def index(request, pk):

    my_list = ToDoList.objects.get(id=pk)
    name = my_list.name
    items = my_list.item_set.all()


    if my_list in request.user.todolist.all():
        if request.method == 'POST':
            print(request.POST)
            if request.POST.get('save'):
                for item in items:
                    if request.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()


            elif request.POST.get('additem'):
                txt = request.POST.get('newitem')

                if len(txt) > 2:
                    my_list.item_set.create(text=txt, complete=False)
                else:
                    print('Invalid')

        context = {
            'name':name,
            'items':items,
        }
        
        return render(request, 'main/single.html', context)
    
    else:
        return render(request, 'main/home.html')




def home(request):
    return render(request, 'main/home.html')




def create(request):

    if request.method == 'POST':
        form = CreateList(request.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            todo = ToDoList(name = n)
            todo.save()
            request.user.todolist.add(todo)

        return HttpResponseRedirect("/%i" %todo.id)

    else: 
        form = CreateList()

    context = {
        'form':form,
    }
    
    return render(request, 'main/create.html', context)