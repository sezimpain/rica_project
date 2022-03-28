from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, school_type_choices
from .forms import StudentForm



def index(request, *args, **kwargs):
    search_querry = request.GET.get("search", "")

    if search_querry:
        students = Student.objects.filter(name_and_family__icontains=search_querry)
    else:
        students = Student.objects.all().order_by('-date')

    context = {
        'students': students
    }

    return render(request, 'index.html', context)

@login_required(login_url='login')
def new(request, *args, **kwargs):
    if request.method == 'GET':
        form = StudentForm()
        context = {
            'statuses': school_type_choices,
            'form': form
        }
        return render(request, 'new.html', context)

    elif request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            Student.objects.create(
                name_and_family=form.cleaned_data['name_and_family'],
                date=form.cleaned_data['date'],
                phone_number=form.cleaned_data['phone_number'],
                school_type=form.cleaned_data['school_type'],
                grade=form.cleaned_data['grade'],
                pay=form.cleaned_data['pay'],
                registered=form.cleaned_data['registered'],
                address=form.cleaned_data['address'],
                extra_classes=form.cleaned_data['extra_classes'],
                additional_info=form.cleaned_data['additional_info'],
                father_name=form.cleaned_data['father_name'],
                father_phone=form.cleaned_data["father_phone"],
                father_job=form.cleaned_data["father_job"],
                mother_name=form.cleaned_data["mother_name"],
                mother_phone=form.cleaned_data["mother_phone"],
                mother_job=form.cleaned_data["mother_job"]
            )
            return redirect('index')
        else:
            return render(request, 'new.html', context={'form': form})


@login_required(login_url='login')
def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)


@login_required(login_url='login')
def delete(request, pk):
    if request.method == 'GET':
        student = get_object_or_404(Student, pk=pk)
        context = {
            'student': student
        }
        return render(request, 'delete.html', context)
    else:
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('index')


@login_required(login_url='login')
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'GET':
        form = StudentForm(data={
            'name_and_family': student.name_and_family,
            'date': student.date,
            'phone_number': student.phone_number,
            'school_type': student.school_type,
            'grade': student.grade,
            'pay': student.pay,
            'registered': student.registered,
            'address': student.address,
            'extra_classes': student.extra_classes,
            'additional_info': student.additional_info,
            'father_name': student.father_name,
            'father_phone': student.father_phone,
            'father_job': student.father_job,
            'mother_name': student.mother_name,
            'mother_phone': student.mother_phone,
            'mother_job': student.mother_job
        })
        return render(request, 'edit.html', context={'form': form, 'student': student})

    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            student.name_and_family = form.cleaned_data['name_and_family']
            student.date = form.cleaned_data['date']
            student.phone_number = form.cleaned_data['phone_number']
            student.school_type = form.cleaned_data['school_type']
            student.grade = form.cleaned_data['grade']
            student.pay = form.cleaned_data['pay']
            student.registered = form.cleaned_data["registered"]
            student.address = form.cleaned_data['address']
            student.extra_classes = form.cleaned_data['extra_classes']
            student.additional_info = form.cleaned_data['additional_info']
            student.image = form.cleaned_data['image']
            student.father_name = form.cleaned_data['father_name']
            student.father_phone = form.cleaned_data['father_phone']
            student.father_job = form.cleaned_data['father_job']
            student.mother_name = form.cleaned_data["mother_name"]
            student.mother_phone = form.cleaned_data["mother_phone"]
            student.mother_job = form.cleaned_data['mother_job']
            student.save()
            return redirect('index')
        else:
            return render(request, 'edit.html', context={'form': form, 'student': student})


@login_required(login_url='login')
def delete_items(request):
    data = request.POST
    for pk in data.keys():
        if pk == 'csrfmiddlewaretoken':
            continue
        student = get_object_or_404(Student, pk=pk)
        student.delete()
    return redirect('index')

