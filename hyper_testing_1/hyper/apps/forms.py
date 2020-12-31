from django import forms
# from basic_app.models import UserProfileInfo EXAMPLE
from hyper.apps.models import Link, Project, Tag, Task, Comment

# EXAMPLE
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model = User
#         fields = ('username', 'email', 'password')

class NewTagForm(forms.ModelForm):

    class Meta():
        model= Tag
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NewTagForm, self).__init__(*args, **kwargs)
        # modify field styling attributes like dis
        self.fields['name'].widget.attrs.update({'type': "text", 'id': "new_tag", 'class': "form-control", 'placeholder': "Enter Tag"})


class NewProjectForm(forms.ModelForm):
    # date formats must be specified both here and in widget attributes!!
    # date formats must match or date error will cause form to fail validation
    start_date = forms.DateField(input_formats=['%d-%m-%Y'])
    end_date = forms.DateField(input_formats=['%d-%m-%Y'])
    budget = forms.DecimalField(required=False)


    class Meta():
        model = Project
        fields ='__all__'
        # fields = ('title', 'desc', 'start_date', 'end_date')

    # data claening example, makign sure end date is greater than start date
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if end_date < start_date:
            msg = 'End date should be greater than start date'
            # adds error to field in form to be displayed alongside, see template for how errors are dsiaplayed (per each field )
            self.add_error('end_date', msg)

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(NewProjectForm, self).__init__(*args, **kwargs)
        # modify field styling attributes like dis
        self.fields['title'].widget.attrs.update({'type': "text", 'id': "projectname", 'class': "form-control", 'placeholder': "Enter project name"})
        self.fields['desc'].widget.attrs.update({'class': "form-control", 'id': "project-overview", 'rows': "5", 'placeholder': "Enter some brief about project.."})
        self.fields['start_date'].widget.attrs.update({'type': "text", 'class': "form-control", 'data-provide': "datepicker", 'data-date-format': "d-m-yyyy", 'data-date-autoclose':"true"})
        self.fields['end_date'].widget.attrs.update({'type': "text", 'class': "form-control", 'data-provide': "datepicker", 'data-date-format': "d-m-yyyy", 'data-date-autoclose':"true"})
        self.fields['budget'].widget.attrs.update({'type': "text", 'id': "project-budget", 'class': "form-control", 'placeholder': "Enter project budget"})
        self.fields['status'].widget.attrs.update({'class': "form-control select2", 'data-toggle': "select2"})
