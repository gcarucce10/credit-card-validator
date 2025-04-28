# Validador de Bandeira de Cartão de Crédito

Este projeto é um simples script Python que **valida números de cartões de crédito** e identifica sua **bandeira** (marca) com base em padrões conhecidos.

## Como funciona?

O script:
1. **Remove** espaços e hífens (`-`) do número do cartão inserido.
2. **Verifica** se o número contém apenas dígitos.
3. **Compara** o número contra expressões regulares que representam padrões de diferentes bandeiras de cartão:
   - Visa
   - MasterCard
   - Elo
   - American Express
   - Discover
   - Hipercard
4. **Retorna** a bandeira correspondente ou `"Invalid"` se o número não se encaixar em nenhum padrão.

## Estrutura do Código

- **Função `validate_credit_card(card_number)`**:
  - Limpa o número do cartão.
  - Verifica se é numérico.
  - Usa expressões regulares para identificar a bandeira.
  - Retorna o nome da bandeira ou `"Invalid"`.
  
- **Bloco `if __name__ == "__main__":`**:
  - Permite que o usuário insira o número do cartão.
  - Chama a função de validação.
  - Exibe a bandeira detectada.

## Exemplo de Uso

```bash
$ python validador_cartao.py
Enter the credit card number: 4111 1111 1111 1111
Card Brand: Visa
