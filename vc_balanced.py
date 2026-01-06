"""
Command-line DPDA simulator that checks whether a sentence has a balanced
number of consonant-starting and vowel-starting words.

The program uses `automata-lib` to define a deterministic pushdown automaton
that reads an input string and tracks, on the stack, the difference between
the number of first-letter consonants and vowels per word. If the stack is
empty when the end-of-input symbol is reached, then the numbers are balanced
and the input is **accepted**. Otherwise, it is **rejected**.

Main entry point is the interactive menu loop at the bottom of the file.
"""

import os  # for clearing screen
import time  # for pausing
import re  # for regex input validation

# requires 'pip install automata-lib'
from automata.pda.dpda import DPDA # for deterministic pushdown automata

# requires 'pip install prompt_toolkit'
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError # for input validation
from prompt_toolkit import prompt

# requires 'pip install tabulate'
import tabulate
tabulate.PRESERVE_WHITESPACE = True
from tabulate import tabulate # for table display


# DISPLAY CLEAR
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# INPUT VALIDATOR
class InputValidator(Validator):
    
    def __init__(self, menu=False, alphaSpace=False):
        self.menu = menu
        self.alphaSpace = alphaSpace
    
    def validate(self, document: Document):
        text = document.text
        if not text:
            raise ValidationError(message='')
        elif self.menu and not text.isdigit():
            raise ValidationError(message='This input contains non-numeric characters')
        elif self.menu and text.isdigit() and not (int(text) >= 1 and int(text) <= 3):
            raise ValidationError(message='The menu only has 1, 2, and 3 as choices')
        elif self.alphaSpace and not re.match("^[a-z ]+$", text.lower()):
            raise ValidationError(message='This input contains non-alphabet/space characters')

# PUSHDOWN AUTOMATON DEFINITION
# -----------------------------
# The DPDA operates over sentences composed of lowercase letters and spaces.
# It inspects only the *first* letter of each word and uses the stack to keep
# track of the difference between the number of consonants and vowels seen so
# far as first letters:
#
# - 'V' on the stack represents one more vowel-starting word than consonant-
#   starting words.
# - 'C' on the stack represents one more consonant-starting word than vowel-
#   starting words.
# - The initial symbol 'S' marks the bottom of the stack.
#
# When the explicit end marker '!' is read, the DPDA checks whether the stack
# is back to the initial symbol (effectively empty under `empty_stack`
# acceptance). If so, the number of first-letter vowels equals the number of
# first-letter consonants and the input is accepted.
dpda = DPDA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'!', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '},
    stack_symbols={'S', 'V', 'C'},
    transitions={
        # CHECK THE FIRST LETTER
        'q0': {
            # END
            '!': {
                'S': ('q2', ''),         # transition to q2, pop 'S'
                'V': ('q2', ('V',)),     # transition to q2
                'C': ('q2', ('C',)),     # transition to q2
            },
            # SPACE
            ' ': {
                'S': ('q0', ('S',)),     # no change
                'V': ('q0', ('V',)),     # no change
                'C': ('q0', ('C',)),     # no change
            },
            # VOWELS
            'a': {
                'S': ('q1', ('V', 'S')), # transition to q1, push 'V'
                'V': ('q1', ('V', 'V')), # transition to q1, push 'V'
                'C': ('q1', ''),        # transition to q1, pop 'C'
            },
            'e': {
                'S': ('q1', ('V', 'S')), # transition to q1, push 'V'
                'V': ('q1', ('V', 'V')), # transition to q1, push 'V'
                'C': ('q1', ''),        # transition to q1, pop 'C'
            },
            'i': {
                'S': ('q1', ('V', 'S')), # transition to q1, push 'V'
                'V': ('q1', ('V', 'V')), # transition to q1, push 'V'
                'C': ('q1', ''),        # transition to q1, pop 'C'
            },
            'o': {
                'S': ('q1', ('V', 'S')), # transition to q1, push 'V'
                'V': ('q1', ('V', 'V')), # transition to q1, push 'V'
                'C': ('q1', ''),        # transition to q1, pop 'C'
            },
            'u': {
                'S': ('q1', ('V', 'S')), # transition to q1, push 'V'
                'V': ('q1', ('V', 'V')), # transition to q1, push 'V'
                'C': ('q1', ''),        # transition to q1, pop 'C'
            },
            # CONSONANTS
            'b': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'c': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'd': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'f': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'g': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'h': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'j': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'k': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'l': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'm': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'n': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'p': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'q': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'r': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            's': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            't': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'v': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'w': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'x': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'y': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            },
            'z': {
                'S': ('q1', ('C', 'S')), # transition to q1, push 'C'
                'V': ('q1', ''),         # transition to q1, pop 'V'
                'C': ('q1', ('C', 'C')), # transition to q1, push 'C'
            }
        },
        # READ TILL END OF WORD
        'q1': {
            # END
            '!': {
                'S': ('q2', ''),         # transition to q2, pop 'S'
                'V': ('q2', ('V',)),     # transition to q2
                'C': ('q2', ('C',)),     # transition to q2
            },
            # SPACE
            ' ': {
                'S': ('q0', ('S',)),     # transition to q0
                'V': ('q0', ('V',)),     # transition to q0
                'C': ('q0', ('C',)),     # transition to q0
            },
            # VOWELS
            'a': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'e': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'i': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'o': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'u': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            # CONSONANTS
            'b': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'c': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'd': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'f': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'g': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'h': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'j': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'k': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'l': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'm': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'n': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'p': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'q': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'r': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            's': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            't': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'v': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'w': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'x': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'y': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            },
            'z': {
                'S': ('q1', ('S',)),     # no change
                'V': ('q1', ('V',)),     # no change
                'C': ('q1', ('C',)),     # no change
            }
        },
    },
    initial_state='q0',
    initial_stack_symbol='S',
    final_states={'q2'},
    acceptance_mode='empty_stack'
)

