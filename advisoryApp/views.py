from django.shortcuts import render
from django.http import HttpResponse
import joblib
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# views.py
def payment(request):
    return render(request, 'payment.html')
    


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in.")
                return redirect("core:home")
            else:
                messages.warning(request, "User Doesn't Exist, create an account.")
        except:
            messages.warning(request, f"User with {email} does not exist")


    return render(request, 'login.html')




#This is for the Home page
def home(request):
    return render(request, 'home.html')


from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm  # Import your UserRegisterForm

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, account created successfully")
            
            # Authenticate the user based on the email and password provided
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            
            if new_user is not None:
                # Log in the authenticated user
                login(request, new_user)
                return redirect('core:payment')
            else:
                # Handle authentication failure
                messages.error(request, "Failed to authenticate the new user.")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)



#This is for the career path
def career(request):
    return render(request, 'careerplanning.html')

#This is for the student performance
def performance(request):
    return render(request, 'performance.html')

#This is for the career path prediction
def careerpath(request):
  
    cls = joblib.load('C:\\Users\\MINISTER JOHN\\ClassAdvisorySystem\\DecisionTree_model_CareerPlanning.pkl')
    lis = []
    lis.append(request.GET.get('Logical quotient rating'))
    lis.append(request.GET.get('hackathons'))
    lis.append(request.GET.get('coding skills rating'))
    lis.append(request.GET.get('public speaking points'))
    lis.append(request.GET.get('self-learning capability?'))
    lis.append(request.GET.get('Extra-courses did'))
    lis.append(request.GET.get('certifications'))
    lis.append(request.GET.get('workshops'))
    lis.append(request.GET.get('reading and writing skills'))
    lis.append(request.GET.get('memory capability score '))
    lis.append(request.GET.get('Interested subjects'))
    lis.append(request.GET.get('interested career area '))
    lis.append(request.GET.get('Type of company want to settle in?'))
    lis.append(request.GET.get('Taken inputs from seniors or elders '))
    lis.append(request.GET.get('Interested Type of Books'))
    lis.append(request.GET.get('Management or Technical '))
    lis.append(request.GET.get('hard/smart worker'))
    lis.append(request.GET.get('worked in teams ever?'))
    lis.append(request.GET.get('Introvert'))

    
    ans = cls.predict([lis])
   
    return render(request, 'Careerpathresult.html', {'ans': ans})
  

#This is for student performance prediction
def studentperformance (request): 
    cls = joblib.load('C:\\Users\\MINISTER JOHN\\ClassAdvisorySystem\\svm_model.pkl')
    lis = []
    lis.append(request.GET['Student_Age'])
    lis.append(request.GET['Gender']) 
    lis.append(request.GET['Graduated_High_School_Type'])  
    lis.append(request.GET['Scholarship type'])  
    lis.append(request.GET['Additional work'])  
    lis.append(request.GET['Regular or Sport_Activity'])
    lis.append(request.GET['Do you have a partner'])
    lis.append(request.GET['Total Salary if available']) 
    lis.append(request.GET['Transportation medium to school'])
    lis.append(request.GET['Accomodation type']) 
    lis.append(request.GET['Mothers Education'])  
    lis.append(request.GET['FATHER_EDU'])  
    lis.append(request.GET['Number of Siblings'])  
    lis.append(request.GET['Parental status'])
    lis.append(request.GET['Mothers occupation'])
    lis.append(request.GET['Fathers occupation']) 
    lis.append(request.GET['Weekly study hours'])
    lis.append(request.GET['Reading frequency_Non-scientific book']) 
    lis.append(request.GET['Reading frequency_Scientific book'])  
    lis.append(request.GET['Attendance to departmental seminar and conferencese'])  
    lis.append(request.GET['Impact of any project to your success'])  
    lis.append(request.GET['Attendance to class'])
    lis.append(request.GET['Preparation_to_midterm-exam_1'])
    lis.append(request.GET['Preparation_to_midterm_exam-2'])  
    lis.append(request.GET['Takes Notes in class'])
    lis.append(request.GET['Listens in Class']) 
    lis.append(request.GET['Discussion improves my success'])  
    lis.append(request.GET['Flips classroom'])  
    lis.append(request.GET['Grade Point Average in Last semester'])  
    lis.append(request.GET['Expected CGPA in graduation'])
       

    predicted_performance = cls.predict([lis])
   
    return render(request, 'performanceresult.html', {'predicted_performance': predicted_performance })


