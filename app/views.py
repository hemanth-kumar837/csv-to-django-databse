from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
import csv

def Create_bank(request):
    with open('C:\\Users\\DELL\\Desktop\\Django projects\\hemanth\\Scripts\\project41\\app\\bank.csv','r')as FO: 
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()


    return HttpResponse(' bank inserted successfully')


def insert_branch(self):
    with open('C:\\Users\\DELL\\Desktop\\Django projects\\hemanth\\Scripts\\project41\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                cn=i[4]
                ci=i[5]
                di=i[6]
                st=i[7]

                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contat=cn,city=ci,district=di,state=st)
                BRO.save()

    return HttpResponse('branch inserted successfully')
