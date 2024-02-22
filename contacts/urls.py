from django.urls import path
# from .views import ContactListView, ContactCreateView, ContactEditView, DeleteContactView
from contacts import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    #==========================================START===============================================#
    #This Section is For the List, Create, Update and Delete Contact by Using Django Rest Framework
    #==============================================================================================#

    path('contacts_api/', views.ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', views.ContactRetrieveUpdateDestroyView.as_view(), name='contact-retrieve-update-destroy'),
    # For JWT Token Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #==============================================================================================#
    #This Section is For the List, Create, Update and Delete Contact by Using Django Rest Framework
    #==============================================END=============================================#


    #=============================================================START===========================================================#
    #This Section is For the List, Create, Update and Delete Contact Including the Frontend by using DTL(Django Template Language)
    #=============================================================================================================================#

    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
    path('contacts/create/', views.ContactCreateView.as_view(), name='contact-create'),
    path('contacts/edit/<int:contact_id>/', views.ContactEditView.as_view(), name='contact-edit'),
    path('delete-contact/<int:contact_id>/', views.DeleteContactView.as_view(), name='delete-contact'),

    #================================================================END=========================================================#
    #This Section is For the List, Create, Update and Delete Contact Including the Frontend by using DTL(Django Template Language)
    #=============================================================================================================================#
]
