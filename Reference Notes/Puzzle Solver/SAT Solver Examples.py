# https://rhettinger.github.io/einstein.html
# https://en.wikipedia.org/wiki/Boolean_satisfiability_problem
# https://en.wikipedia.org/wiki/Propositional_calculus
# # https://dsearls.org/

import pycosat
from pprint import pprint
from sat_utils import *

pprint(list(pycosat.itersolve([(-1, 2), (-1, 3)])), width=20)

pprint(translate([['~P', 'Q'],['~P', 'R']])[0])

pprint(from_dnf([['~P'], ['Q', 'R']]))

cnf = from_dnf([['~P'], ['Q', 'R']])
pprint(solve_all(cnf, True))

cnf = from_dnf([['~FlatTire'], ['NeedToRemove', 'GotoGasStation']])
pprint(solve_all(cnf, True))


# Express that at least one of A, B, and C are true
pprint(some_of(['A', 'B', 'C']))

# Express that at exactly one of A, B, and C is true
pprint(one_of(['A', 'B', 'C']))

# Express that no more than one of A, B, and C are true
pprint(Q(['A', 'B', 'C']) <= 1)