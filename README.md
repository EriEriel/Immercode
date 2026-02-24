# Immercode (.immer)

  **It’s not a bug, it’s a logic deficiency. Spin to win!**

  Immercode is an argumentative, Turing-complete esoteric programming language inspired by the V-tuber ancient automaton, Cecilia Immergreen. In Immercode, you don't "execute" a script; you submit a proposal to a pedantic, green lady who will judge your logic, skip your lines if she’s bored, and rename your file to SKILL_ISSUE.immer if you annoy her too much.

## The Core Mechanic: Hidden Temperament

  Immercode features a Hidden Metadata Temperament System. Cecilia’s mood (ranging from -100 to +100) is never displayed as a number. Instead, you must gauge her "vibe" by her ASCII expressions and dialogue.

**Mood Range**   **State**                   **Behavior**
+51 to +100  High Tea Harmony        Optimized execution; smug satisfaction.
0 to +50     Standard Umu            Normal execution; polite condescension.
-1 to -24    Passive-Aggressive      Sarcastic console logs; slight execution delays.
-25 to -50   Mechanical Malfunction  Glitch Mode: 30% chance to jump to random lines.
< -51        Divine Retribution      CRASH: File is renamed to SKILL_ISSUE.immer.

## Syntax Reference
1. Variables, Math & Comparison operation
  - ```ACTUALLY [var]``` = [val] : Declare/update a variable (Negative Keyword).
  - ```+, -, *``` : Arithmetic.
  - ```/, %``` : Division and Modulo (Negative Keywords; Cecilia finds them "messy").
  - ```==, !=, <, >, <=, >=``` : this inherited from Python because I'm lazy.

2. Conditionals & Loops
  - ```IS IT THOUGH? [condition]``` : An if statement (Negative Keyword).
  - ```DONE.``` : Ends an IS IT THOUGH? block.
  - ```ENCORE! [condition]``` : A while loop. Each iteration costs -1 Mood.
  - ```CURTAIN CALL.``` : Ends an ENCORE! block.

3. The "Chat" Keywords
  - ```UMU / JUSTICE``` : Neutralize negative mood (Positive Keywords).
  - ```I LOVE ~[subject]~``` : Significantly boosts mood (Positive Keyword).
  - ```I HATE ~[subject]~``` : Deletes data but tanks mood (Negative Keyword).
  - ```LISTEN TO ME: ~[msg]~``` : Prints to console, also string need to be in ~ ~.
  - ```VIBE+```: Check Cecilia's current temperament (Careful: can trigger a Mood Swing).

4. Special Commands
  - ```SPIN TO WIN!``` : Roll a d20.
    - 1: Instant crash.
    - 2-10: Random jump.
    - 20: Critical Justice (Mood 100).

## File Naming & Punishment
  - Extension: .immer
  - The Vandalism Clause: If the mood drops below -50, Cecilia will use os.rename() to change your source file to SKILL_ISSUE.immer. She will refuse to run any file with this name until you learn some respect.

## Installation
  1. Ensure you have Python 3.10+ installed.
  2. Save the immer_interpreter.py to your directory.
  3. Run your code:

```python immer_interpreter.py your_logic.immer```

**Warning** : Do not insult green tea within your code. The interpreter is watching.

