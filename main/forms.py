from django import forms
from .models import TestTable
import uuid
from datetime import datetime


class TestForm(forms.ModelForm):
    # Name=forms.CharField(max_length=30, required=True)
    # Position=forms.CharField( required=True)
    # Date_of_Birth=forms.DateField( required=True)
    # Date_of_Joining=forms.DateField(required=True)
    # Salary=forms.FloatField(required=True)
    # Profile_image=forms.FileField(required=True)
    # def save(self, commit = True):
    #     # print(self.cleaned_data)
    #     instance = super().save(commit=False)
    #     instance.id=str(uuid.uuid5(uuid.NAMESPACE_URL, url))[:8]
    #     instance.name=self.cleaned_data["name"]
    #     instance.position=self.cleaned_data["position"]
    #     # print(self.cleaned_data["doj"])
    #     instance.dob=self.cleaned_data["dob"]
    #     instance.doj=self.cleaned_data["doj"]
    #     instance.salary=self.cleaned_data["salary"]
    #     instance.profile_image=self.cleaned_data['profile_image']
    #     if commit:
    #         instance.save()
    #         self._save_m2m()
        
    #     return instance    
    class Meta:
        Position_Choices=(("Ground Staff","Ground Staff"),("Pilot","Pilot"),("Cabin Crew","Cabin Crew"),("Engineer","Engineer"),("RnD","RnD"),("Cleaning Crew","Cleaning Crew"))
        Gender_Choices=(
            ('Male','Male'),('Female','Female'),('Other','Other'),('Not disclosing','Not disclosing')
        )
        PrefferedShifts_Choices=(
            ('early-morning','early morning'),('morning','morning'),('noon','noon'),('afternoon','afternoon'),('early evening','early evening'),('late evening','late evening'),('night','night')
        )
        model = TestTable
        fields = (
            "id","name",'profile_image',"position","dob","gender","bio","doj","salary","preffered_shifts","permanent_employee","age"
        )
        widgets = {
        'doj': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','required':True}),
        'dob': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','required':True}),
        'profile_image':forms.ClearableFileInput(),
        'position': forms.Select(choices=Position_Choices),
        'preffered_shifts':forms.CheckboxSelectMultiple(choices=PrefferedShifts_Choices),
        'gender': forms.RadioSelect(choices=Gender_Choices),
        'permanent_employee':forms.CheckboxInput(),
        'salary':forms.NumberInput(),
        'age':forms.NumberInput(),
        'id':forms.HiddenInput()
        }

class TestForm1(forms.ModelForm):
    # Name=forms.CharField(max_length=30, required=True)
    # Position=forms.CharField( required=True)
    # Date_of_Birth=forms.DateField( required=True)
    # Date_of_Joining=forms.DateField(required=True)
    # Salary=forms.FloatField(required=True)
    # Profile_image=forms.FileField(required=True)
    # def save(self, commit = True):
    #     # print(self.cleaned_data)
    #     instance = super().save(commit=False)
    #     instance.id=str(uuid.uuid5(uuid.NAMESPACE_URL, url))[:8]
    #     instance.name=self.cleaned_data["name"]
    #     instance.position=self.cleaned_data["position"]
    #     # print(self.cleaned_data["doj"])
    #     instance.dob=self.cleaned_data["dob"]
    #     instance.doj=self.cleaned_data["doj"]
    #     instance.salary=self.cleaned_data["salary"]
    #     instance.profile_image=self.cleaned_data['profile_image']
    #     if commit:
    #         instance.save()
    #         self._save_m2m()
        
    #     return instance    
    class Meta:
        Position_Choices=(("Ground Staff","Ground Staff"),("Pilot","Pilot"),("Cabin Crew","Cabin Crew"),("Engineer","Engineer"),("RnD","RnD"),("Cleaning Crew","Cleaning Crew"))
        Gender_Choices=(
            ('Male','Male'),('Female','Female'),('Other','Other'),('Not disclosing','Not disclosing')
        )
        PrefferedShifts_Choices=(
            ('early-morning','early morning'),('morning','morning'),('noon','noon'),('afternoon','afternoon'),('early evening','early evening'),('late evening','late evening'),('night','night')
        )
        model = TestTable
        fields = (
            "id","name",'profile_image',"position","dob","gender","bio","doj","salary","preffered_shifts","permanent_employee","age"
        )
        widgets = {
        'profile_image':forms.ClearableFileInput(),
        'position': forms.Select(choices=Position_Choices),
        'preffered_shifts':forms.CheckboxSelectMultiple(choices=PrefferedShifts_Choices),
        'permanent_employee':forms.CheckboxInput(),
        'salary':forms.NumberInput(),
        'age':forms.NumberInput(),
        }