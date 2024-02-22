from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Contact
from .serializers import ContactSerializer
from .forms import ContactForm
from django.views import View


#==========================================START===============================================#
#This Section is For the List, Create, Update and Delete Contact by Using Django Rest Framework
#==============================================================================================#

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

#==============================================================================================#
#This Section is For the List, Create, Update and Delete Contact by Using Django Rest Framework
#==============================================END=============================================#



#=============================================================START===========================================================#
#This Section is For the List, Create, Update and Delete Contact Including the Frontend by using DTL(Django Template Language)
#=============================================================================================================================#

# Views Display a list of all contacts
class ContactListView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'contacts/contact_list.html', {'contacts': contacts})


# View For Adding A New Contact.
class ContactCreateView(View):
    def get(self, request):
         # Create an instance of the ContactForm
        form = ContactForm()
        # Render the contact form template with the form instance
        return render(request, 'contacts/contact_form.html', {'form': form})

    def post(self, request):
         # Create an instance of the ContactForm with the data from the POST request
        form = ContactForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            form.save()
            return redirect('contact-list')
        # If the form is not valid, render the contact form template with the form instance
        return render(request, 'contacts/contact_form.html', {'form': form})
    

# View For Update The Contact Informations    
class ContactEditView(View):
    def get(self, request, contact_id):
        contact = get_object_or_404(Contact, id=contact_id)
        form = ContactForm(instance=contact)
        return render(request, 'contacts/contact_edit.html', {'form': form, 'contact': contact})

    def post(self, request, contact_id):
        contact = get_object_or_404(Contact, id=contact_id)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
        return render(request, 'contacts/contact_edit.html', {'form': form, 'contact': contact})


class DeleteContactView(View):
    def get(self, request, contact_id):
        contact = get_object_or_404(Contact, id=contact_id)
        return render(request, 'contacts/contact_list.html', {'contact': contact})

    def post(self, request, contact_id):
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
        return redirect('contact-list')


#=============================================================================================================================#
#This Section is For the List, Create, Update and Delete Contact Including the Frontend by using DTL(Django Template Language)
#===============================================================END===========================================================#