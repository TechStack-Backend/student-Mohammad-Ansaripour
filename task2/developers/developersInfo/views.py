from django.shortcuts import render

# Create your views here.
def devListView(request):
    return render(request,"developersInfo/developers_list.html")
