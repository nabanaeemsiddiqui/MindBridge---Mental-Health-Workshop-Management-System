from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login
from .models import Workshop, Enrollment, Feedback
from django.contrib.auth.decorators import login_required
from .feedback_form import FeedbackForm


def home(request):

    workshops = Workshop.objects.all()

    return render(request, 'home.html', {
        'workshops': workshops
    })

def signup(request):

    if request.method == 'POST':
        form = CustomUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('home')

    else:
        form = CustomUserForm()

    return render(request, 
                  'signup.html',
                   {'form': form})


@login_required
def enroll(request, workshop_id):

    workshop = Workshop.objects.get(id=workshop_id)

    enrolled_count = Enrollment.objects.filter(
        workshop=workshop
    ).count()

    if enrolled_count >= workshop.seats:

        return redirect('home')  # workshop full

    already_enrolled = Enrollment.objects.filter(
        user=request.user,
        workshop=workshop
    ).exists()

    if not already_enrolled:

        Enrollment.objects.create(
            user=request.user,
            workshop=workshop
        )

    return redirect('home')


@login_required
def my_workshops(request):

    enrollments = Enrollment.objects.filter(
        user=request.user
    )

    return render(request,
                  'my_workshops.html',
                  {'enrollments': enrollments})

@login_required
def give_feedback(request, workshop_id):

    workshop = Workshop.objects.get(id=workshop_id)

    already_submitted = Feedback.objects.filter(
        user=request.user,
        workshop=workshop
    ).exists()

    if already_submitted:

        return redirect('my_workshops')

    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():

            feedback = form.save(commit=False)

            feedback.user = request.user
            feedback.workshop = workshop

            feedback.save()

            return redirect('my_workshops')

    else:

        form = FeedbackForm()

    return render(request,
                  'feedback.html',
                  {
                      'form': form,
                      'workshop': workshop
                  })