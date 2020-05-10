from django.shortcuts import render

# Create your views here.
# request is HttpRequestObject that is created whenever a page is loaded
# render looks for HTML templates inside a directory called templates
def view_table(request):
	return render(request, 'table.html', {})
