from django.shortcuts import render
from grades.models import StudentModel


def add_student(request):
    from exam.forms import AddStudentForm
    form = AddStudentForm(request.POST or None)
    if form.is_valid():
        student = StudentModel(
            name=form.cleaned_data['name'],
            grades=form.cleaned_data['grades'],
            average_grade=__calculate_average_grade(form.cleaned_data['grades'])
        )
        student.save()
        context = {
            'student': student,
        }
        return render(request, template_name='student/view.html', context=context)
    context = {
        'form': form
    }
    return render(request, template_name='student/add.html', context=context)


def get_all_students(request):
    context = {
        'students': StudentModel.objects.all()
    }
    return render(request, template_name='student/list.html', context=context)


def get_student(request, student_id):
    context = {
        'student': StudentModel.objects.get(id=student_id)
    }
    return render(request, template_name='student/view.html', context=context)


def __calculate_average_grade(grades):
    grades_sum = 0
    grades_qty = 0
    for grade in grades.split(','):
        grades_qty += 1
        grades_sum += int(grade)
    return round(float(grades_sum / grades_qty), 2)
