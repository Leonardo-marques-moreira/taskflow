# Situação-problema: PagaFácil

## 1. Correção de segurança hoje (comandos)
```
git switch main
git pull
git switch -c hotfix/login-seguranca
# aplicar a correção de 3 linhas
git add .
git commit -m "fix: corrige falha de segurança no login"
git push -u origin hotfix/login-seguranca
# abrir PR para a main, revisar rápido, fazer o merge e publicar
git switch develop
git cherry-pick <hash-do-commit>
```
A correção sai da branch de produção, sem esperar a release. O `cherry-pick` leva o mesmo commit para a `develop`, para o erro não voltar na próxima release.

## 2. Problemas do processo atual
| Problema | Ligação com a aula |
| --- | --- |
| Features ficam 2 a 4 semanas em branches | Integrar cedo: branches longas geram conflitos grandes |
| Uma release por mês, em lote grande | Entregas pequenas e frequentes reduzem o risco |
| Uma semana de testes manuais, sem revisão automática | Pull Request com revisão e testes automáticos |

## 3. Estratégia recomendada e justificativa
Recomendo GitHub Flow. A main fica sempre pronta para publicar, e todo trabalho vai em branches curtas, com Pull Request revisado. Com 12 desenvolvedores, o fluxo é simples de seguir e dispensa a `develop` e as branches de release do GitFlow. Correções como a do login seguem o mesmo caminho das demais e saem no mesmo dia. A proteção da main garante que nada entre sem revisão.

## 4. O que precisa existir antes de mudar
Testes automáticos rodando a cada PR (integração contínua, tema da Semana 3), main protegida com revisão obrigatória, uma forma rápida de publicar e de voltar atrás, e o time treinado em branches curtas.