from django import forms
from candidate.models import Candidate

def unique_skills():
    skills_list = []
    for obj in Candidate.objects.exclude(skills__isnull=True):
        skills_list += obj.skills.split(",")
    skills_list = [i.strip() for i in skills_list]
    unique_skills = list(set(skills_list))
    unique_skills.sort()
    x = []
    x.append(("","Select Skill"))
    for i in unique_skills:
        x.append((i,i))
    return x

def unique_location():
    loc = []
    for obj in Candidate.objects.all():
        loc += obj.preferred_loc.split(",")
        loc.append(obj.current_loc)
    loc = [i.strip() for i in loc]
    loc = list(set(loc))
    loc.sort()
    x = []
    x.append(("","Select Location"))
    for i in loc:
        x.append((i,i))
    return x

def work_exp_range():
    work_exp = []
    for obj in Candidate.objects.all():
        work_exp.append(obj.work_exp)
    work_exp = list(set(work_exp))
    work_exp = [i for i in range(0, int(max(work_exp)))]
    x = []
    x.append(("","Select Work Exp"))
    for i in work_exp:
        x.append((i,i))
    return x

class CandidateForm(forms.Form):
    skills = forms.CharField(
        max_length=2000,
        label="Select Skills",
        widget=forms.Select(choices=unique_skills())
    )
    loc = forms.CharField(
        max_length=2000,
        label="Select Location",
        widget=forms.Select(choices=unique_location())
    )
    work_exp = forms.IntegerField(
        label="Select Work Experience",
        widget=forms.Select(choices=work_exp_range())
    )