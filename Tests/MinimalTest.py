from Release.__builtins__minimal import *
#  from __builtins__ import *

for entity in Entities:
    print(entity)

import builtins

MyModule : ModuleType = builtins
MyModuleAny : Any = builtins