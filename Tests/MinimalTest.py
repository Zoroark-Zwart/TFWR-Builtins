from Release.__builtins__minimal import *
#  from __builtins__ import *

def test_add(given_set: set[Hashable], object: AnyTFWR) -> None:
    ...


TestSet = set()
TestSet.add(1)
test_add({1, 2, 3}, 4)
test_add(TestSet, 6)