# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 01:05:45 2025

@author: 34346
"""
from AST import * 

def parse_atomic(sentence: str) -> Proposition:
    sentence = normalize(sentence)

    if sentence.startswith("therefore "):
        return Conclusion(parse_atomic(sentence.replace("therefore ", "")))
    if sentence.startswith("if "):
        return parse_conditional(sentence)
    if sentence.startswith("all "):
        return parse_universal(sentence)
    if sentence.startswith("some "):
        return parse_existential(sentence)
    if sentence.startswith("not "):
        return Negation(parse_atomic(sentence[4:]))
    else:
        try:
            return parse_individual(sentence)
        except:
            raise ValueError(f"Unrecognized form: {sentence}")
    

def normalize(sentence: str) -> str:
    sentence = sentence.lower().strip()
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(",", "")
    return sentence

def make_term(word: str) -> Term:
    if word.endswith("s"):
        word = word[:-1]
    return Term(word)

def parse_individual(sentence:str)-> Atomic:
    
    tokens = sentence.split()
    individual= make_term(tokens[0])
    predicate=make_term(tokens[-1])
    return Atomic(individual, predicate)

def parse_universal(sentence: str) -> Universal:
    # "all dogs are mammals"
    tokens = sentence.split()
    subject = make_term(tokens[1])
    predicate = make_term(tokens[-1])
    return Universal(subject, predicate)

def parse_existential(sentence: str) -> Existential:
    # "some dogs are pets"
    tokens = sentence.split()
    subject = make_term(tokens[1])
    predicate = make_term(tokens[-1])
    return Existential(subject, predicate)

def parse_conditional(sentence: str) -> Conditional:
    # "if it rains then the ground is wet"
    sentence = sentence.replace("if ", "")
    antecedent_text, consequent_text = sentence.split(" then ")

    antecedent = parse_atomic(antecedent_text)
    consequent = parse_atomic(consequent_text)

    return Conditional(antecedent, consequent)