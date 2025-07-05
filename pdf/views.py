from django.shortcuts import render

from pdf.models import Profile

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

  return render(request, 'pdf/accept.html')