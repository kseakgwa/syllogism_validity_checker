# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 21:45:45 2025

@author: 34346
"""
from AST import Conditional,Proposition, Universal, Negation, Disjunction, Conclusion, Existential

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

def valid_categorical_1(p1: Proposition, p2: Proposition, p3: Proposition):
    """
    If p1 is a Universal ∀x (P(x) → Q(x)) and p2 is also a universal where ∀x (Q(x) → R(x)),
    return  ∀x (P(x) → R(x)). Otherwise, return None.
    """

    if isinstance(p1, Universal) and isinstance(p2, Universal) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Universal):
            if p1.predicate == p2.subject:
                if p1.subject==p3.proposition.subject and p2.predicate==p3.proposition.predicate:
                    
                    return Universal(p1.subject, p2.predicate)

    if isinstance(p1, Universal) and isinstance(p2, Universal)and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Universal):
            if p1.subject == p2.predicate:
                if p2.subject==p3.proposition.subject and p1.predicate==p3.proposition.predicate:
            
                    return Universal(p2.subject, p1.predicate)

    return None

def apply_valid_categorical_1(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            for p3 in premises:
                result = valid_categorical_1(p1, p2, p3)
                if result is not None:
                    new_conclusions.add(result)

    return new_conclusions

def valid_categorical_2(p1: Proposition, p2: Proposition, p3: Proposition):
    """
    If p1 is a Universal ∀x (P(x) → Q(x)) and p2 is also an existential where Ex (Q(x) → R(x)),
    return  Ex (P(x) → R(x)). Otherwise, return None.
    """

    if isinstance(p1, Universal) and isinstance(p2, Existential) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Existential):
            if p1.subject == p2.predicate:
                if p2.subject == p3.proposition.subject and p1.predicate ==p3.proposition.predicate :
            
                    return Existential(p2.subject, p1.predicate)

    if isinstance(p2, Universal) and isinstance(p1, Existential)and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Existential):
            if p2.subject == p1.predicate:
                if p1.subject==p3.proposition.subject and p2.predicate ==p3.proposition.predicate:
            
                    return Existential(p1.subject, p2.predicate)

    return None

def apply_valid_categorical_2(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            for p3 in premises:
                result = valid_categorical_2(p1, p2,p3)
                if result is not None:
                    new_conclusions.add(result)

    return new_conclusions

def valid_categorical_3(p1: Proposition, p2: Proposition, p3: Proposition):
    """
    If p1 is a Universal ∀x (P(x) → Q(x)) and p2 is also an existential where Ex (Q(x) → R(x)),
    return  Ex (P(x) → R(x)). Otherwise, return None.
    """

    if isinstance(p1, Universal) and isinstance(p2, Universal) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Existential):
            if p1.subject == p2.subject and p1.predicate != p2.predicate:
                if p2.predicate == p3.proposition.subject and p1.predicate == p3.proposition.predicate:
            
                    return Existential(p2.predicate, p1.predicate)

    if isinstance(p2, Universal) and isinstance(p1, Universal) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Existential):
            if p2.subject == p1.subject and p1.predicate != p2.predicate:
                if p1.predicate==p3.proposition.subject and p2.predicate == p3.proposition.predicate:
            
                    return Existential(p1.predicate, p2.predicate)

    return None

def apply_valid_categorical_3(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            for p3 in premises:
                result = valid_categorical_3(p1, p2,p3)
                if result is not None:
                    new_conclusions.add(result)

    return new_conclusions

def valid_categorical_4(p1: Proposition, p2: Proposition, p3: Proposition):
    """
    If p1 is a Universal ∀x (P(x) → Q(x)) and p2 is also an existential where Ex (Q(x) → R(x)),
    return  Ex (P(x) → R(x)). Otherwise, return None.
    """

    if isinstance(p1, Universal) and isinstance(p2, Universal) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Universal):
            if p1.predicate == p2.predicate and p1.subject != p2.subject:
                if p1.subject == p3.proposition.subject and p2.subject == p3.proposition.predicate:
                    
                    return Universal(p1.subject, p2.subject)

    if isinstance(p2, Universal) and isinstance(p1, Universal) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Universal):
            if p2.predicate == p1.predicate and p1.subject != p2.subject:
                if p2.subject == p3.proposition.subject and p1.subject == p3.proposition.predicate:
            
                    return Universal(p2.subject, p1.subject)

    return None

def apply_valid_categorical_4(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            for p3 in premises:
                result = valid_categorical_4(p1, p2, p3)
                if result is not None:
                    new_conclusions.add(result)

    return new_conclusions

def valid_categorical_5(p1: Proposition, p2: Proposition, p3: Proposition):
    """
    If p1 is a Universal ∀x (P(x) → Q(x)) and p2 is also an existential where Ex (Q(x) → R(x)),
    return  Ex (P(x) → R(x)). Otherwise, return None.
    """

    if isinstance(p1, Universal) and isinstance(p2, Existential) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Existential):
            if p1.predicate == p2.predicate and p1.subject != p2.subject:
                if p2.subject == p3.proposition.subject and p1.subject == p3.proposition.predicate:
            
                    return Existential(p2.subject, p1.subject)

    if isinstance(p2, Universal) and isinstance(p1, Existential) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Existential):
            if p2.predicate == p1.predicate  and p1.subject != p2.subject:
                if p1.subject == p3.proposition.subject and p2.subject == p3.proposition.predicate:
            
            
                    return Existential(p1.subject, p2.subject)

    return None

def apply_valid_categorical_5(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            for p3 in premises:
                result = valid_categorical_5(p1, p2, p3)
                if result is not None:
                    new_conclusions.add(result)

    return new_conclusions

def valid_categorical_6(p1: Proposition, p2: Proposition, p3: Proposition):
    """
    If p1 is a Universal ∀x (P(x) → Q(x)) and p2 is also an existential where Ex (Q(x) → R(x)),
    return  Ex (P(x) → R(x)). Otherwise, return None.
    """

    if isinstance(p1, Universal) and isinstance(p2, Universal)  and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Universal):
            if p1.subject == p2.subject and p1.predicate != p2.predicate:
                if p1.predicate == p3.proposition.subject and p2.predicate == p3.proposition.predicate:
                    return Universal(p1.predicate, p2.predicate)

    if isinstance(p2, Universal) and isinstance(p1, Universal) and isinstance(p3, Conclusion):
        if isinstance(p3.proposition, Universal):
            if  p1.subject == p2.subject and p2.predicate != p1.predicate:
                if p2.predicate== p3.proposition.subject and p1.predicate == p3.proposition.predicate:
            
                    return Universal(p2.predicate, p1.predicate)
# if isinstance(p1, Universal) and isinstance(p2, Universal) and isinstance(p3, Universal):
#     if p1.predicate == p2.subject and and p1.subject==p3.subject and p2.predicate==p3.predicate:
        
#         return Universal(p1.subject, p2.predicate)

# if isinstance(p1, Universal) and isinstance(p2, Universal)and isinstance(p3, Universal):
#     if p1.subject == p2.predicate and p2.subject==p3.subject and p1.predicate==p3.predicate:
        
        return Universal(p2.subject, p1.predicate)

    return None

def apply_valid_categorical_6(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            for p3 in premises:
                result = valid_categorical_6(p1, p2, p3)
                if result is not None:
                    new_conclusions.add(result)

    return new_conclusions

def modus_tollens (p1: Proposition, p2: Proposition):
    
    """
    If p1 is a conditional (P → Q) and p2 is a negation not Q,
    return not P. Otherwise, return None.
    """

    if isinstance(p1, Conditional) and isinstance(p2, Negation):
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

def eliminative_syllogism (p1: Proposition, p2: Proposition):
    
    """
    If p1 is a disjunction (P v Q) and p2 is either P or Q,
    return either P or Q. Otherwise, return None.
    """

    if isinstance(p1, Disjunction) and isinstance(p2, Negation):
        if p2.proposition == p1.left:
            return p1.right
        if p2.proposition == p1.right:
            return p1.left

    if isinstance(p2, Disjunction) and isinstance(p1, Negation):
        if p1.proposition == p2.left:
            return p2.right
        if p1.proposition == p2.right:
            return p2.left


    return None

def apply_eliminative_syllogism(premises):
    new_conclusions = set()

    for p1 in premises:
        for p2 in premises:
            result = eliminative_syllogism (p1, p2)
            if result is not None:
                new_conclusions.add(result)

    return new_conclusions
