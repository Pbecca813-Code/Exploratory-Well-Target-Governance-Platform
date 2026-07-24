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
    WellTargetDocument,
    Project,
    ProjectTeam,
    Company,
    EmployeeProfile,
    SeismicReview,
    Validation,
    TargetApproval,
)

from .forms import (

    WellTargetForm,
    WellTargetDocumentForm,
    EmployeeCreateForm,
    EmployeeEditForm,
    AdministratorAccessRequestForm,
    ProjectForm,
    ProjectTeamForm,
    CompanyForm,
    ReviewForm,
    ValidationForm,

)


@login_required
def home(request):

    role = "No Role"

    groups = request.user.groups.all()

    if groups.exists():
        role = groups.first().name

    # ==========================================
    # DASHBOARD DATA
    # ==========================================

    targets = WellTarget.objects.all()

    documents = WellTargetDocument.objects.all().order_by("-upload_date")[:5]

    # ==========================================
    # KPI COUNTS
    # ==========================================

    employee_count = User.objects.count()

    company_count = Company.objects.count()

    project_count = Project.objects.count()

    planning_projects = Project.objects.filter(
    status="PLANNING"
    ).count()

    active_projects = Project.objects.filter(
    status="ACTIVE"
    ).count()

    on_hold_projects = Project.objects.filter(
    status="ON_HOLD"
    ).count()

    completed_projects = Project.objects.filter(
    status="COMPLETED"
    ).count()

    archived_projects = Project.objects.filter(
    status="ARCHIVED"
    ).count()

    well_target_count = WellTarget.objects.count()

    document_count = WellTargetDocument.objects.count()

    review_count = SeismicReview.objects.count()

    validation_count = Validation.objects.count()

    approval_count = TargetApproval.objects.count()

    # ==========================================
    # WELL TARGET STATUS
    # ==========================================

    draft_count = WellTarget.objects.filter(
        status="DRAFT"
    ).count()

    under_review_count = WellTarget.objects.filter(
        status="UNDER_REVIEW"
    ).count()

    validated_count = WellTarget.objects.filter(
        status="VALIDATED"
    ).count()

    approved_count = WellTarget.objects.filter(
        status="APPROVED"
    ).count()

    # ==========================================
    # CONTEXT
    # ==========================================

    context = {

        "role": role,

        "targets": targets,

        "documents": documents,

        # Enterprise KPIs
        "employee_count": employee_count,

        "company_count": company_count,

        "project_count": project_count,

        "planning_projects": planning_projects,

        "active_projects": active_projects,

        "on_hold_projects": on_hold_projects,

        "completed_projects": completed_projects,

        "archived_projects": archived_projects,

        "well_target_count": well_target_count,

        "document_count": document_count,

        "review_count": review_count,

        "validation_count": validation_count,

        "approval_count": approval_count,

        # Workflow Status
        "draft_count": draft_count,

        "under_review_count": under_review_count,

        "validated_count": validated_count,

        "approved_count": approved_count,

    }

    return render(
        request,
        "dashboard.html",
        context,
    )

# =====================================================
# WELL TARGET MANAGEMENT
# =====================================================

@login_required
def well_targets(request):

    targets = WellTarget.objects.all()

    status = request.GET.get("status")

    if status:

        targets = targets.filter(
            status=status
        )

    search = request.GET.get("search")

    if search:

        targets = targets.filter(
            target_name__icontains=search
        )

    return render(

        request,

        "well_targets.html",

        {

            "targets": targets,

            "selected_status": status,

            "search": search,

        },

    )

# =====================================================
# WELL TARGET DETAIL
# =====================================================

@login_required
def well_target_detail(request, pk):

    target = get_object_or_404(
        WellTarget,
        pk=pk
    )

    return render(
        request,
        "well_target_detail.html",
        {
            "target": target,
        }
    )

# =====================================================
# EDIT WELL TARGET
# =====================================================

@login_required
def well_target_edit(request, pk):

    target = get_object_or_404(
        WellTarget,
        pk=pk
    )

    if request.method == "POST":

        form = WellTargetForm(
            request.POST,
            instance=target
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Well Target updated successfully."
            )

            return redirect(
                "well_targets"
            )

    else:

        form = WellTargetForm(
            instance=target
        )

    return render(
        request,
        "well_target_edit.html",
        {
            "form": form,
            "target": target,
        }
    )

# =====================================================
# DELETE WELL TARGET
# =====================================================

