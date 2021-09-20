from django.db import models
from model_utils import Choices


# Create your models here.

class Employees_Detail(models.Model):
    Department_type= Choices('Select','Sales', "Service", "Both","Admin")
    Department = Choices('Select','HR', "Gate", "IT",'Accounts', "Warranty","Warranty",'Insurance', "Customer Care")
    Roles = Choices('Select','GM',"CFO", "VP", "CEO", "Manager","Sales Manager","Service Manager","Customer Care Manager","Executive","Accounts Officer","Accounts Head")
    Gender = Choices('Select', 'Male', "Female")
    Employee_ID = models.BigAutoField(primary_key=True)
    Employee_Name=models.CharField(max_length=50,blank=True,null=True)
    Phone_Number=models.CharField(max_length=10,blank=True)
    Date_Of_Birth=models.DateField(blank=True,null=True)
    Gender=models.CharField(choices=Gender, default=Department_type.Select, max_length=20)
    Address_Line_1=models.CharField(max_length=50,blank=True)
    Address_Line_2 = models.CharField(max_length=50, blank=True)
    PAN_Card_Number=models.CharField(max_length=10,blank=True)
    Bank_Acount_Name=models.CharField(max_length=30, blank=True)
    Bank_Account_Number=models.CharField(max_length=30, blank=True)
    Passport_Size_Image=models.ImageField(upload_to='images',null=True)

    Reference_1_Name = models.CharField(max_length=20, blank=True)
    Reference_1_Phone_number = models.CharField(max_length=20, blank=True)
    Reference_2_Name = models.CharField(max_length=20, blank=True)
    Reference_2_Phone_number = models.CharField(max_length=20, blank=True)

    Spouse_Or_Husband_Or_Father_Name=models.CharField(max_length=30, blank=True)
    Spouse_Or_Husband_Or_Father_Date_Of_Birth = models.CharField(max_length=30, blank=True)
    Spouse_Or_Husband_Or_Father_Phone_Number=models.CharField(max_length=10,blank=True)
    Child_1_If_any= models.CharField(max_length=20,blank=True)
    Child_2_If_any = models.CharField(max_length=20, blank=True)

    Education_Qualification_1=models.CharField(max_length=30, blank=True)
    Education_Qualification_2 = models.CharField(max_length=30, blank=True)

    Experience = models.CharField(max_length=50, blank=True)
    Last_Place_Of_Work= models.CharField(max_length=20, blank=True)
    Previous_Postion = models.CharField(max_length=50, blank=True)



    #HR Department Fields
    Department_Type=models.CharField(choices=Department_type, default=Department_type.Select, max_length=20)
    Department = models.CharField(choices=Department, default=Department.Select, max_length=20)
    Role = models.CharField(choices=Roles, default=Roles.Select, max_length=30)
    Weekoff = models.CharField(max_length=10,default="Sunday")
    Join_Date=models.DateField(max_length=15,blank=True,null=True)
    Left_Date=models.DateField(max_length=15,blank=True,null=True)
    Leave_Per_Month=models.IntegerField(null=True)
    Leave_Balance=models.IntegerField(null=True)
    Joining_Salary=models.IntegerField(null=True)

    def __str__(self):
        return str(self.Employee_ID)



class Daily_Attendance(models.Model):
    STATUS = Choices('Present', "Absent", "Leave", "Weekoff")
    Employee_Id=models.ForeignKey(Employees_Detail,on_delete=models.CASCADE)
    Time_in=models.DateTimeField(max_length=20)
    Time_out = models.DateTimeField(max_length=20, blank=True, null=True)
    Status=models.CharField(choices=STATUS, default=STATUS.Present, max_length=20)

class Employee_Payroll(models.Model):
    STATUS = Choices('Present', "Absent", "Leave", "Weekoff")

    Employee_ID= models.ForeignKey(Employees_Detail,on_delete=models.CASCADE)

    From= models.DateField(max_length=20,blank=True,null=True)
    To = models.DateField(max_length=20,blank=True,null=True)
    Basic=models.IntegerField()
    HRA = models.IntegerField()
    Other_Allowance = models.IntegerField()
    LTA = models.IntegerField()
    Incentive = models.IntegerField()
    Bonus = models.IntegerField()
    EPF= models.IntegerField()
    ESI = models.IntegerField()
    TDS = models.IntegerField()
    Other_Deductions = models.IntegerField()
    Annual_Leaves= models.IntegerField(null=True)

    def __str__(self):
        return str(self.Employee_ID)

