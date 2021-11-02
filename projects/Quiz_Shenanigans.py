"""A Funny Program."""


def zip_dict(ks: list[str], vs: list[str]) -> dict[str, str]: 
    d: dict[str, str] = {}

    if len(ks) != len(vs): 
        return d 

    i: int = 0 
    while i < len(ks): 
        d[ks[i]] = vs[i]
        i += 1 

    print(d)
    return d 


a: list[str] = ["B", "O", "O"] 
b: list[str] = []
c: dict[str, str] = zip_dict(a, b) 
