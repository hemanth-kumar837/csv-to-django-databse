from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
from app.models import *
import csv
def insert_business(self):
    with open('C:\\Users\\DELL\\Desktop\\Django projects\\hemanth\\Scripts\\project42\\app\\Business-employment-data-september-2022-quarter-csv.csv') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            sr=i[0].strip()
            BO=Business(Series_reference=sr)
            if BO:
                p=i[1]
                dv=i[2]
                s=i[3]
                st=i[4]
                u=i[5]
                m=i[6]
                su=i[7]
                gr=i[8]
                st1=i[9]
                st2=i[10]
                st3=i[11]

                BEO=Business(Series_reference=sr[0],Period=p,Data_value=dv,Suppressed=s,Status=s,Units=u,Magnitude=m,Subject=s,Group=gr,Series_title_1=st1,Series_title_2=st2,Series_title_3=st3)
                BEO.save()
    return HttpResponse('business  inserted successfully ')
