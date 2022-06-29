from django.forms import Form, CharField


class AddStudentForm(Form):
    name = CharField(label='Name', max_length=200)
    grades = CharField(label='Grades', max_length=100)

