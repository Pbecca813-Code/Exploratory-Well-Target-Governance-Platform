from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path("register/", views.register, name="register"),

    path(
        'well-targets/',
        views.well_targets,
        name='well_targets'
    ),

    path(
    "well-targets/<int:pk>/",
    views.well_target_detail,
    name="well_target_detail",
),

path(
    "well-targets/<int:pk>/edit/",
    views.well_target_edit,
    name="well_target_edit",
),

path(
    "well-targets/<int:pk>/delete/",
    views.well_target_delete,
    name="well_target_delete",
),

    path(
        'new-target/',
        views.new_target,
        name='new_target'
    ),

    path(
        'upload-document/',
        views.upload_document,
        name='upload_document'
   ),
    
    path(
        'documents/download/<int:document_id>/',
        views.download_document,
        name='download_document'
   ),
   
    path(
        'documents/delete/<int:document_id>/',
        views.delete_document,
        name='delete_document'
   ),

    path(
        'documents/',
        views.documents,
        name='documents'
    ),

    path(
        'documents/view/<int:document_id>/',
        views.view_document,
        name='view_document'
   ),

    path(
        'reviews/',
        views.reviews,
        name='reviews'
    ),

    # =====================================================
# REVIEW CRUD
# =====================================================

path(
    "reviews/new/",
    views.review_create,
    name="review_create",
),

path(
    "reviews/<int:pk>/",
    views.review_detail,
    name="review_detail",
),

path(
    "reviews/<int:pk>/edit/",
    views.review_edit,
    name="review_edit",
),

path(
    "reviews/<int:pk>/delete/",
    views.review_delete,
    name="review_delete",
),

    path(
        'validation/',
        views.validation,
        name='validation'
    ),

    path(
        'approvals/',
        views.approvals,
        name='approvals'
    ),

    path(
        'audit-trail/',
        views.audit_trail,
        name='audit_trail'
    ),

    path(
        'reports/',
        views.reports,
        name='reports'
    ),

    path(
        'project-management/',
        views.project_management,
        name='project_management'
    ),

    path(
        'administration/users/',
        views.user_management,
        name='user_management'
    ),

    path(
        'administration/users/create/',
        views.create_employee,
        name='create_employee'
    ),

    # =====================================================
# EMPLOYEE CRUD
# =====================================================

path(
    "employees/<int:pk>/",
    views.employee_detail,
    name="employee_detail",
),

path(
    "employees/<int:pk>/edit/",
    views.employee_edit,
    name="employee_edit",
),

path(
    "employees/<int:pk>/delete/",
    views.employee_delete,
    name="employee_delete",
),

    path(
        "user-login/",
        views.user_login,
        name="user_login",
    ),

    path(
        "admin-login/",
        views.admin_login,
        name="admin_login",
    ),

    path(
        "forgot-password/",
        views.forgot_password,
        name="forgot_password",
    ),

    path(
        "forgot-username/",
        views.forgot_username,
        name="forgot_username",
    ),

    path(
        "request-admin-access/",
        views.request_admin_access,
        name="request_admin_access",
    ),

    path(
        "master-data/",
        views.master_data,
        name="master_data",
    ),

    path(
    "companies/",
    views.company_list,
    name="company_list",
),

path(
    "companies/new/",
    views.company_create,
    name="company_create",
),

path(
    "companies/<int:pk>/edit/",
    views.company_edit,
    name="company_edit",
),

path(
    "companies/<int:pk>/delete/",
    views.company_delete,
    name="company_delete",
),

path(
    "projects/<int:pk>/",
    views.project_detail,
    name="project_detail",
),

path(
    "projects/<int:pk>/team/",
    views.project_team,
    name="project_team",
),

path(
    "projects/<int:pk>/edit/",
    views.project_edit,
    name="project_edit",
),

path(
    "projects/<int:pk>/delete/",
    views.project_delete,
    name="project_delete",
),

path(
    "project-team/<int:pk>/edit/",
    views.project_team_edit,
    name="project_team_edit",
),

path(
    "project-team/<int:pk>/delete/",
    views.project_team_delete,
    name="project_team_delete",
),

path(
    "coming-soon/<str:title>/",
    views.coming_soon,
    name="coming_soon",
),
]
