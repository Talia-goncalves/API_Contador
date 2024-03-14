from django.shortcuts import render
from django.http import JsonResponse
from .models import Dados

def receber_dados(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        dados = Dados.objects.create(
            sensor=data.get('Sensor'),
            botao=data.get('Botao'),
            liga_robo=data.get('LigaRobo'),
            reset_contador=data.get('ResetContador'),
            valor_contagem=data.get('Valor Contagem')
        )
        return JsonResponse({'status': 'Dados recebidos com sucesso!'})
    return JsonResponse({'error': 'Método não permitido'}, status=405)


def mostrar_dados(request):
    dados = Dados.objects.last()
    return render(request, 'index.html', {
        'sensor': dados.sensor,
        'botao': dados.botao,
        'liga_robo': dados.liga_robo,
        'reset_contador': dados.reset_contador,
        'valor_contagem': dados.valor_contagem
    })
