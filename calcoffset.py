#%%

import re

f = open('/home/bbales2/record/rec.txt')
lines = f.read()
f.close()

x = 0
y = 0

for line in lines.split('\n'):
    out = re.search('REL_([XY]) ([\-0-9]+)', line)
    
    if out:
        t, d = out.groups()
        
        if t == 'X':
            x += int(d)
        else:
            y += int(d)
            
print x, y