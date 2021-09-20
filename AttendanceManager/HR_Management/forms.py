from django.forms import ModelForm
from .models import Employees_Detail
from django import forms

#create a employee deltail forms
class RegisterForm(ModelForm):
    class Meta:
        model= Employees_Detail
        fields = ('Gender','Employee_Name','Phone_Number','Date_Of_Birth','Address_Line_1','Address_Line_2','PAN_Card_Number','Bank_Acount_Name','Bank_Account_Number','Reference_1_Name','Reference_1_Phone_number','Reference_2_Name','Reference_2_Phone_number','Spouse_Or_Husband_Or_Father_Name','Spouse_Or_Husband_Or_Father_Date_Of_Birth','Spouse_Or_Husband_Or_Father_Phone_Number','Child_1_If_any','Child_2_If_any','Education_Qualification_1','Education_Qualification_2','Experience','Last_Place_Of_Work','Previous_Postion')
        labels = {
            'Employee_Name':'',
            'Phone_Number':'',
            'Date_Of_Birth':'',
            'Address_Line_1':'',
            'Address_Line_2': '',
            'PAN_Card_Number':'',
            'Bank_Acount_Name':'',
            'Bank_Account_Number':'',

            'Reference_1_Name':'',
            'Reference_1_Phone_number':'',
            'Reference_2_Name':'',
            'Reference_2_Phone_number':'',
            'Spouse_Or_Husband_Or_Father_Name':'',
            'Spouse_Or_Husband_Or_Father_Date_Of_Birth':'',
            'Spouse_Or_Husband_Or_Father_Phone_Number':'',
            'Child_1_If_any':'',
            'Child_2_If_any':'',
            'Education_Qualification_1':'',
            'Education_Qualification_2':'',
            'Experience':'',
            'Last_Place_Of_Work':'',
            'Previous_Postion':'',


            }
        widgets = {
            'Employee_Name':forms.TextInput(attrs={"placeholder":"Name"}),
            'Phone_Number':forms.TextInput(attrs={"placeholder":"Phone Number"}),
            'Date_Of_Birth': forms.TextInput(attrs={"placeholder":"D.O.B"}),
            'Address_Line_1':forms.TextInput(attrs={"placeholder":"Address Line 1"}),
            'Address_Line_2': forms.TextInput(attrs={"placeholder": "Address Line 2"}),
            'PAN_Card_Number': forms.TextInput(attrs={"placeholder": "PAN Number"}),
            'Bank_Acount_Name': forms.TextInput(attrs={"placeholder": "Bank Account Name"}),
            'Bank_Account_Number':forms.TextInput(attrs={"placeholder": "Bank Account Number"}),
            'Reference_1_Name': forms.TextInput(attrs={"placeholder": "Reference 1 Name"}),
            'Reference_1_Phone_number': forms.TextInput(attrs={"placeholder": "Reference 1 Phone number"}),
            'Reference_2_Name': forms.TextInput(attrs={"placeholder": "Reference 1 Name"}),
            'Reference_2_Phone_number': forms.TextInput(attrs={"placeholder": "Reference 2 Phone number"}),
            'Spouse_Or_Husband_Or_Father_Name': forms.TextInput(attrs={"placeholder": "Spouse/Husband/Father's Name"}),
            'Spouse_Or_Husband_Or_Father_Date_Of_Birth': forms.TextInput(attrs={"placeholder": "Spouse/Husband/Father's D.O.B"}),
            'Spouse_Or_Husband_Or_Father_Phone_Number': forms.TextInput(attrs={"placeholder": "Spouse/Husband/Father's Phone Number"}),
            'Child_1_If_any': forms.TextInput(attrs={"placeholder": "Child 1 If any"}),
            'Child_2_If_any': forms.TextInput(attrs={"placeholder": "Child 2 If any"}),
            'Education_Qualification_1': forms.TextInput(attrs={"placeholder": "Education Qualification 1"}),
            'Education_Qualification_2': forms.TextInput(attrs={"placeholder": "Education Qualification 2"}),
            'Experience': forms.TextInput(attrs={"placeholder": "Experience"}),
            'Last_Place_Of_Work': forms.TextInput(attrs={"placeholder": "Last Place Of Work"}),
            'Previous_Postion': forms.TextInput(attrs={"placeholder": "Previous Postion"}),
        }