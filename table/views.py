from django.shortcuts import render
from table.models import Table
from .forms import AddDataForms
from django.shortcuts import redirect
import os
import csv

# Create your views here.
# request is HttpRequestObject that is created whenever a page is loaded
# render looks for HTML templates inside a directory called templates

def view_table(request):


	with open('../voyce/voyce.csv') as csvfile:

		next(csvfile)

		data = csv.reader(csvfile, delimiter=',')

		for items in data:


			facility = items[0]
			type = items[1]

			number_beds = items[2]
			region = items[3]
			address = items[4]
			city = items[5]
			state = items[6]
			zip = items[7]
			telefone = items[8]
			fax = items[9]
			admin = items[10]
			admin_email = items[11]
			sw = items[12]
			sw_email = items[13]
			markt = items[14]
			markt_email = items[15]

			user = Table.objects.get_or_create(facility=facility,
				type=type,
				number_beds=number_beds,
				region=region,
				address=address,
				city=city,
				state=state,
				zip=zip,
				telefone=telefone,
				fax=fax,
				admin=admin,
				admin_email=admin_email,
				sw=sw,
				sw_email=sw_email,
				markt=markt,
				markt_email=markt_email
				)
	
	users = Table.objects.all()

	context = {
		'users': users
	}
	return render(request, 'table.html', context)

def add_data(request):
	form = AddDataForms()
	if request.method == 'POST':
		form = AddDataForms(request.POST)
		if form.is_valid():
			form.save()

			return redirect('view_table')
	#users1 = Table.objects.all()
	context = {
		#'users': users1,
		'form': form,
	}

	return render(request, 'newdata.html', context)


'''
number_beds = form.cleaned_data["number_beds"],
region = form.cleaned_data["region"],
address = form.cleaned_data["address"],
city = form.cleaned_data["city"],
state = form.cleaned_data["state"],
zip = form.cleaned_data["zip"],
telefone = form.cleaned_data["telefone"],
fax = form.cleaned_data["fax"],
admin = form.cleaned_data["admin"],
admin_email = forms.cleaned_data["admin_email"],
sw = form.cleaned_data["sw"],
sw_email = forms.cleaned_data["sw_email"],
markt = form.cleaned_data["markt"],
markt_email = forms.cleaned_data["markt_email"]
'''

'''
<td>{{user.number_beds}}</td>
<td>{{user.region}}</td>
<td>{{user.address}}</td>
<td>{{user.city}}</td>
<td>{{user.state}}</td>
<td>{{user.zip}}</td>
<td>{{user.telefone}}</td>
<td>{{user.fax}}</td>
<td>{{user.admin}}</td>
<td>{{user.admin_email}}</td>
<td>{{user.sw}}</td>
<td>{{user.sw_email}}</td>
<td>{{user.markt}}</td>
<td>{{user.martk_email}}</td>
'''

'''
<th scope="col">Number of Beds</th>
<th scope="col">Region</th>
<th scope="col">Address</th>
<th scope="col">City</th>
<th scope="col">State</th>
<th scope="col">Zip</th>
<th scope="col">Telefone</th>
<th scope="col">Fax</th>
<th scope="col">Admin</th>
<th scope="col">Admin Email</th>
<th scope="col">SW</th>
<th scope="col">SW Email</th>
<th scope="col">Markt/Adminssion</th>
<th scope="col">Markt/Adminssion Email</th>
'''


