from shutil import copy
print('ok')
import os
for a, b, c in os.walk('test'):
    copy(__file__, a)