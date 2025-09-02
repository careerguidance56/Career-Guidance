class HRForm(ModelForm):
    class Meta:
        Model=HRTable
        fields=['company name','address','number','email']