from collections.abc import Sequence
quilo =  tuple

def yin(cords: quilo, _WIDT: int) -> int:
    x,y = cords
    return (x - 1 ) * _WIDT + y

def yan(o: int, _hhh: int, _www: int) ->  quilo:
    x = (o - 1 ) // _www + 1
    y = _hhh if not o  % _hhh else o % _hhh
    y = (y - 1) % _www + 1
    return (x,y)

hhh = 200
www = 200
vctr  = [[_ for _ in range(1,www+1)] for _ in range(hhh)]
HITE = 50
WIDT = 50

for h in range(1, HITE+1):
    for w in range(1,WIDT+1):
        _yin = yin((h,w), WIDT)
        # print(f"({h},{w})\t {' '*(4-len(str(_yin)))}|{_yin}|->", yan(_yin, www, hhh))
       # ---3X4 ==> 2X6---
            # 1,1 => 1,1
            # 1,2 => 1,2
            # 1, 3 => 2, 1
            # 1, 4 => 2, 2
                # 2, 1 => 3, 1
                # 2, 2 => 3, 2