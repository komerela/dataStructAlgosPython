from typing import List
from time import time

array: List[str] = ['koome']


def finding_nemo(x):

    start = time()
    """

    :param array: 
    """
    arr = len(x)
    for i in range(arr):
        if x[i] == 'nemo':
            print('found nemo well')
        else:
            print('nemo is dead')

    print(time() - start)
finding_nemo(array)
