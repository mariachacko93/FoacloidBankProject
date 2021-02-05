from django import forms
from django.forms import ModelForm

from accounts.models import Transferdetails
from accounts.models import CreateAccount

class AccountCreateForm(forms.Form):
    personname=forms.CharField(max_length=120)
    accno = forms.IntegerField()
    acctype = forms.CharField(max_length=120)
    balance = forms.IntegerField()
    phonenumber = forms.IntegerField()
    mpin = forms.IntegerField()

class LoginForm(forms.Form):
    phonenumber = forms.CharField(max_length=12)
    mpin = forms.CharField(max_length=6)
    print(phonenumber,mpin)

class BalanceCheckForm(forms.Form):
    mpin = forms.CharField(max_length=6)
    def clean(self):
        clean_data=super().clean()
        mpin=clean_data.get("mpin")
        try:
            object=CreateAccount.objects.get(mpin=mpin)

            if object:
                pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)


class TransferAmountForm(ModelForm):
    class Meta:
        model=Transferdetails
        fields="__all__"

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        accno=cleaned_data.get("accno")
        amount=cleaned_data.get("amount")
        print(mpin,",",accno,",",amount)
        try:
            object=CreateAccount.objects.get(mpin=mpin)
            if(object):

        # for checking sufficent balance
                if(object.balance<amount ):
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)
        # for account validation
        try:
            object=CreateAccount.objects.get(accno=accno)
            if(object):
                pass
        except:
            msg="you have provided invalid accno"
            self.add_error("accno",msg)


class withdrawForm(ModelForm):
    class Meta:
        model=Transferdetails
        fields="__all__"


    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        accno = cleaned_data.get("accno")
        amount = cleaned_data.get("amount")
        print(mpin,",",accno,",",amount)

        # sufficent amount
        try:
            object=CreateAccount.objects.get(mpin=mpin)
            if object:
                if (object.balance<amount):
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                pass
        #     pin validation
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)

        # account validation
        try:
            object=CreateAccount.objects.get(accno=accno)
            if object:
                pass
        except:
            msg="please provide a valid account details"
            self.add_error("accno",msg)