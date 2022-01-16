from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from app.forms import CadastroForm
from app.models import Cadastro
import datetime
from weasyprint import HTML
import tempfile


# Create your views here.
def home(request):
    data = {}
    data['db'] = Cadastro.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CadastroForm()
    return render(request, 'form.html', data)


def create(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    data['form'] = CadastroForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Relatorio' + str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    cadastro = Cadastro.objects

    html_string = render_to_string('export-pdf.html', {'cadastro': cadastro})
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
