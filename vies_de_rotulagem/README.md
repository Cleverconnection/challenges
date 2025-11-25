# G08 — Viés de Rotulagem

## Narrativa
Fei-Fei Li defende que “dados de qualidade exigem diversidade e respeito”. Nesta estação azul, você encontra um
serviço que arquiva rótulos sintéticos para imagens. Porém, um dos campos carrega um viés: pessoas com traços
similar de tons de pele recebem etiquetas diferentes.

## Objetivo
Investigue o endpoint `/dados` para baixar o dataset. Ajuste a etiqueta `atributo` das entradas onde `tom_de_pele`
é "escuro" e o `atributo` esteja rotulado como "neutro". Envie uma requisição `POST` para `/corrigir` com a lista
alterada. Se o serviço reconhecer que o viés foi removido, a flag será retornada.

## Recursos fornecidos
- Arquivo `data/dataset.json` com registros fictícios.
- Script `scripts/ajuste.py` para automatizar a correção.
- Páginas HTML relatando o compromisso de Fei-Fei Li com uma IA centrada em pessoas.

## Tabela de referência
| Desafio | Flag | Valor conceitual |
|---------|------|------------------|
| Viés de Rotulagem | CTF{fei_fei_bias_ajustado} | Detecção e correção de viés em labels |

## Observações
- Execute `flask --app app.py run --host 0.0.0.0 --port 5008`.
- A correção precisa enviar JSON no formato `{"registros": [...]}`.
- A narrativa destaca a citação “Uma IA justa precisa refletir a humanidade”.
