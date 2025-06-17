import collections
import random

"""
2. O que é o "data model" em Python?
O data model é o conjunto de regras e interfaces que definem como objetos devem se comportar dentro da linguagem.

🧩 Ele define:

Como objetos são criados, comparados, iterados, somados, representados em string, etc.

Como operadores (+, ==), funções built-in (len, abs, repr), estruturas de controle (for, with) interagem com objetos.

➡️ O data model se baseia fortemente em special methods, como:

| Python code    | Internally calls...              |
| -------------- | -------------------------------- |
| `len(obj)`     | `obj.__len__()`                  |
| `obj[0]`       | `obj.__getitem__(0)`             |
| `obj + other`  | `obj.__add__(other)`             |
| `for x in obj` | `obj.__iter__()`                 |
| `with obj:`    | `obj.__enter__()` / `__exit__()` |
"""

Card = collections.namedtuple('Card', ['rank', 'suit'])

# Este exemplo mostra como você pode criar um objeto que se comporta como 
# uma sequence (como uma lista).
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# ##############################################################

deck = FrenchDeck()

# len(deck) funciona → porque implementamos __len__
print(len(deck))
# deck[0] funciona → porque implementamos __getitem__
print(deck[0])

# ##############################################################

random.choice(deck) # funciona porque o objeto é uma sequence

# ##############################################################

# O Python cuida dessas chamadas para manter consistência e otimização 
# (por exemplo, len() em listas é uma chamada em C extremamente rápida).

len(deck)       # correto ✅
deck.__len__()  # errado ❌

"""
➡️ Em Python, um objeto é considerado uma sequence (mesmo que não herde de list) 
se implementar:

__getitem__(index)
__len__()

Assim que você define esses dois special methods, seu objeto "comporta-se como" 
uma sequence para qualquer código Python que use len() ou [].
"""



# ##############################################################

len(deck) # funciona → porque implementamos __len__
deck[0], deck[-1] #→ porque implementamos __getitem__
random.choice(deck) #→ funciona porque o objeto é uma sequence
for card in deck: #→ iteração implícita
    deck[12::13]  #→ slicing funciona

# Esses comportamentos acontecem sem herdar de list ou implementar __iter__. 
# Isso acontece porque o Python reconhece __getitem__ como sinal de que o objeto 
# pode ser iterado.

# ##############################################################

"""
🧠 Reforçando: por que isso importa?
O data model define como fazer seu próprio tipo se comportar como os tipos built-in:

listas → com __getitem__, __len__

números → com __add__, __mul__, __abs__

funções → com __call__

context managers → com __enter__, __exit__

iteradores → com __iter__, __next__
"""

