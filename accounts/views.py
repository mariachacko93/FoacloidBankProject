from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import CreateAccount,Transferdetails
from accounts.forms import AccountCreateForm,LoginForm,BalanceCheckForm,TransferAmountForm,withdrawForm,DepositForm


# Create your views here.

def transfer(request):
    form=TransferAmountForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TransferAmountForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            accno=form.cleaned_data.get("accno")
            try:
                object=CreateAccount.objects.get(mpin=mpin)
                bal=object.balance-amount
                object.balance=bal
                object.save()
                object1 = CreateAccount.objects.get(accno=accno)
                bal1=object1.balance+amount
                object1.balance=bal1
                object1.save()

            except Exception:
                context["form"] = form
                return render(request, "accounts/transferamount.html", context)

            form.save()


            return redirect("balance")
        else:
            context["form"]=form
            return render(request, "accounts/transferamount.html", context)

    return render(request,"accounts/transferamount.html",context)



def createAccount(request):
    form=AccountCreateForm()
    context={}
    context["form"]=form
    if (request.method=='POST'):
        form=AccountCreateForm(request.POST)
        if form.is_valid():
            personname=form.cleaned_data.get("personname")
            accno=form.cleaned_data.get("accno")
            acctype=form.cleaned_data.get("acctype")
            balance=form.cleaned_data.get("balance")
            phonenumber=form.cleaned_data.get("phonenumber")
            mpin=form.cleaned_data.get("mpin")

            print(personname,",",accno,",",acctype,",",balance,",",phonenumber,",",mpin)
            account=CreateAccount(personname=personname,accno=accno,acctype=acctype,balance=balance,phonenumber=phonenumber,mpin=mpin)
            account.save()

            return redirect("accountlist")
    return  render(request,"accounts/createaccount.html",context)

def accountList(request):
    account=CreateAccount.objects.all()
    context={}
    context["account"]=account
    return render(request,"accounts/accountlist.html",context)


def loginView(request):
    form=LoginForm()
    context={}
    context["form"]=form
    form=LoginForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            phone=form.cleaned_data.get("phonenumber")
            mpin=form.cleaned_data.get("mpin")

            try:

                object=CreateAccount.objects.get(phonenumber=phone)
                if((object.phonenumber==phone) & (object.mpin==mpin)):
                    print("user exist")
                return redirect("homein")

            except Exception as e:
                print("invalid user")
                context["form"]=form
                return render(request,"accounts/login.html",context)

    return render(request, "accounts/login.html",context)

def Homein(request):
    return render(request, "accounts/homein.html")


def balanceEnq(request):
    form=BalanceCheckForm()
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=BalanceCheckForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            try:

                object=CreateAccount.objects.get(mpin=mpin)
                context["balance"]=object.balance

                return render(request,"accounts/checkbalance.html",context)
            except Exception as e:
                context["form"]=form
                return render(request,"accounts/checkbalance.html",context)


    return render(request,"accounts/checkbalance.html",context)

def Home(request):
    return render(request, "accounts/accounthome.html")


def accountActivity(request):
    form=BalanceCheckForm()
    context={}
    context["form"]=form
    if (request.method=="POST"):
        form=BalanceCheckForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")

            trans=Transferdetails.objects.filter(mpin=mpin)

            context["transaction"]=trans
            return render(request, "accounts/accounthistory.html", context)

    return render(request,"accounts/accounthistory.html",context)


def withdrawAmount(request):
        form=withdrawForm()
        context={}
        context["form"]=form
        if request.method == "POST":
            form = withdrawForm(request.POST)
            if form.is_valid():
                mpin = form.cleaned_data.get("mpin")
                amount = form.cleaned_data.get("amount")
                try:
                    object = CreateAccount.objects.get(mpin=mpin)
                    bal = object.balance - amount
                    object.balance = bal
                    object.save()

                except Exception:
                    context["form"] = form
                    return render(request, "accounts/withdrawamount.html",context)

                form.save()

                return redirect("balance")
            else:
                context["form"] = form
                return render(request, "accounts/withdrawamount.html", context)

        return render(request, "accounts/withdrawamount.html", context)


def DepositView(request):
        form=DepositForm()
        context={}
        context["form"]=form
        if request.method == "POST":
            form = DepositForm(request.POST)
            if form.is_valid():
                mpin = form.cleaned_data.get("mpin")
                amount = form.cleaned_data.get("amount")
                try:
                    object = CreateAccount.objects.get(mpin=mpin)
                    bal = object.balance + amount
                    object.balance = bal
                    object.save()

                except Exception:
                    context["form"] = form
                    return render(request, "accounts/deposit.html",context)

                form.save()

                return redirect("balance")
            else:
                context["form"] = form
                return render(request, "accounts/deposit.html", context)

        return render(request, "accounts/deposit.html", context)