# Situação-problema: EduTech Saber

## 1. Diagnóstico
| Problema | Prática de CI que resolve |
| --- | --- |
| Sem testes automatizados | Rodar testes a cada push e PR |
| Build feito no notebook do tech lead | Build num ambiente limpo e padronizado do CI |
| O bug passou pela revisão humana | Teste automático que pega a regressão antes do merge |
| Deploy toda sexta às 18h | Entregas menores e frequentes, com o CI verde como pré-requisito |

## 2. Pipeline proposto
1. Baixar o código: parte sempre da versão commitada.
2. Instalar dependências: ambiente igual em toda execução.
3. Lint: pega erros simples e baratos.
4. Testes com cobertura: barram bugs como o das notas.
5. Build: gerado pelo CI, e não no notebook de uma pessoa.

## 3. Teste que pegaria o bug
```python
def nota_final(n1, n2):
    return (n1 + n2) / 2


def test_nota_final_com_decimal():
    assert nota_final(7.5, 8.5) == 8.0
```

## 4. Plano de adoção
Começar com o CI rodando sem bloquear, para o time se acostumar. Escrever primeiro os testes dos fluxos mais críticos, como o cálculo de notas. Depois tornar o check obrigatório na main e, por último, automatizar o deploy e sair da rotina das sextas.