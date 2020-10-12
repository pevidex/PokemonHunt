# Premium Minds exercício - solução básica

## Descrição da solução:

Aqui procurei ter uma abordagem mais simples. O objectivo desta solução é maioritariamente gerar resultados para testar as soluções mais complexas.

complexidade espacial: Para cada casa não repetida, iremos guardar as suas coordenadas. No pior caso temos 0 casas repetidas o que origina uma complexidade de O(N).

complexidade temporal: Para cada casa, vamos procurar se existe uma entrada no dicionário tal que casa.x = dicionário.key. Se existir incluímos o y correspondente nessa entrada. Se não existir criamos uma entrada tal que dict[casa.x] = [casa.y] Esta operação tem um custo amortizado de O(N) * N = O*(N^2).
