# PokemonHunt

### Prerequisites

- Python3
- MongoDb

### Setup

```
pip install -r requirements.txt
```

### Run

```
cd solution
python pokemon_hunt.py
```

### Test

```
cd solution
python tests.py
```

### Descrição da solução

Para este exercício desenvolvi duas soluções. A primeira "solution_for_testing" é uma solução simples com o intuito de testar a solução complexa. Em baixo vou descrever a solução completa juntamente com algumas observações de possíveis melhoramentos.

Para resolver este problema decidi dividir o espaço em matrizes de MATRIX_LENGTH * MATRIX_LENGTH (configurável). O Ash começa numa posição neutra (0,0) que corresponde ao centro da matriz inicial. À medida que o Ash se vai movendo, vai preenchendo a matriz com 1's nas casas que ainda não foram visitadas (sinalizadas por 0's). Um contador vai sendo incrementado à medida que a matriz é preenchida com 1's.

Quando o Ash sai dos limites da matriz, podem acontecer 3 situações:

a) Está a entrar numa zona nunca antes visitada.
b) Está a entrar numa zona já antes visitada e: 
	b1) A matriz encontra-se em cache; 
	b2) A matriz não se encontra em cache.

Para resolver a situação a), é rendida uma nova matriz e a anterior é colocada no topo da cache. É registado um ponto de entrada nesta nova matriz. Este ponto de entrada contém um par de coordenadas e um ponteiro para a posição do input que gerou esta posição. O objetivo é poder reconstruir esta matriz no futuro se for necessário. Podem ser registados mais que 1 pontos de entrada.

Na situação b1) restabelecemos a matriz da cache e criamos um novo ponto de entrada.

Na situação b2) fazemos uma query à bd pela matriz e reconstruímos com base nos pontos de entrada registados.

Observações:
1) A cache segue uma política LRU, ou seja, a matriz que não é usada há mais tempo é enviada para a base de dados.
2) Foi usada um SGBD NoSql (mongodb) para ter vantagem na velocidade de query em a relação a uma bd relacional
3) Porque não guardar somente os pontos visitados por matriz em vez de matrizes inteiras? Porque uma forma de melhorar esta solução seria incluíndo novas threads responsáveis pela construção das matrizes adjacentes. Assim deixávamos a main thread com a única task de aceder às matrizes e conferir se os pontos já tinham sido visitados.
