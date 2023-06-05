from django.shortcuts import render, redirect
from .models import EnteringPerson, Student, Teacher
from .forms import EnteringPersonForm
import mysql.connector


def auth(request):
    return render(request, 'enter.html')

def enter(request):
    if request.method == 'POST':
        
        if True:
            role_value = request.POST.get('status')
            unique_numbers_value = request.POST.get('pass')
            full_name_value = request.POST.get('full_name')

            print(role_value)
            print(unique_numbers_value)
            print(full_name_value)

            if role_value == 'student':
                # check if in db + redirect if necessary

                conn = mysql.connector.connect(user='<username>', password='<password>', database='<database>')
                
                cursor = conn.cursor()

                cursor.execute(f"SELECT COUNT (*) FROM students WHERE unique_numbers = {unique_numbers}")
                
                account_exists = cursor.fetchone() 

                if account_exists == 1:
                    # redirect to assesment page
                    pass

                else:
                    return render(request, 'enter.html', {'form': EnteringPersonForm()})
                    

            elif role_value == 'teacher':
                # check if in db + redirect if necessary

                conn = mysql.connector.connect(user='<username>', password='<password>', database='<database>')
                
                cursor = conn.cursor()

                cursor.execute(f"SELECT COUNT (*) FROM teachers WHERE unique_numbers = {unique_numbers}")
                
                account_exists = cursor.fetchone()

                if account_exists == 1:
                    # redirect on page with teacher stats
                    pass

                else:
                    return render(request, 'enter.html', {'form': EnteringPersonForm()})

            elif role_value == 'matirculant':
                pass

            elif role_value == 'director':
                pass

        form = EnteringPersonForm()

        data = {
            'form': form
        }

        return render(request, 'enter.html', data)