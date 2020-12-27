#### ============================ ####
# terrible design thanks to ME / arindam chow
# this is really dumb as to how unnecessarily complicated this has begun to be, i will shink it down TODO
#### ============================ ####

from tensor_annotations.tensorflow import Tensor1, Tensor0

def globalize(f):
    global dic, tensor0
    def new(type_, **dic):
        x,y = dic
        return f(type_, **dic)
    return new    

class d_tensor(Tensor0):
    # this needs to be difined
    # x,y = dic
    def __init__(self, type_):
        self.A1 = Tensor1[type_]

class d_tensor1(object):
    def setdic(data1, data2):
        for x,y in zip(data1, data2):
            dic1[x] = int
            dic1[y] = float
    
    # TODO expand the tensor classes 
    @globalize
    def main(type_,**dic):
        d_t = d_tensor(type_)
        return d_t.A1

    def __init__(self, **dic):
        self.t0 = d_tensor1.main(float, **dic)
        

def run():
    a =["test" ]
    b =["test1"]
    d_tensor1.setdic(a, b)
    d = d_tensor1(**dic1)
    return d.t0

dic1 = {}
print(run())




