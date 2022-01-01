import math
from functools import total_ordering
def find_more_len(pile):
    more_len = 0
    for p in pile:
        if len(str(p)) > more_len:
            more_len = len(str(p))
    return more_len

@total_ordering
class Pile:
    def __init__(self, pile=[]):
        self.pile = None
        if self.pile is None:
            if type(pile) in [list,str]:
                self.pile = pile
            elif type(pile) is int:
                self.pile = list(range(pile-1, -1, -1))
            else:
                raise TypeError("Only list or str are allowed")

    def __len__(self):
        return len(self.pile)

    def __repr__(self):
        if self.is_empty():
            return "This pile is empty"
        else:
            m = ""
            more_len = find_more_len(self.pile)
            for elt in self.pile:
                m += "|_ " + str(elt).center(more_len) + " _|"
                m += "\n"
            return m

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.pile == other.pile
        else:
            raise TypeError("Only Pile are allowed")

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return len(self.pile) < len(other.pile)
        else:
            raise TypeError("Only Pile are allowed")

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return len(self.pile) <= len(other.pile)
        else:
            raise TypeError("Only Pile are allowed")

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return len(self.pile) >= len(other.pile)
        else:
            raise TypeError("Only Pile are allowed")

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return len(self.pile) > len(other.pile)
        else:
            raise TypeError("Only Pile are allowed")

    def __iter__(self):
        return iter(self.pile)

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.remove()

    def push(self, elt):
        if elt is None or type(elt) in [int, float, str]:
            self.pile.insert(0, elt)
        else:
            raise TypeError("Only int, float, str are allowed")

    def is_empty(self):
        return len(self.pile) == 0

    def pop(self, nb=1):
        if type(nb) is not int:
            raise TypeError("Only int are allowed")
        if nb <= 0:
            raise ValueError("Only positive int are allowed")
        if nb > len(self.pile):
            raise ValueError("Not enough elements")
        if nb == 1:
            return self.pile.pop(0)
        else:
            return [self.pile.pop(0) for _ in range(nb)]

    def clear(self):
        self.pile = []

    def peek(self):
        return self.pile[0]

def simple_verify_exp(expression, caractere_start, caractere_end):
    p = Pile()
    for letter in expression:
        if letter == caractere_start:
            p.add(letter)
        elif letter == caractere_end:
            if p.is_empty():
                return False
            else:
                p.remove()
    return p.is_empty()


if __name__ == "__main__":
    p = Pile()
    print(len(p))



    # exp = "((()())"
    # print(simple_verify_exp(exp,'(',')'))
