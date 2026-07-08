from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm

from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from django.http import FileResponse
import mimetypes

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import (
    WellTarget,
    WellTargetDocument
)

from .forms import (
    WellTargetForm,
    WellTargetDocumentForm,
    EmployeeCreateForm,
)


@login_required
def home(request):

    role = "No Role"

    groups = request.user.groups.all()

    if groups.exists():
        role = groups.first().name

    targets = WellTarget.objects.all()

    documents = WellTargetDocument.objects.all().order_by('-upload_date')[:5]

    document_count = WellTargetDocument.objects.count()

    draft_count = WellTarget.objects.filter(status='DRAFT').count()

    review_count = WellTarget.objects.filter(
        status='UNDER_REVIEW'
    ).count()

    validated_count = WellTarget.objects.filter(
        status='VALIDATED'
    ).count()

    approved_count = WellTarget.objects.filter(
        status='APPROVED'
    ).count()

    context = {

        'role': role,

        'targets': targets,

        'documents': documents,

        'document_count': document_count, 
        
        'draft_count': draft_count,

        'review_count': review_count,

        'validated_count': validated_count,

        'approved_count': approved_count,

    }

    return render(
        request,
        'dashboard.html',
        context
    )

@login_required
def well_targets(request):

    targets = WellTarget.objects.all()

    return render(
        request,
        'well_targets.html',
        {
            'targets': targets
        }
    )


@login_required
def new_target(request):

    if request.method == 'POST':

        form = WellTargetForm(request.POST)

        if form.is_valid():

            target = form.save(commit=False)

            target.lead_interpreter = request.user

            target.save()

            return redirect('/')

    else:

        form = WellTargetForm()

    return render(
        request,
        'new_target.html',
        {
            'form': form
        }
    )
@login_required
def upload_document(request):

    if request.method == 'POST':

        form = WellTargetDocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            document = form.save(commit=False)

            document.uploaded_by = request.user

            document.save()

            return redirect('documents')

    else:

        form = WellTargetDocumentForm()

    return render(
        request,
        'upload_document.html',
        {
            'form': form
        }
    )
@login_required
def documents(request):

    documents = WellTargetDocument.objects.all()

    form = WellTargetDocumentForm()

    context = {

        'documents': documents,

        'form': form

    }

    return render(
        request,
        'documents.html',
        context
    )


@login_required
def reviews(request):
    return render(
        request,
        'reviews.html'
    )

@login_required
def view_document(request, document_id):

    document = get_object_or_404(
        WellTargetDocument,
        id=document_id
    )

    file_path = document.file.path

    mime_type, _ = mimetypes.guess_type(file_path)

    return FileResponse(
        open(file_path, 'rb'),
        content_type=mime_type
    )

@login_required
def validation(request):
    return render(
        request,
        'validation.html'
    )


@login_required
def approvals(request):
    return render(
        request,
        'approvals.html'
    )


@login_required
def audit_trail(request):
    return render(
        request,
        'audit_trail.html'
    )


@login_required
def reports(request):
    return render(
        request,
        'reports.html'
    )

@login_required
def download_document(request, document_id):

    document = get_object_or_404(
        WellTargetDocument,
        id=document_id
    )

    try:
        return FileResponse(
            document.file.open('rb'),
            as_attachment=True
        )
    except FileNotFoundError:
        raise Http404("File not found.")
    
@login_required
def delete_document(request, document_id):

    document = get_object_or_404(
        WellTargetDocument,
        id=document_id
    )

    document.file.delete()

    document.delete()

    return redirect('documents')

def register(request):

    # Disable public registration in production
    if not settings.ALLOW_SELF_REGISTRATION:
        return redirect("login")

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterUserForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            login(request, user)

            return redirect("home")

    else:

        form = RegisterUserForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form
        }
    )

@login_required
def user_management(request):

    users = User.objects.all().order_by("first_name")

    context = {
        "users": users,
    }

    return render(
        request,
        "user_management.html",
        context,
    )

@login_required
def create_employee(request):

    if request.method == "POST":

        form = EmployeeCreateForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(

                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],

            )

            return redirect("user_management")

    else:

        form = EmployeeCreateForm()

    return render(
        request,
        "create_employee.html",
        {
            "form": form
        }
    )

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "registration/user_login.html"
    )
    
def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:

            login(request, user)

            return redirect("home")

        messages.error(
            request,
            "Administrator credentials required."
        )

    return render(
        request,
        "registration/admin_login.html"
    )