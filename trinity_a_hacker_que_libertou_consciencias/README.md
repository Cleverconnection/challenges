# Trinity — A Hacker que Libertou Consciências

Trinity introduziu Neo ao mundo real ao provar que não era apenas um mito digital. No clube, ela revela ter sido a
responsável por invadir o banco de dados da Receita, derrubando estereótipos sobre quem estava por trás do handle
"Trinity".

## Como participar

- O serviço Flask na porta `8080` apenas fornece contexto e validação.
- Utilize `GET /hints` para recuperar lembretes do diálogo.
- Quando tiver certeza da resposta, envie `POST /verify` com JSON `{"answer": "sua_resposta"}`.
- A API converte letras maiúsculas/minúsculas automaticamente e aceita respostas com ou sem sublinhados.

## Flag

A flag oficial é `CTF{Banco_de_Dados_da_Receita}`. Basta enviar a frase que descreve o motivo da surpresa de Neo para
recebê-la de volta.
