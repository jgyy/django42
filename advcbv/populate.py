import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advcbv.settings')
django.setup()

from basic_app.models import School, Student

school1 = School(name='ABC School', principal='Mr. Smith', location='New York')
school2 = School(name='XYZ School', principal='Ms. Johnson', location='California')

school1.save()
school2.save()

student1 = Student(name='John Doe', age=15, school=school1)
student2 = Student(name='Jane Smith', age=16, school=school1)
student3 = Student(name='Mike Johnson', age=14, school=school2)
student4 = Student(name='Emily Brown', age=17, school=school2)

student1.save()
student2.save()
student3.save()
student4.save()

print("Sample data populated successfully!")
