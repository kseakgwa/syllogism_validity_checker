# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 21:45:45 2025

@author: 34346
"""
from AST import Conditional,Proposition, Universal, Negation

def modus_ponens(p1: Proposition, p2: Proposition):
    """
    If p1 is a conditional (P → Q) and p2 is P,
    return Q. Otherwise, return None.
    """

    if isinstance(p1, Conditional) and p1.antecedent == p2:
        return p1.consequent

    if isinstance(p2, Conditional) and p2.antecedent == p1:
        return p2.consequent

    return None

def apply_modus_ponens(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            result = modus_ponens(p1, p2)
            if result is not None:
                new_conclusions.add(result)

    return new_conclusions

def affirming_the_consequent(p1: Proposition, p2: Proposition):
    """
    If p1 is a conditional (P → Q) and p2 is Q,
    return P. Otherwise, return None.
    """

    if isinstance(p1, Conditional) and p1.consequent == p2:
        return p1.antecedent

    if isinstance(p2, Conditional) and p2.consequent == p1:
        return p2.antecedent

    return None

def apply_affirming_the_consequent(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            result = affirming_the_consequent(p1, p2)
            if result is not None:
                new_conclusions.add(result)

    return new_conclusions

def valid_categorical_1(p1: Proposition, p2: Proposition):
    """
    If p1 is a Universal ∀x (P(x) → Q(x)) and p2 is also a universal where ∀x (Q(x) → R(x)),
    return  ∀x (P(x) → R(x)). Otherwise, return None.
    """

    if isinstance(p1, Universal) and isinstance(p2, Universal):
        if p1.predicate == p2.subject:
            
            return Universal(p1.subject, p2.predicate)

    if isinstance(p1, Universal) and isinstance(p2, Universal):
        if p1.subject == p2.predicate:
            
            return Universal(p2.subject, p1.predicate)

    return None

def apply_valid_categorical_1(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            result = valid_categorical_1(p1, p2)
            if result is not None:
                new_conclusions.add(result)

    return new_conclusions

def modus_tollens (p1: Proposition, p2: Proposition):
    
    """
    If p1 is a conditional (P → Q) and p2 is a negation not Q,
    return not P. Otherwise, return None.
    """

    if isinstance(p1, Conditional) and isinstance(p2, Negation):
        print(p1)
        print(p2)
        if p2.proposition == p1.consequent:
            return Negation(p1.antecedent)

    if isinstance(p2, Conditional) and isinstance(p1, Negation):
        if p1.proposition == p2.consequent:
            return Negation(p2.antecedent)

    return None

def apply_modus_tollens(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            result = modus_tollens(p1, p2)
            if result is not None:
                new_conclusions.add(result)

    return new_conclusions

def denying_the_antecendent (p1: Proposition, p2: Proposition):
    
    """
    If p1 is a conditional (P → Q) and p2 is a negation not P,
    return not P. Otherwise, return None.
    """

    if isinstance(p1, Conditional) and isinstance(p2, Negation):
        if p2.proposition == p1.antecedent:
            return Negation(p1.antecedent)

    if isinstance(p2, Conditional) and isinstance(p1, Negation):
        if p1.proposition == p2.antecedent:
            return Negation(p2.antecedent)

    return None

def apply_denying_the_antecendent(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            result = denying_the_antecendent(p1, p2)
            if result is not None:
                new_conclusions.add(result)

    return new_conclusions
