from django.forms import ModelForm
from CareerGuidanceApp.models import HRTable,jobTable


class HRForm(ModelForm):
    class Meta:
        model=HRTable
        fields=['Company_name','Address','phone_no','email_id']
class JobForm(ModelForm):
    class Meta:
        model=jobTable
        fields=['Job_name','phone_no','Qualification','Experience']