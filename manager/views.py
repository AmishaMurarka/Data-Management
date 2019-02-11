from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render ,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from homepage.models import Events
from django.core.mail import send_mail
from django.core.files import File 
import openpyxl
import csv
import pandas as pd

class Page:
	def admin_login(request):
		logout(request)
		username=''
		password = ''
		error=False
		if request.POST:
                        username = request.POST.get('admin_username')
                        password = request.POST.get('admin_password')
                        user = authenticate(username=username, password=password)
                        if user is not None:
                                if user.is_active:
                                        login(request, user)
                                        return render(request, 'manager/admin_homepage.html', {'username':username})
                                        
		error=True
		message=False
		return render(request, 'homepage/login.html', {'error':error,'message':message})

	def orderspage(request):
                if request.POST:
                        ret=request.POST.get('ret')
                        or_no=request.POST.get('or_no')
                        prod_line=request.POST.get('prod_line')
                        prod_typ=request.POST.get('prod_typ')
                        year=request.POST.get('year')
                        rev=request.POST.get('rev')
                        qt=request.POST.get('qt')
                        data=[ret,or_no,prod_line,prod_typ,year,rev,qt]
                        with open('SalesOrder.csv', 'a') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)

                df=pd.read_csv("SalesOrder.csv")
                row_count=0
                advrep=False
                excel_data = list()
                tot_rev=0
                columns=['RetailerCountry','Ordermethodtype','Productline','Producttype','Year','Revenue','Quantity']
                # iterating over the rows and
                # getting value from each cell in row
                for index, row in df.iterrows():
                        row_data = list()
                        row_count=row_count+1
                        for cell in columns:
                                row_data.append(row[cell])
                        excel_data.append(row_data)
                tot_rev=df['Revenue'].sum()
                count=len(df.groupby('RetailerCountry'))
                ord_met=len(df.groupby('Ordermethodtype'))
                p_l=len(df.groupby('Productline'))
                p_t=len(df.groupby('Producttype'))
                y=len(df.groupby('Year'))

                country_name=df.groupby('RetailerCountry').groups.keys()
                country_ord=df.groupby('RetailerCountry')['RetailerCountry'].count()
                country_wise_ord=Page.form_dict(country_name,country_ord)

                method_name=df.groupby(['RetailerCountry','Ordermethodtype']).groups.keys()
                country_ord=df.groupby(['RetailerCountry','Ordermethodtype'])['Ordermethodtype'].count()
                country_wise_method=Page.form_dict(method_name,country_ord)

                method2_name=df.groupby(['RetailerCountry','Ordermethodtype','Productline']).groups.keys()
                country2_ord=df.groupby(['RetailerCountry','Ordermethodtype','Productline'])['Ordermethodtype'].count()
                country2_wise_method=Page.form_dict(method2_name,country2_ord)

                years=df.groupby('Year').groups.keys()
                year_revenue=df.groupby('Year')['Revenue'].sum()
                yearly_rev=Page.form_dict(years,year_revenue)
                return render(request, 'manager/admin_orders.html', {"yearly_rev":yearly_rev,"country2_wise_method":country2_wise_method,"country_wise_method":country_wise_method,"country_wise_ord":country_wise_ord,"country":count,"method":ord_met,"line":p_l,"type":p_t,"year":y,"excel_data":excel_data,"row_count":row_count,"revenue":tot_rev})
        
	def customerpage(request):
                if request.POST:
                        fn=request.POST.get('f_n')
                        ln=request.POST.get('l_n')
                        address=request.POST.get('addr')
                        city=request.POST.get('city')
                        c1=request.POST.get('c1')
                        c2=request.POST.get('c2')
                        em=request.POST.get('email')
                        sku=request.POST.get('sku')
                        stat=request.POST.get('stat')
                        pdate=request.POST.get('pdate')
                        con=request.POST.get('country')
                        data=[fn,ln,address,city,c1,c2,em,sku,stat,pdate,con]
                        with open('Customer DB.csv', 'a') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)
                """#if "GET" == request.method:
                #       return render(request, 'employee/customers.html', {})
                #else:
                #excel_file = request.FILES["excel_file"]
                excel_file = 'C:\\Users\\Amisha\\Desktop\\CustomerDB.xlsx'
                # you may put validations here to check extension or file size
                wb = openpyxl.load_workbook(excel_file)
                # getting a particular sheet by name out of many sheets
                worksheet = wb["Customer DB"]
                print(worksheet)"""
                df=pd.read_csv("Customer DB.csv")
                row_count=0
                excel_data = list()
                country_wise_custom=list()
                columns=['first_name','last_name','address','city','phone1','phone2','email','SKU_number','PriorityStatus','DateOfPurchase','Country']
                # iterating over the rows and
                # getting value from each cell in row
                for index, row in df.iterrows():
                        row_data = list()
                        row_count=row_count+1
                        for cell in columns:
                                row_data.append(row[cell])
                        excel_data.append(row_data)

                country_name=df.groupby('Country').groups.keys()
                country_custom=df.groupby('Country')['Country'].count()
                country_wise_custom=Page.form_dict(country_name,country_custom)

                sku_cust=df.groupby('SKU_number')['SKU_number'].count()
                sku_prod=df.groupby('SKU_number').groups.keys()
                sku_wise_cust=Page.form_dict(sku_prod,sku_cust)

                priority=df.groupby('PriorityStatus').groups.keys()
                cust_pri=df.groupby('PriorityStatus')['first_name'].count()
                pri_wise_cust=Page.form_dict(priority,cust_pri)

                return render(request, 'manager/admin_customers.html', {"cust_pri":pri_wise_cust,"sku_cust":sku_wise_cust,"excel_data":excel_data,"row_count":row_count,"country_customers":country_wise_custom})
                        
	def form_dict(keys,values):
                res=dict(zip(keys, values))
                return res
                
	def productpage(request):
                if request.POST:
                        sku=request.POST.get('sku')
                        mrp=request.POST.get('mrp')
                        pu=request.POST.get('p_units')
                        su=request.POST.get('s_units')
                        r=request.POST.get('rate')
                        data=[sku,mrp,pu,su,r]
                        with open('ProductDB.csv', 'a') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)

                #df=pd.read_csv("ProductDB1.csv")
                df=pd.read_csv("ProductDB2.csv")
                #df=pd.read_csv("ProductDB3.csv")
                row_count=0
                excel_data = list()
                columns=['SKU_number','MRP','UnitsInProduction','UnitsSold','AvgRating','Year']
                # iterating over the rows and
                # getting value from each cell in row
                for index, row in df.iterrows():
                        row_data = list()
                        row_count=row_count+1
                        for cell in columns:
                                row_data.append(row[cell])
                        excel_data.append(row_data)
                tot_sold=df['UnitsSold'].sum()
                tot_prod=df['UnitsInProduction'].sum()

                prod_rates=df.groupby('AvgRating').groups.keys()
                rating=df.groupby('AvgRating')['SKU_number'].count()
                prod_rating=Page.form_dict(prod_rates,rating)

                #obtain list of sku's
                skul=df['SKU_number'].unique().tolist()
                #skulcnt=len(df['SKU_number'].unique().tolist())
                countsku=len(skul)

                #obtain avg sales of each sku sold over 3 years
                
                #avgskusale=round(df.groupby('SKU_number')['TotalUnits'].sum()/5,2)
                avgskusale=round(df.groupby('SKU_number')['TotalUnits'].sum()/3,2)
                #avgskusale=round(df.groupby('SKU_number')['TotalUnits'].sum()/4,2)
                
                avgskusale=avgskusale.tolist()

                #to find avg number of ALL units sold over the years
                totalavg=round(df['TotalUnits'].sum()/(df['SKU_number'].count()),2)
                #to classify on basis of priority

                priordict={}
                for i in range(countsku):
                        if(avgskusale[i]>=totalavg):
                                priordict[skul[i]]='Priority'
                        else:
                                priordict[skul[i]]='Non-Priority'

                #obtain avg sales of each sku sold over 3 years
                
                #avgskusale2=round(df.groupby('SKU_number')['Revenue'].sum()/5,2)
                avgskusale2=round(df.groupby('SKU_number')['Revenue'].sum()/3,2)
                #avgskusale2=round(df.groupby('SKU_number')['Revenue'].sum()/4,2)
                
                avgskusale2=avgskusale2.tolist()

                #to find avg number of ALL units sold over the years
                totalavg2=round(df['Revenue'].sum()/(df['SKU_number'].count()),2)
                #to classify on basis of priority

                priordict_rev={}
                for i in range(countsku):
                        if(avgskusale2[i]>=totalavg2):
                                priordict_rev[skul[i]]='Priority'
                        else:
                                priordict_rev[skul[i]]='Non-Priority'


                return render(request, 'manager/admin_products.html', {"priordict_rev":priordict_rev,"skulcnt":countsku,"priordict":priordict,"prod_rating":prod_rating,"excel_data":excel_data,"units_sold":tot_sold,"units_prod":tot_prod,"row_count":row_count})
				
	def contactpage(request):
                if request.POST:
                        mail=True
                        name=request.POST.get('name')
                        country=request.POST.get('country')
                        query=request.POST.get('subject')
                        query_final="Name of Sender:"+name+"\nCountry Of Sender:"+country+"\n\nQuery:\n"+query
                        subject='Query'
                        sender='amishamurarka@gmail.com'
                        send_mail(subject, query_final, sender, ['abhinayarao98@gmail.com'])
                        return render(request, 'manager/contact.html', {'mail':mail})
                mail=False
                return render(request, 'manager/contact.html', {'mail':mail})
				
	def calendarpage(request):
		event=list(Events.objects.values())
		return render(request, 'manager/admin_calendar.html',{'eventdata':event})
				
	def logoutpage(request):
		message=True
		error=False
		return render(request, 'homepage/login.html',{'error':error,'message':message})
		
	def downloadcustomer(request):
                with open('Customer DB.csv', 'rb') as myfile:
                        response = HttpResponse(myfile, content_type='text/csv')
                        response['Content-Disposition'] = 'attachment; filename=CustomerDB.csv'
                        return response
						
	def downloadorder(request):
                with open('SalesOrder.csv', 'rb') as myfile:
                        response = HttpResponse(myfile, content_type='text/csv')
                        response['Content-Disposition'] = 'attachment; filename=OrderDB.csv'
                return response
				
	def downloadproduct(request):
                with open('ProductDB1.csv', 'rb') as myfile:
                        response = HttpResponse(myfile, content_type='text/csv')
                        response['Content-Disposition'] = 'attachment; filename=ProductDB.csv'
                        return response



        
