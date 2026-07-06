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

]