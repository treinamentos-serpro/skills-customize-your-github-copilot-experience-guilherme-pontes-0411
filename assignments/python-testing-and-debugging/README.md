# 📘 Assignment: Python Testing and Debugging

## 🎯 Objective

Escreva testes automatizados com `pytest`, investigue falhas usando as mensagens de erro e corrija uma implementação sem alterar os comportamentos esperados.

## 📝 Tasks

### 🛠️ Criar testes para resultados e casos-limite

#### Descrição
Renomeie `starter-code.py` para `student_code.py` para que o módulo possa ser importado normalmente. Crie `test_student_code.py` e escreva testes para as funções fornecidas.

#### Requisitos
O programa concluído deve:

- Instalar e executar `pytest` usando `python -m pip install pytest` e `python -m pytest -v`
- Verificar se `calculate_average([70, 80, 90])` retorna `80` e se a função também aceita uma lista com um único valor
- Verificar se `calculate_average([])` levanta `ValueError`
- Verificar se `is_passing(59)` retorna `False`, `is_passing(60)` retorna `True` e `is_passing(100)` retorna `True`

### 🛠️ Investigar e corrigir uma falha

#### Descrição
Execute os testes, leia o resultado do `pytest` para encontrar o comportamento incorreto e ajuste a implementação até que todos os testes passem.

#### Requisitos
O programa concluído deve:

- Corrigir a implementação para que a nota mínima de aprovação seja `60`
- Manter os testes criados, sem remover casos que falham
- Executar novamente todos os testes e confirmar que passam
- Explicar qual caso de teste revelou o erro e como a mensagem do `pytest` ajudou a localizá-lo