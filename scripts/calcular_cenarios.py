"""Modelo acadêmico Netrunner OT. Executar com Python 3, sem dependências.

Valores em reais. Cenários estabilizados de 2026, não apuração fiscal real.
RBT12 é receita mensal x 12; não simula regras de início de atividade.
"""
from math import ceil

FAIXAS_V = [(180000, .155, 0), (360000, .18, 4500),
            (720000, .195, 9900), (1800000, .205, 17100)]


def aliquota(rbt12):
    if rbt12 <= 0:
        return 0
    for limite, nominal, deducao in FAIXAS_V:
        if rbt12 <= limite:
            return (rbt12 * nominal - deducao) / rbt12
    raise ValueError('Modelo limitado a RBT12 de R$ 1,8 milhão.')


def calcular(basico, profissional, fixos, depreciacao=0, desconto=0, custo_hora=100):
    receita = (basico * 990 + profissional * 1990) * (1 - desconto)
    horas = basico * 2 + profissional * 4
    variavel = horas * custo_hora + basico * 30 + profissional * 60
    imposto = receita * aliquota(receita * 12)
    pagamento = receita * .03
    contribuicao = receita - imposto - pagamento - variavel
    return dict(clientes=basico + profissional, receita=receita,
                rbt12=receita * 12, aliquota=aliquota(receita * 12),
                imposto=imposto, variavel=variavel, pagamento=pagamento,
                contribuicao=contribuicao, fixos=fixos, horas=horas,
                caixa=contribuicao - fixos,
                resultado=contribuicao - fixos - depreciacao)


def brl(valor):
    return f'{valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


if __name__ == '__main__':
    for nome, b, p, f, d, capital, marketing, novos in [
        ('Lean', 15, 5, 8000, 6000 / 36, 45000, 1500, 3),
        ('Ideal', 30, 30, 25000, 18000 / 36, 160000, 4500, 6),
    ]:
        r = calcular(b, p, f, d)
        print('\n' + nome)
        for chave, valor in r.items():
            print(f'{chave}: {valor * 100:.6f}%' if chave == 'aliquota'
                  else f'{chave}: {brl(valor)}')
        arpu = r['receita'] / r['clientes']
        mc = r['contribuicao'] / r['clientes']
        print('ARPU:', brl(arpu), 'MC/cliente:', brl(mc))
        print('Equilíbrio aproximado à alíquota-base:', ceil(f / mc))
        # Busca inteira mantendo o mix exato: blocos 3:1 no Lean, 1:1 no Ideal.
        bloco = (3, 1) if nome == 'Lean' else (1, 1)
        for n in range(1, 101):
            pe = calcular(bloco[0] * n, bloco[1] * n, f, d)
            if pe['caixa'] >= 0:
                print('Equilíbrio com mix exato:', pe['clientes'], 'clientes;',
                      'caixa:', brl(pe['caixa']))
                break
        print('Payback estático (meses):', brl(capital / r['caixa']))
        print('CAC:', brl(marketing / novos), 'LTV receita:', brl(arpu / .03),
              'LTV contribuição:', brl(mc / .03))
        for label, kwargs in [('Desconto 10%', {'desconto': .1}),
                              ('Hora técnica +25%', {'custo_hora': 125})]:
            print(label, 'caixa:', brl(calcular(b, p, f, d, **kwargs)['caixa']))
