import sys
from sa import *

from Schaffer import *

for model in [Schaffer]:
    for optimizer in [sa]:
        optimizer(model())
