import sys
import re

file_path = r"c:\Users\kaito\Documents\GitHub\KAMEN-RIDER\妖怪\RPG企画3\Visual_Prompt_Pack_LUMINOUS_WASHI_V3.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

anatomy_neg = "bad anatomy, bad proportions, gross proportions, deformed, disconnected limbs, extra limbs, missing arms, missing legs, mutated hands, poorly drawn hands, extra fingers, floating objects, disconnected objects, surreal AI artifacts, "

new_lines = []
lines = content.split('\n')
i = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    if line.strip() == 'Negative Prompt:':
        i += 1
        if i < len(lines):
            next_line = lines[i]
            if 'bad anatomy' not in next_line:
                if next_line.startswith('**'):
                    new_lines.append('**' + anatomy_neg + next_line[2:])
                else:
                    new_lines.append(anatomy_neg + next_line)
            else:
                new_lines.append(next_line)
    i += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print("Done")
