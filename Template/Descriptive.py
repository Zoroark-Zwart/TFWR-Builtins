import BuiltinsBuilder

import Minimal

BuiltinsManager: BuiltinsBuilder.Manager = Minimal.BuiltinsManager
BuiltinsManager.SetName("__builtins__descriptive")
BuiltinsManager.SetVersion("Descriptive")

# print(Minimal.BuiltinsManager.GetName(), Minimal.BuiltinsManager.GetVersion())

# print(BuiltinsManager.GetName(), BuiltinsManager.GetVersion())

# print(BuiltinsManager._Manager__MergedContent)

if __name__ == "__main__":
    BuiltinsManager.MergeGroupings()
    BuiltinsManager.Compile(True)