$ python main.py chat

Chat RAG — digite sua pergunta (ou 'sair' para encerrar).
>> Nosso logging está de acordo com as boas práticas?

=== Resposta ===
Não, o logging no código fornecido não está de acordo com as boas práticas.

A função `processa_dados` em [FILE]: calc.py é identificada no contexto como "sem logging".

**Boas Práticas Relevantes:**
*   Logging deve usar níveis apropriados (INFO, WARNING, ERROR).

**Passos acionáveis:**
1.  **Adicionar logging:** Implemente logging na função `processa_dados` em [FILE]: calc.py.
2.  **Usar níveis apropriados:** Certifique-se de que o logging utilize níveis como INFO, WARNING e ERROR, conforme necessário, para diferentes eventos ou estados dentro da função.

>> `Tem funções muito longas?                

=== Resposta ===
Sim, a função `processa_dados` no arquivo [FILE]: calc.py é identificada como uma função muito longa.

**Passos Acionáveis:**

1.  **Refatorar funções muito longas:** Conforme as boas práticas da equipe Jullia, Paula, Bozzi (ponto 3), deve-se refatorar funções muito longas para melhorar a legibilidade e manutenibilidade do código.

>> Qual função não tem docstring?

=== Resposta ===
A função que não tem docstring é `soma` no arquivo [FILE]: calc.py.

**Passos acionáveis:**

1.  Adicione uma docstring clara à função `soma`, explicando o que ela faz, seus parâmetros e o que ela retorna.
2.  Adicione tipagem estática aos parâmetros e ao retorno da função `soma`, conforme recomendado nas boas práticas (item 2: "Funções devem ter docstrings claras e tipagem estática sempre que possível").

>> Onde há senhas hardcoded?     

=== Resposta ===
A senha hardcoded está presente no arquivo [FILE]: calc.py, dentro da função `processa_dados`, na linha que define `senha = "123456"`.

**Passos acionáveis:**

1.  **Remover a senha do código:** Mova a configuração sensível para uma variável de ambiente.
2.  **Utilizar variáveis de ambiente:** Conforme as Boas Práticas (item 5), "Configurações sensíveis via variáveis de ambiente (.env), nunca em código."

>> Qual a cobertura de testes mínima?

=== Resposta ===
A cobertura de testes mínima recomendada é de 80%.

[Boas Práticas — Equipe: Jullia, Paula, Bozzi]: Testes unitários para funções críticas; cobertura mínima recomendada: 80%.

>> Como devo fazer logging?

=== Resposta ===
De acordo com as boas práticas, o logging deve usar níveis apropriados.

**Como fazer logging:**

1.  Utilize níveis de logging apropriados:
    *   `INFO`
    *   `WARNING`
    *   `ERROR`

**Passos Acionáveis:**

*   Identifique as partes do código onde o registro de informações é necessário.
*   Escolha o nível de logging mais adequado para cada mensagem, por exemplo:
    *   `INFO` para eventos rotineiros ou de acompanhamento.
    *   `WARNING` para situações que podem indicar um problema futuro, mas não interrompem a execução.
    *   `ERROR` para falhas que impedem a operação normal de uma parte do sistema.

O contexto do código em [FILE]: calc.py na função `processa_dados` atualmente não possui logging, o que pode ser uma área para implementação dessas boas práticas.
