from typing import Any, List, Tuple
def ralen(*ite: Any) -> range:return (range(ite[0]) if type(ite[0])==int else range(len(ite))) if not len(ite)-1 else range(*ite)


def yinyang(_x_i:int,_y_i:int,_w_i:int,_w_f:int,_h_f:int) -> Tuple[int,int]:
    return  ((((_x_i - 1)*_w_i + _y_i-1)//_w_f + 1),
    ((h_f
    if not ((_x_i - 1)*_w_i + _y_i) % _h_f
    else ((_x_i - 1)*_w_i + _y_i) % _h_f)-1)%_w_f + 1)


def tao(_w_i: int, _h_i: int, _w_f:int,_h_f:int) -> List[List[Tuple[int,int]]]:
    """
    #  Suppose we want a mapping with matrix parameters
    # w_i, h_i, w_f, h_f = 4, 3, 2, 6
    # ---3X4 ==> 2X6---
    # 1,1 => 1,1
    # 1,2 => 1,2
    # 1, 3 => 2, 1
    # 1, 4 => 2, 2
    # 2, 1 => 3, 1
    # 2, 2 => 3, 2
    """
    return [[yinyang(x_i,y_i,w_i,w_f,h_f) for y_i in ralen(1, h_i + 1)] for x_i in ralen(1, w_i + 1)]


if __name__=="__main__":
    w_i, h_i, w_f, h_f = 4, 3, 2, 6
    te_cheng = tao(w_i, h_i, w_f, h_f)
    for y_i in ralen(h_i):
        for x_i in ralen(w_i):
            print(te_cheng[x_i][y_i])

