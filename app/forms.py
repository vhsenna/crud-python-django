from django.forms import ModelForm
from app.models import Cadastro


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'telefone', 'endereco', 'cpf']

    # Sobrescreve o método __init__
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
