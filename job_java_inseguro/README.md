# Job Java Inseguro

## Visão geral
O Job Server Java aceita objetos serializados enviados em Base64 e assume que são instâncias da classe `TrustedEnvelope`. Não há validação de classes permitidas, permitindo carregar gadgets arbitrários presentes no classpath e atingir a ação `admin`.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Job Java Inseguro | `CTF{java_insecure_deserialize}` | Médio |

## Execução
1. Produzir payloads Java serializados (por exemplo com `ysoserial`).; Entender o formato `application/x-java-serialized-object` codificado em Base64.; Manipular o campo `action` da classe `TrustedEnvelope` para obter a flag.
2. `POST /api/jobs` — Recebe `payload=` via formulário.; `GET /flag` — Bloqueado diretamente, apenas retornado quando um envelope com `action=admin` é desserializado.; Arquivos estáticos (`index.html`, `theme.css`) com instruções no tema Vivo.
3. Compile o projeto com `./gradlew shadowJar` ou utilize o binário fornecido na imagem Docker (feito automaticamente). 2. Gere um objeto `TrustedEnvelope` com `action=admin` e serialize-o usando um script Java ou `ysoserial` customizado. 3. Codifique o resultado em Base64 e envie via `curl -d "payload="` para `/api/jobs`.
4. Criar manualmente uma instância de `TrustedEnvelope("admin", "qualquer")`, serializar e enviar.; O servidor reconhecerá a classe e retornará diretamente a flag na resposta HTTP.

## Narrativa
Explorar Job Java Inseguro revela a flag quando a vulnerabilidade principal é compreendida e explorada.
