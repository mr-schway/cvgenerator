from django.shortcuts import redirect, render

from pdf.models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io 

# Create your views here.
def accept(request):
  if request.method == "POST":
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    about = request.POST.get("about", "")
    degree = request.POST.get("degree", "")
    school = request.POST.get("school", "")
    university = request.POST.get("university", "")
    experience = request.POST.get("experience", "")
    skills = request.POST.get("skills", "")

    profile = Profile(
      name = name,
      email = email,
      phone = phone,
      about = about,
      degree = degree,
      school = school,
      university = university,
      experience = experience,
      skills = skills
    )
    profile.save()
    return redirect('cv', id=profile.id)

  return render(request, 'pdf/accept.html')

def cv(request, id):
  profile = Profile.objects.get(pk = id)
  template = loader.get_template('pdf/cv.html')
  html = template.render({'profile': profile})
  options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
  }
  pdf = pdfkit.from_string(html, False, options)
  response = HttpResponse(pdf, content_type = 'application/pdf')
  response['Content-Disposition'] = 'attachment'
  filename = "cv.pdf"
  return response

def listView(request):
  profiles = Profile.objects.all()
  return render(request, 'pdf/listView.html', {'profiles': profiles})