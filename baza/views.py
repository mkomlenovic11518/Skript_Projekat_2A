from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Proizvodjac
from .models import Roba
from .forms import ProizvodjacForm
from .forms import RobaForm
from .forms import SignupForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Script projekat 2'})
    else:
        return redirect('demo_app:proizvodjaci')

def registracija(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            #user.is_active = False
            user.save()
            #current_site = get_current_site(request)
            #mail_subject = 'Activate your blog account.'
            #message = render_to_string('acc_active_email.html', {
                #'user': user,
                #'domain': current_site.domain,
                #'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                #'token': account_activation_token.make_token(user),
            #})
            #to_email = form.cleaned_data.get('email')
            #email = EmailMessage(
               # mail_subject, message, to=[to_email]
            #)
            #email.send()
            return redirect('demo_app:proizvodjaci')

    else:
        form = SignupForm()
    return render(request, 'registration/registracija.html', {'form': form})

@login_required
def proizvodjaci(req):
    tmp = Proizvodjac.objects.all()
    return render(req, 'proizvodjaci.html', {'proizvodjaci': tmp})


@login_required
def proizvodjac(req, id):
    tmp = get_object_or_404(Proizvodjac, id=id)
    return render(req, 'proizvodjac.html', {'proizvodjac': tmp, 'page_title': tmp.naziv_proizvodjac})


@permission_required('demo_app.change_proizvodjac')
def edit(req, id):
    if req.method == 'POST':
        form = ProizvodjacForm(req.POST)

        if form.is_valid():
            a = Proizvodjac.objects.get(id=id)
            a.naziv_proizvodjac = form.cleaned_data['naziv_proizvodjac']
            a.sifra_proizvodjac = form.cleaned_data['sifra_proizvodjac']
            a.save()
            return redirect('demo_app:proizvodjaci')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Proizvodjac.objects.get(id=id)
        form = ProizvodjacForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('demo_app.add_proizvodjac')
def new(req):
    if req.method == 'POST':
        form = ProizvodjacForm(req.POST)

        if form.is_valid():
            a = Proizvodjac(naziv_proizvodjac=form.cleaned_data['naziv_proizvodjac'], sifra_proizvodjac=form.cleaned_data['sifra_proizvodjac'], owner=req.user)
            a.save()
            return redirect('demo_app:proizvodjaci')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = ProizvodjacForm()
        return render(req, 'new.html', {'form': form})

@login_required
def robe(req):
    tmp = Roba.objects.all()
    return render(req, 'robe.html', {'robe': tmp})

@login_required
def robe_p(req,id):
    queryset = Roba.objects.filter(proizvodjac=id)
    return render(req, 'robe_p.html', {'robe_p': queryset})

@login_required
def roba(req, id):
    tmp = get_object_or_404(Roba, id=id)
    return render(req, 'roba.html', {'roba': tmp, 'page_title': tmp.naziv_robe})

@permission_required('demo_app.add_roba')
def new_roba(req):
    if req.method == 'POST':
        form = RobaForm(req.POST)

        if form.is_valid():
            a = Roba(naziv_robe=form.cleaned_data['naziv_robe'], sifra_robe=form.cleaned_data['sifra_robe'],kolicina=form.cleaned_data['kolicina'],proizvodjac=form.cleaned_data['proizvodjac'],owner=req.user)
            a.save()
            return redirect('demo_app:robe')
        else:
            return render(req, 'new_roba.html', {'form': form})
    else:
        form = RobaForm()
        return render(req, 'new_roba.html', {'form': form})

@permission_required('demo_app.change_roba')
def edit_roba(req, id):
    if req.method == 'POST':
        form = RobaForm(req.POST)

        if form.is_valid():
            a = Roba.objects.get(id=id)
            a.naziv_robe = form.cleaned_data['naziv_robe']
            a.sifra_robe = form.cleaned_data['sifra_robe']
            a.kolicina = form.cleaned_data['kolicina']
            a.proizvodjac=form.cleaned_data['proizvodjac']
            a.save()
            return redirect('demo_app:robe')
        else:
            return render(req, 'edit_roba.html', {'form': form, 'id': id})

    else:
        a = Roba.objects.get(id=id)
        form = RobaForm(instance=a)
        return render(req, 'edit_roba.html', {'form': form, 'id': id})

@permission_required('demo_app.delete_roba')
def delete_roba(req, id):
    tmp = get_object_or_404(Roba, id=id)
    tmp.delete()
    return render(req, 'robe.html')

@permission_required('demo_app.delete_proizvodjac')
def delete_proizvodjac(req, id):
    tmp = get_object_or_404(Proizvodjac, id=id)
    tmp.delete()
    return render(req, 'proizvodjaci.html')

#def broj(request, br=0):
#    return HttpResponse('Broj' + str(br))

#def rec(request, r):
#   return HttpResponse('String:' + r)

#def params(request):
#    return HttpResponse('Params:' + str([str(k) + ':' + str(v) for k, v in request.GET.items()]))

#def regex(request,godina, mesec):
 #   return HttpResponse('Godina:' + godina + ' Mesec:'+ mesec)

#def hello(request):
 #   return render(request,'baza/hello.html')