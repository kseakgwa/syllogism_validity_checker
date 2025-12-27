# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 15:54:28 2025

@author: 34346
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Term:
    name: str


class Proposition:
    pass


@dataclass(frozen=True)
class Universal(Proposition):
    subject: Term
    predicate: Term


@dataclass(frozen=True)
class Existential(Proposition):
    subject: Term
    predicate: Term


@dataclass(frozen=True)
class Conditional(Proposition):
    antecedent: Proposition
    consequent: Proposition

@dataclass(frozen=True)
class Individual:
    name: str


@dataclass(frozen=True)
class Atomic(Proposition):
    individual: Individual
    predicate: Term
    
    
@dataclass(frozen=True)
class Disjunction(Proposition):
    left: Proposition
    right: Proposition


@dataclass(frozen=True)
class Negation(Proposition):
    proposition: Proposition


@dataclass(frozen=True)
class Conclusion:
    proposition: Proposition
