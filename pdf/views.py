from django.shortcuts import render

# Create your views here.
def accept(request):
  return render(request, 'pdf/accept.html')