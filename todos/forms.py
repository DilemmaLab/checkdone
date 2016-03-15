from django import forms
from django.utils import timezone
#from django.contrib.admin.widgets import AdminDateWidget # ''' Admin Datepicker ''' #
from functools import partial # Jquery Datepicker

DateInput = partial(forms.DateInput, {'class': 'datepicker form-control', 'required': True,}) # Jquery Datepicker
DateInputNonReq = partial(forms.DateInput, {'class': 'datepicker form-control', 'required': False,}) # Jquery Datepicker
DateTimeInput = partial(forms.DateTimeInput, {'class': 'form-control timepicker', 'required': True,}) # Jquery Datepicker
DateTimeInputNonReq = partial(forms.DateTimeInput, {'class': 'datetimepicker'}) # Jquery Datepicker
TimeInput = partial(forms.TimeInput, {'class': 'timepicker', 'required': True,}) # Jquery Datepicker

class AddNewForm(forms.Form):
    text = forms.CharField(required=True, max_length=100, label='Task*',
                           widget=forms.TextInput(attrs={'class':'form-control', 'id':'id_text1',
                                                         'placeholder': 'New task...', 'type': 'text',
                                                         'required': True,
                                                        }), ) # (REQUIRED)
    # ''' Admin Datepicker ''' #
    #deadline = forms.DateTimeField(required=True, label='Deadline*',
    #                               widget=AdminDateWidget, ) #  (REQUIRED) Or DateField(), if only Date is in Use.
    # ''' Admin Datepicker ''' #
    deadline = forms.DateTimeField(required=True, label='Deadline*', widget=DateTimeInput(), )
    check = forms.BooleanField(required=False, initial=False, label='Done?', label_suffix='',
                               widget=forms.CheckboxInput(attrs={'id':'id_check1',
                                                                     'type': 'checkbox',
                                                                    }), ) # (REQUIRED)
    donedate = forms.DateTimeField(required=False, label='Done on date',
                                   widget=DateInputNonReq(), ) # (Not nessessary) Or DateField(), if only Date is in Use.
    progress = forms.FloatField(required=False, min_value=0.0, max_value=100.0, label='Progress',
                                widget=forms.NumberInput(attrs={'class':'form-control', 'id':'id_progress1',
                                                                'placeholder': '0.0', 'type': 'number',
                                                               }), ) # (Not nessessary) % for progressbar.
    textexp = forms.CharField(required=False, label='Details',
                              widget=forms.Textarea(attrs={'class':'form-control', 'id':'id_textexp1',
                                                           'placeholder': 'Explain more detail (optional)...',
                                                           'cols':'50', 'rows':'5', }), )# (Not nessessary) % Expanded text explaination

    error_css_class = "form-control"
    #NullBooleanSelect = partial(forms.NullBooleanSelect, {'type': 'checkbox'})

    def clean_donedate(self):
        dt1 = self.cleaned_data['donedate']
        dt2=timezone.now()
        error_list = ["Date, when task was done, ", "should be less than or equal to current date."]
        if dt1:
            if dt1>dt2:
                raise forms.ValidationError(error_list)
        return
