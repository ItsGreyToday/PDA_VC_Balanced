## PDA – Balanced Vowel/Consonant First Letters

Interactive command-line tool that uses a deterministic pushdown automaton (DPDA) to check whether a sentence has the **same number of vowel-starting and consonant-starting words**.

### Features

- **DPDA-based checker**: Implements a formal pushdown automaton via `automata-lib`.
- **Input validation**: Ensures only lowercase letters and spaces are accepted as input.
- **Step-by-step mode**: Optionally shows each DPDA configuration as a Markdown-style table.

### Requirements

Install the dependencies with `pip` (Python 3.8+ recommended):

```bash
pip install automata-lib prompt_toolkit tabulate
```

### Usage

Run the main script:

```bash
python vc_balanced.py
```

You will see a simple menu:

- **[1] Input a String** – Enter a sentence consisting only of lowercase letters `a–z` and spaces.
- **[2] Show Step-By-Step [ON/OFF]** – Toggle whether to display the DPDA’s stepwise execution as a table.
- **[3] Exit Program** – Quit the application.

#### What is being checked?

For each word in the sentence, only the **first letter** is examined. The tool counts how many of those first letters are vowels (`a, e, i, o, u`) and how many are consonants. If the counts are equal, the input is **ACCEPTED**; otherwise, it is **REJECTED**.

Example sentence (balanced):

```text
captivating melodies echo across the ocean enchanting all who listen
```

The first letters are:

```text
c, m, e, a, t, o, e, a, w, l
```

There are 5 consonants and 5 vowels, so the DPDA accepts this input.

### Notes

- Input must match the pattern `[a-z ]+` (lowercase letters and spaces only).
- Internally, the program appends a special end marker `!` to signal the end of input to the DPDA.

### Technicalities

<img width="1552" height="873" alt="7tuple" src="https://github.com/user-attachments/assets/b2d8777b-fa18-4db2-a488-7c21578bc49c"/>

<img width="666" height="526" alt="transition" src="https://github.com/user-attachments/assets/4712f927-8261-4410-9474-39d5860e4027"/>

There are 3 states which are q0, q1 and q2. q0 state is the initial state while q2 state is the final state. The first letter of the input will go into q1 state and any letter input will remain in q1 state. However, if a space is detected, the state will go back to q0 state and will continue to remain in q0 state unless a letter is detected. If an exclamation point is detected, the state will go to q2 state which is the final state whether the state is in q0
and q1.

In stack, there are 3 elements which are V for vowels, C for consonants and S for Stack. The S element is pushed into the stack by default. If a vowel is detected in the first letter of the word, the V element will be pushed into the stack. If it is a consonant, the C will be pushed into the stack. If the stack contains one consonant and one vowel they cancel each other out, popping them out of the stack. If the exclamation point is detected at the end of the sentence and there are no remaining C and S elements in the stack, The S element will pop out making the stack empty. Making your input marked accepted. However, if there are remaining C or S elements left in the stack, your input will be marked rejected.

### Screenshots

Menu:

<img width="715" height="385" alt="menu" src="https://github.com/user-attachments/assets/7c46d50a-8ff5-4cb8-956d-587f976c2046"/>

Example Input:

<img width="712" height="783" alt="example" src="https://github.com/user-attachments/assets/6df38565-7bd1-4ed1-b508-e29a3e19d356" />
