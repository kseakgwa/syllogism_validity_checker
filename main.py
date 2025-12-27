# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 01:45:26 2025

@author: 34346
"""

# Collect user input
# Clean/ format input
# pass to dispatcher
# run correct parser

# check validity
# print valid or not + what kind of argument

from AST import *
from parsers import *
from argument_forms import apply_modus_ponens, apply_affirming_the_consequent, apply_valid_categorical_1

def user_input(): #This gets the required input from the user
    
    print("***** Syllogism Validity Checker *****")
    syllogism= input("Paste syllogism here:\n")
    syllogism=syllogism.lower()
    syllogism_lines=syllogism.split(".")
    
    rule_to_prac=input("what form would you like to practice?")
    rule_to_prac=rule_to_prac.lower()
    
    return syllogism_lines, rule_to_prac

def apply_rules(parsed_syllogism, rule_to_prac):
    
    rule_map={"modus ponens":[apply_modus_ponens(parsed_syllogism), "valid"],
              "affirming the consequent":[apply_affirming_the_consequent(parsed_syllogism), "invalid"],
              "Categorical 1": [apply_valid_categorical_1(parsed_syllogism), "valid"]
              }
    
    result= rule_map.get(rule_to_prac)[0]
    validity= rule_map.get(rule_to_prac)[1]
    
    # def recursive_rule_search(parsed_syllogism, rule_to_prac,result):
        
    if result!=set():
        rule_name= rule_to_prac
        return result, rule_name,validity
    else:
        
        for rule_name in rule_map:
            if rule_name != rule_to_prac:
                result= rule_map.get(rule_name)[0]
                validity= rule_map.get(rule_name)[1]
                if result != set():
                    return result, rule_name, validity
                    
                        

def output_gen(rule_output, rule_name, rule_to_prac,validity):
    
    if rule_output!=set():
        verdict= validity
        if rule_to_prac==rule_name:
        
            match_intention = (f"You did what you set out to: you generated an example of a {verdict} {rule_to_prac}")
        else:
            match_intention = (f"You didn't do what you set out to: you generated an example of a {verdict} {rule_name} instead of a {rule_to_prac}")
    # else:
    #     verdict=(f"Invalid:{rule_name}")
        
    return match_intention

if __name__== "__main__":
    
    syllogism_lines,rule_to_prac = user_input()
    parsed_syllogism = []
    for line in syllogism_lines[:-1]:
        line=normalize(line)
        line_logic=parse_atomic(line)
        # print(parsed_syllogism)
        parsed_syllogism.append(line_logic)
        # print(line_logic)
    # print(parsed_syllogism)
    rule_output, rule_name, validity=apply_rules(parsed_syllogism, rule_to_prac)
    # while rule_output!=set():
        
    #     a
    
    print(output_gen(rule_output, rule_name, rule_to_prac, validity))
    
        
        
        
        
        
    
    
    
    
    

