#Self-recovery, if librr or init has issue, run this
#It is better to solve issue using these before running a full recovery which is time consuming

import os
pth=os.path.pardir(__file__)
os.remove(os.path.join(pth, '__init__.py'))
os.remove(os.path.join(pth, librr.py))
with open('__init__.py', 'w') as f:
    f.write()
os.system('git clone https://github.com/rish27c/librr.git')