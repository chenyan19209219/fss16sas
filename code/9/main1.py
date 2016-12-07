
from sk import *
from global_variables import *
from GA import *
import Model


from DE import de
from DTLZ1 import *
from DTLZ3 import *
from DTLZ5 import *
from DTLZ7 import *
data_lists = [['DLTZ3'],['DLTZ5'],['DLTZ7']]
k=0
for model in [DTLZ3,DTLZ5,DTLZ7]:

   # for _ in range(20):
    list_loss=[data_lists[k]]
    for _ in range(20):
            de(GA,model)
            list_loss.append(global_variable.loss_inter)
    data_lists[k]=list_loss
    k=k+1

print data_lists
rdivDemo(data_lists)
