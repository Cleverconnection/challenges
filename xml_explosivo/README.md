# XML Explosivo

## Visão geral
A API de importação XML usa `lxml` com suporte a entidades externas e DTDs sem restrições. Isso permite tanto abusar de expansão exponencial (ataques "Billion Laughs") quanto incluir entidades externas para ler arquivos locais ou invocar endpoints internos.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| XML Explosivo | `CTF{xml_xxe_resource_exhaust}` | Médio |

## Execução
1. Construir payloads XML com DTD customizada para XXE.; Avaliar o risco de negação de serviço causado por expansão de entidades.; Demonstrar extração de informações sensíveis por meio de entidades externas.
2. `POST /api/import` — Processa XML enviado via corpo bruto ou campo `xml` em formulário.; `GET /api/sample` — Exibe um XML válido de referência.; `GET /flag` — Endpoint protegido, mas acessível via XXE quando referenciado.
3. Suba o container do desafio. 2. Envie o XML de exemplo para se familiarizar com o formato esperado. 3. Monte um XML com DTD inline que defina uma entidade externa.
4. Utilize um payload como: xml
5. ]> &flag; ; Envie para `/api/import` e observe a resposta contendo o conteúdo retornado pelo endpoint, incluindo a flag.

## Narrativa
Explorar XML Explosivo revela a flag quando a vulnerabilidade principal é compreendida e explorada.