@login_required
def well_target_delete(request, pk):

    target = get_object_or_404(
        WellTarget,
        pk=pk
    )

    if request.method == "POST":

        target.delete()

        messages.success(
            request,
            "Well Target deleted successfully."
        )

        return redirect(
            "well_targets"
        )

    return render(
        request,
        "well_target_delete.html",
        {
            "target": target,
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

    reviews = (
        SeismicReview.objects
        .select_related("well_target", "reviewer")
        .order_by("-review_date")
    )

    pending_reviews = reviews.filter(
        status="PENDING"
    ).count()

    in_progress_reviews = reviews.filter(
        status="IN_PROGRESS"
    ).count()

    completed_reviews = reviews.filter(
        status="COMPLETED"
    ).count()

    total_reviews = reviews.count()

    return render(
        request,
        "reviews.html",
        {
            "reviews": reviews,
            "pending_reviews": pending_reviews,
            "in_progress_reviews": in_progress_reviews,
            "completed_reviews": completed_reviews,
            "total_reviews": total_reviews,
        },
    )

# =====================================================
# CREATE REVIEW
# =====================================================

@login_required
def review_create(request):

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Review created successfully."
            )

            return redirect("reviews")

    else:

        form = ReviewForm()

    return render(

        request,

        "review_form.html",

        {

            "form": form,

            "title": "Create Review",

        },

    )


# =====================================================
# REVIEW DETAIL
# =====================================================

@login_required
def review_detail(request, pk):

    review = get_object_or_404(

        SeismicReview,

        pk=pk

    )

    return render(

        request,

        "review_detail.html",

        {

            "review": review,

        },

    )


# =====================================================
# EDIT REVIEW
# =====================================================

@login_required
def review_edit(request, pk):

    review = get_object_or_404(

        SeismicReview,

        pk=pk

    )

    if request.method == "POST":

        form = ReviewForm(

            request.POST,

            instance=review

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Review updated successfully."

            )

            return redirect(

                "reviews"

            )

    else:

        form = ReviewForm(

            instance=review

        )

    return render(

        request,

        "review_form.html",

        {

            "form": form,

            "title": "Edit Review",

        },

    )


# =====================================================
# DELETE REVIEW
# =====================================================

@login_required
def review_delete(request, pk):

    review = get_object_or_404(

        SeismicReview,

        pk=pk

    )

    if request.method == "POST":

        review.delete()

        messages.success(

            request,

            "Review deleted successfully."

        )

        return redirect(

            "reviews"

        )

    return render(

        request,

        "review_delete.html",

        {

            "review": review,

        },

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

# =====================================================
# USER MANAGEMENT
# =====================================================

@login_required
def user_management(request):

    users = User.objects.all().order_by(
        "first_name",
        "last_name"
    )

    admin_count = User.objects.filter(
        is_staff=True
    ).count()

    active_count = User.objects.filter(
        is_active=True
    ).count()

    inactive_count = User.objects.filter(
        is_active=False
    ).count()

    context = {

        "users": users,

        "admin_count": admin_count,

        "active_count": active_count,

        "inactive_count": inactive_count,

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

# =====================================================
# EMPLOYEE DETAIL
# =====================================================

@login_required
def employee_detail(request, pk):

    employee = get_object_or_404(
        User,
        pk=pk
    )

    return render(
        request,
        "employee_detail.html",
        {
            "employee": employee,
        },
    )


# =====================================================
# EDIT EMPLOYEE
# =====================================================

@login_required
def employee_edit(request, pk):

    employee = get_object_or_404(
        User,
        pk=pk
    )

    if request.method == "POST":

        form = EmployeeEditForm(
            request.POST,
            instance=employee,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Employee updated successfully."
            )

            return redirect(
                "user_management"
            )

    else:

        form = EmployeeEditForm(
            instance=employee
        )

    return render(
        request,
        "employee_form.html",
        {
            "form": form,
            "employee": employee,
            "title": "Edit Employee",
        },
    )


# =====================================================
# DELETE EMPLOYEE
# =====================================================

@login_required
def employee_delete(request, pk):

    employee = get_object_or_404(
        User,
        pk=pk
    )

    if request.method == "POST":

        employee.delete()

        messages.success(
            request,
            "Employee deleted successfully."
        )

        return redirect(
            "user_management"
        )

    return render(
        request,
        "employee_delete.html",
        {
            "employee": employee,
        },
    )

# =====================================================
# FORGOT PASSWORD
# =====================================================

from django.contrib import messages


def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get("email")

        messages.success(

            request,

            "If this email address exists, a password reset link will be sent."

        )

    return render(

        request,

        "registration/forgot_password.html"

    )
# =====================================================
# FORGOT USERNAME
# =====================================================

def forgot_username(request):

    if request.method == "POST":

        email = request.POST.get("email")

        messages.success(

            request,

            "If this email address exists, your username will be sent."

        )

    return render(

        request,

        "registration/forgot_username.html"

    )
# =====================================================
# REQUEST ADMINISTRATOR ACCESS
# =====================================================

def request_admin_access(request):

    if request.method == "POST":

        form = AdministratorAccessRequestForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Your administrator access request has been submitted successfully. It is now pending review."

            )

            return redirect("request_admin_access")

    else:

        form = AdministratorAccessRequestForm()

    return render(

        request,

        "registration/request_admin_access.html",

        {

            "form": form

        }

    )

# =====================================================
# PROJECT MANAGEMENT
# =====================================================

@login_required
def project_management(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Project created successfully."
            )

            return redirect("project_management")

    else:

        form = ProjectForm()

    projects = Project.objects.all().order_by("-created_at")

    context = {

        "form": form,

        "projects": projects,

    }

    return render(

        request,

        "project_management.html",

        context,

    )

# =====================================================
# PROJECT DETAILS
# =====================================================

@login_required
def project_detail(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    context = {

        "project": project,

    }

    return render(

        request,

        "project_detail.html",

        context,

    )

# =====================================================
# PROJECT TEAM
# =====================================================

@login_required
def project_team(request, pk):

    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":

        form = ProjectTeamForm(request.POST)

        if form.is_valid():

            assignment = form.save(commit=False)

            assignment.project = project

            assignment.assigned_by = request.user

            if ProjectTeam.objects.filter(
                project=project,
                employee=assignment.employee
            ).exists():

                messages.warning(
                    request,
                    "This employee is already assigned."
                )

            else:

                assignment.save()

                messages.success(
                    request,
                    "Team member assigned successfully."
                )

            return redirect(
                "project_team",
                pk=project.pk
            )

        else:

            print(form.errors)

    else:

        form = ProjectTeamForm()

    members = project.team_members.select_related("employee")

    return render(
        request,
        "project_team.html",
        {
            "project": project,
            "form": form,
            "members": members,
        }
    )

# =====================================================
# EDIT PROJECT TEAM MEMBER
# =====================================================

@login_required
def project_team_edit(request, pk):

    member = get_object_or_404(ProjectTeam, pk=pk)

    if request.method == "POST":

        form = ProjectTeamForm(
            request.POST,
            instance=member
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Team member updated successfully."
            )

            return redirect(
                "project_team",
                pk=member.project.id
            )

    else:

        form = ProjectTeamForm(instance=member)

    return render(
        request,
        "project_team_edit.html",
        {
            "form": form,
            "member": member,
        },
    )

# =====================================================
# DELETE PROJECT TEAM MEMBER
# =====================================================

@login_required
def project_team_delete(request, pk):

    member = get_object_or_404(ProjectTeam, pk=pk)

    project_id = member.project.id

    if request.method == "POST":

        member.delete()

        messages.success(
            request,
            "Team member removed successfully."
        )

        return redirect(
            "project_team",
            pk=project_id
        )

    return render(
        request,
        "project_team_delete.html",
        {
            "member": member,
        },
    )

# =====================================================
# EDIT PROJECT
# =====================================================

@login_required
def project_edit(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Project updated successfully."
            )

            return redirect("project_management")

    else:

        form = ProjectForm(instance=project)

    context = {

        "form": form,

        "project": project,

    }

    return render(

        request,

        "project_edit.html",

        context,

    )

# =====================================================
# DELETE PROJECT
# =====================================================

@login_required
def project_delete(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    if request.method == "POST":

        project.delete()

        messages.success(

            request,

            "Project deleted successfully."

        )

        return redirect("project_management")

    return render(

        request,

        "project_delete.html",

        {

            "project": project

        }

    )

# =====================================================
# MASTER DATA
# =====================================================

@login_required
def master_data(request):

    return render(
        request,
        "master_data.html"
    )

# =====================================================
# COMPANY MANAGEMENT
# =====================================================

@login_required
def company_list(request):

    companies = Company.objects.all().order_by("name")

    return render(
        request,
        "companies/company_list.html",
        {
            "companies": companies,
        },
    )


@login_required
def company_create(request):

    if request.method == "POST":

        form = CompanyForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Company created successfully."
            )

            return redirect("company_list")

    else:

        form = CompanyForm()

    return render(
        request,
        "companies/company_form.html",
        {
            "form": form,
            "title": "Create Company",
        },
    )


@login_required
def company_edit(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk
    )

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            instance=company
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Company updated successfully."
            )

            return redirect("company_list")

    else:

        form = CompanyForm(instance=company)

    return render(
        request,
        "companies/company_form.html",
        {
            "form": form,
            "title": "Edit Company",
        },
    )


@login_required
def company_delete(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk
    )

    company.delete()

    messages.success(
        request,
        "Company deleted successfully."
    )

    return redirect("company_list")

# =====================================================
# COMING SOON PAGE
# =====================================================

@login_required
def coming_soon(request, title):

    return render(

        request,

        "coming_soon.html",

        {

            "title": title.replace("-", " ").title(),

        },

    )