# Define the view function for predicting student performance and displaying advice
def studentperformance(request):
    cls = joblib.load('C:\\Users\\MINISTER JOHN\\ClassAdvisorySystem\\svm_model.pkl')
    lis = []
    lis.append(request.GET['Student_Age'])
    lis.append(request.GET['Gender']) 
    lis.append(request.GET['Graduated_High_School_Type'])  
    lis.append(request.GET['Scholarship type'])  
    lis.append(request.GET['Additional work'])  
    lis.append(request.GET['Regular or Sport_Activity'])
    lis.append(request.GET['Do you have a partner'])
    lis.append(request.GET['Total Salary if available']) 
    lis.append(request.GET['Transportation medium to school'])
    lis.append(request.GET['Accomodation type']) 
    lis.append(request.GET['Mothers Education'])  
    lis.append(request.GET['FATHER_EDU'])  
    lis.append(request.GET['Number of Siblings'])  
    lis.append(request.GET['Parental status'])
    lis.append(request.GET['Mothers occupation'])
    lis.append(request.GET['Fathers occupation']) 
    lis.append(request.GET['Weekly study hours'])
    lis.append(request.GET['Reading frequency_Non-scientific book']) 
    lis.append(request.GET['Reading frequency_Scientific book'])  
    lis.append(request.GET['Attendance to departmental seminar and conferencese'])  
    lis.append(request.GET['Impact of any project to your success'])  
    lis.append(request.GET['Attendance to class'])
    lis.append(request.GET['Preparation_to_midterm-exam_1'])
    lis.append(request.GET['Preparation_to_midterm_exam-2'])  
    lis.append(request.GET['Takes Notes in class'])
    lis.append(request.GET['Listens in Class']) 
    lis.append(request.GET['Discussion improves my success'])  
    lis.append(request.GET['Flips classroom'])  
    lis.append(request.GET['Grade Point Average in Last semester'])  
    lis.append(request.GET['Expected CGPA in graduation'])
    # Assume student performance prediction is made by your machine learning model
    predicted_performance = predicted_performance = cls.predict([lis])  

    # Determine the advice based on the predicted performance
    advice = get_advice(predicted_performance)  # Function to determine advice based on prediction

    # Pass the predicted performance and advice to the HTML template
    context = {
        'predicted_performance': predicted_performance,
        'advice': advice,
    }

    return render(request, 'performanceresult.html', context)


# Define the function to get advice based on the predicted performance
def get_advice(studentperformance):
    if studentperformance == 0:
        return ("Your academic performance is very poor. Here are some tips to improve:\n"
                "- Attend all classes regularly.\n"
                "- Ask questions when you don't understand.\n"
                "- Seek help from tutors or teachers.\n"
                "- Create a study schedule and stick to it.\n"
                "- Review and practice regularly.")
    elif studentperformance == 1:
        return ("Your academic performance is marginal. Here are some tips to improve:\n"
                "- Identify areas where you struggle and seek help.\n"
                "- Stay organized and manage your time effectively.\n"
                "- Participate actively in class discussions.\n"
                "- Form study groups to review material together.\n"
                "- Utilize resources such as textbooks, online tutorials, and study guides.")
    elif studentperformance == 2:
        return ("Your academic performance is a pass, but with below-average performance. Here are some tips to improve:\n"
                "- Set clear academic goals and work towards achieving them.\n"
                "- Seek feedback from professors or mentors on areas for improvement.\n"
                "- Utilize supplementary learning resources to reinforce understanding.\n"
                "- Take advantage of office hours or tutoring services for extra support.\n"
                "- Practice active learning techniques such as summarizing, teaching others, and self-testing.")
    elif studentperformance == 3:
        return ("Your academic performance is a pass with an average level. Here are some tips to improve:\n"
                "- Focus on understanding concepts rather than memorization.\n"
                "- Engage in regular review and revision sessions.\n"
                "- Seek clarification on unclear topics from professors or peers.\n"
                "- Take advantage of academic support services offered by your institution.\n"
                "- Develop effective study habits and time management skills.")
    elif studentperformance == 4:
        return ("Your academic performance is a pass with above-average performance. Here are some tips to improve:\n"
                "- Challenge yourself with more advanced coursework or projects.\n"
                "- Actively seek out opportunities for academic enrichment or research.\n"
                "- Collaborate with classmates on group projects or study sessions.\n"
                "- Explore interdisciplinary connections to deepen your understanding.\n"
                "- Set ambitious but achievable academic goals and track your progress regularly.")
    elif studentperformance == 5:
        return ("Your academic performance is good, higher than average. Here are some tips to improve:\n"
                "- Continue to pursue intellectual curiosity and academic interests.\n"
                "- Explore opportunities for leadership and mentorship roles.\n"
                "- Consider engaging in research or independent study projects.\n"
                "- Network with professionals in your field of interest.\n"
                "- Stay updated with current developments and trends in your academic discipline.")
    elif studentperformance == 6:
        return ("Your academic performance is very good with distinction. Here are some tips to maintain:\n"
                "- Maintain a balance between academic pursuits and personal well-being.\n"
                "- Continue to challenge yourself with new academic endeavors.\n"
                "- Serve as a role model and mentor for peers.\n"
                "- Contribute to academic and intellectual discourse in your community.\n"
                "- Pursue opportunities for academic recognition or awards.")
    elif studentperformance == 7:
        return ("Your academic performance is excellent, with the highest level of distinction. Here are some tips to maintain:\n"
                "- Foster a lifelong commitment to learning and intellectual growth.\n"
                "- Engage in research, publication, or scholarly activities.\n"
                "- Mentor and support aspiring students in their academic journeys.\n"
                "- Contribute to the advancement of knowledge in your field through innovation and discovery.\n"
                "- Serve as an ambassador for academic excellence and integrity.")
    else:
        return "Invalid prediction. Please enter a valid prediction between 0 and 7."







