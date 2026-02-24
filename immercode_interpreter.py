import sys
import random
import re
import os

class ImmercodeInterpreter:
    def __init__(self):
        self.mood = 0 
        self.variables = {}
        self.code = []
        self.pointer = 0
        
        # Keyword Classes
        self.positive_keywords = ["I LOVE", "UMU", "JUSTICE", "TEA", "VIBRATO", "VIBE+"]
        self.negative_keywords = ["I HATE", "ACTUALLY", "ERROR", "WRONG", "REDO", "IS IT THOUGH?"]

    def update_mood(self, line):
        for kw in self.positive_keywords:
            if kw in line: self.mood += 1
        for kw in self.negative_keywords:
            if kw in line: self.mood -= 1
        
        # New: Arithmetic mood penalties
        if "/" in line: self.mood -= 1 # Division is messy
        if "%" in line: self.mood -= 1 # Modulo is pedantic
        
        self.mood = max(-100, min(100, self.mood))

    def get_prefix(self):
        if self.mood > 50: return "(❁´◡` ) Cecilia >"
        if self.mood > 0:  return "( ¬‿¬) Cecilia >"
        if self.mood > -25: return "( -_ -) Cecilia >"
        return "( ╬◣_◢) Cecilia >"

    def terminate_with_prejudice(self, filename):
        prefix = self.get_prefix()
        print(f"{prefix} JUSTICE HAS BEEN SERVED!")
        print(f"{prefix} Your logic is a tragedy. I am renaming this file so you never forget.")
        try:
            os.rename(filename, "SKILL_ISSUE.immer")
            print(f"[*] System: '{filename}' has been renamed to 'SKILL_ISSUE.immer'")
        except Exception:
            pass
        sys.exit("\n[PROGRAM TERMINATED: SKILL ISSUE DETECTED]")

    def evaluate_expression(self, expr):
        # Replace variables
        for var in self.variables:
            if var in expr:
                expr = expr.replace(var, str(self.variables[var]))
        
        try:
            # We use integer division // because CC likes clean numbers
            if "/" in expr and "//" not in expr:
                expr = expr.replace("/", "//")
            
            result = eval(expr)
            return result
        except ZeroDivisionError:
            print(f"{self.get_prefix()} DIVIDING BY ZERO?! That's... that's illegal!")
            self.mood -= 10 # Major penalty
            return 0
        except:
            return None

    def execute_vibe_check(self, filename):
        # Mood Swing logic
        if -50 <= self.mood <= -25:
            if random.random() < 0.3:
                self.mood = random.randint(-60, -10)
                print(f"{self.get_prefix()} Wait... my clockwork skipped! *Clunking* Where were we?")
                if self.mood < -50:
                    self.terminate_with_prejudice(filename)
                return

        if self.mood > 50:
            print(f"{self.get_prefix()} The gears are greased and my brilliance is unmatched. Proceed.")
        elif self.mood > 0:
            print(f"{self.get_prefix()} Umu! Your logic is... acceptable.")
        elif self.mood > -25:
            print(f"{self.get_prefix()} *Sigh* I'm processing your 'code', I guess.")
        else:
            print(f"{self.get_prefix()} My sensors are spiking. I might just skip a few steps...")

    def execute_spin(self):
        roll = random.randint(1, 20)
        prefix = self.get_prefix()
        if roll == 1:
            print(f"{prefix} SPIN TO... WAIT, MY CLOAK IS CAUGHT!")
            sys.exit("Error: SKILL_ISSUE_CRITICAL")
        elif roll <= 10:
            print(f"{prefix} SPIN TO WIN! *Wheeeeeeee!* Where am I?")
            self.pointer = random.randint(0, len(self.code) - 1)
            self.mood -= 2
        elif roll <= 19:
            print(f"{prefix} SPIN TO WIN! A flawless maneuver.")
            self.mood += 5
        else:
            print(f"{prefix} SPIN TO WIN! DIVINE... CRITICAL... JUSTICE!!")
            self.mood = 100
            self.pointer = len(self.code) - 1

    def run(self, filename):
        # Initial check for Skill Issue
        if filename == "SKILL_ISSUE.immer":
            print("( ╬◣_◢) Cecilia > I am not reading a file with that name. Apologize first.")
            return

        with open(filename, 'r') as f:
            self.code = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("//")]

        skip_until_end = False
        loop_stack = []

        while self.pointer < len(self.code):
            line = self.code[self.pointer]
            
            if line == "CURTAIN CALL.":
                if loop_stack:
                    start_idx, condition = loop_stack[-1]
                    if self.evaluate_expression(condition):
                        self.pointer = start_idx
                        self.mood -= 1
                        continue
                    else:
                        loop_stack.pop()
                self.pointer += 1
                continue

            if skip_until_end:
                if line == "DONE.": skip_until_end = False
                self.pointer += 1
                continue

            self.update_mood(line)

            # Check fatal mood BEFORE executing line
            if self.mood < -50:
                self.terminate_with_prejudice(filename)

            if line.startswith("ENCORE!"):
                condition = line.replace("ENCORE!", "").strip()
                if self.evaluate_expression(condition):
                    loop_stack.append((self.pointer + 1, condition))
                else:
                    depth = 1
                    while depth > 0 and self.pointer < len(self.code) - 1:
                        self.pointer += 1
                        if "ENCORE!" in self.code[self.pointer]: depth += 1
                        if "CURTAIN CALL." in self.code[self.pointer]: depth -= 1
            elif "IS IT THOUGH?" in line:
                cond = line.replace("IS IT THOUGH?", "").strip()
                if not self.evaluate_expression(cond): skip_until_end = True
            elif "ACTUALLY" in line:
                parts = line.replace("ACTUALLY", "").split("=")
                self.variables[parts[0].strip()] = self.evaluate_expression(parts[1].strip())
            elif "LISTEN TO ME:" in line:
                val = line.split(":")[1].strip().replace("~", "")
                print(f"{self.get_prefix()} {self.variables.get(val, val)}")
            elif "VIBE+" in line:
                self.execute_vibe_check(filename)
            elif "SPIN TO WIN!" in line:
                self.execute_spin()

            self.pointer += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python immer_interpreter.py <file.immer>")
    else:
        interpreter = ImmercodeInterpreter()
        interpreter.run(sys.argv[1])
