from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render ,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from homepage.models import Events
import openpyxl
import csv
import pandas as pd

class Page:
	def loginpage(request):
		logout(request)
		username=''
		password = ''
		error=False
		if request.POST:
                        username = request.POST.get('emp_username')
                        password = request.POST.get('emp_password')
                        user = authenticate(username=username, password=password)
                        if user is not None:
                                if user.is_active:
                                        login(request, user)
                                        return render(request, 'employee/homepage.html', {'username':username})
                                        
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
                return render(request, 'employee/orders.html', {"country":count,"method":ord_met,"line":p_l,"type":p_t,"year":y,"excel_data":excel_data,"row_count":row_count,"revenue":tot_rev})
		
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
                columns=['first_name','last_name','address','city','phone1','phone2','email','SKU_number','PriorityStatus','DateOfPurchase','Country']
                # iterating over the rows and
                # getting value from each cell in row
                for index, row in df.iterrows():
                        row_data = list()
                        row_count=row_count+1
                        for cell in columns:
                                row_data.append(row[cell])
                        excel_data.append(row_data)

                return render(request, 'employee/customers.html', {"excel_data":excel_data,"row_count":row_count})
                        
	
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

                df=pd.read_csv("ProductDB.csv")
                row_count=0
                excel_data = list()
                columns=['SKU_number','MRP','UnitsInProduction','UnitsSold','AvgRating']
                # iterating over the rows and
                # getting value from each cell in row
                for index, row in df.iterrows():
                        row_data = list()
                        row_count=row_count+1
                        for cell in columns:
                                row_data.append(row[cell])
                        excel_data.append(row_data)
#                tot_sold=df['UnitsSold'].sum()
 #               tot_prod=df['UnitsInProduction'].sum()
                return render(request, 'employee/products.html', {"excel_data":excel_data, "row_count":row_count})
		
	def calendarpage(request):
                event=list(Events.objects.values())
                return render(request, 'employee/calendar.html',{'eventdata':event})

	def logoutpage(request):
		message=True
		error=False
		return render(request, 'homepage/login.html',{'error':error,'message':message})