def stepsTable(input_string):
    """
    Pretty-print, as a Markdown table, the sequence of DPDA configurations
    encountered while reading `input_string`.

    This is only used when "Show Step-By-Step" is enabled in the menu.
    """
    table = []
    headers = ["State", "Remaining Input", "Stack"]

    try:
        steps = dpda.read_input_stepwise(input_string)
        for step in steps:
            str_step = str(step)
            parts = str_step.split(', ')
            state = parts[0].split("'")[1]
            remaining_input = parts[1]
            remaining_input = remaining_input.replace("'", "")
            if remaining_input == '':
                remaining_input = 'ε'
            if len(parts) >= 3:
                if parts[2] != "PDAStack())":
                    stack_parts = parts[2:]
                    stack = ''.join([part.split("'")[1] for part in reversed(stack_parts)])
                else:
                    stack = 'ε'
            else:
                stack = 'ε'
            table.append([state, remaining_input, stack])
        table_str = tabulate(table, headers, tablefmt="pipe")
        print(table_str)
    except:
        table_str = tabulate(table, headers, tablefmt="pipe")
        print(table_str)
        print('')
        print("The input is empty but the stack is not empty!")


# DRIVER CODE
show_steps = False
while (1):
    clear()
    print("========================================================================================")
    print('')
    print("Verifies if the string's first letter per word has the same number of consonants/vowels.")
    print('')
    print("For example: captivating melodies echo across the ocean enchanting all who listen")
    print("1st letters: c           m        e    a      t   o     e          a   w   l")
    print('')
    print("c, m, e, a, t, o, e, a, w, l")
    print("This string's words has 5 consonants and 5 vowels as their first letter.")
    print("Because they are balanced, the string will be accepted.")
    print('')
    print("========================================================================================")
    print('')
    print("CHOICES:")
    print('')
    print("[1] Input a String")
    if (show_steps):
        print("[2] Show Step-By-Step [ON]")
    else:
        print("[2] Show Step-By-Step [OFF]")
    print("[3] Exit Program")
    print('')
    print("========================================================================================")
    print('')
    choice = int(prompt("Choice: ", validator=InputValidator(menu=True)))
    if (choice == 1):
        clear()
        print("========================================================================================")
        print('')
        print("Verifies if the string's first letter per word has the same number of consonants/vowels.")
        print('')
        print("For example: captivating melodies echo across the ocean enchanting all who listen")
        print("1st letters: c           m        e    a      t   o     e          a   w   l")
        print('')
        print("c, m, e, a, t, o, e, a, w, l")
        print("This string's words has 5 consonants and 5 vowels as their first letter.")
        print("Because they are balanced, the string will be accepted.")
        print('')
        print("========================================================================================")
        print('')
        print("Valid input is [a-z ] -- that means alphabet and space.")
        print('')
        print("========================================================================================")
        print('')
        input_string = prompt("Input words here: ", validator=InputValidator(alphaSpace=True)).lower()
        if (re.match("^[a-z ]+$", input_string)):
            input_string += '!' # symbolizes end of the string
        else:
            print('')
            print("Invalid input!")
            time.sleep(3) # pause for 3 seconds
            continue
        
        print('')
        print("========================================================================================")
    
        if (show_steps):
            print('')
            stepsTable(input_string)
            print('')
        print('')
        if (dpda.accepts_input(input_string)):
            print('INPUT IS ACCEPTED')
        else:
            print('INPUT IS REJECTED')
        print('')
        print("========================================================================================")
        print('')
        wait = input("Press Enter to continue.")
    if (choice == 2):
        show_steps = False if show_steps else True
    if (choice == 3):
        clear()
        break # exit program