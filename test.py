#### ============================ ####
# terrible design thanks to ME / arindam chow

from tensor_annotations.tensorflow import Tensor1, Tensor0

def globalize(f):
    global dic, tensor0
    dic = {"x":int, "y":float}
    def new(**dic1):
        x,y = dic1
        tensor0 =Tensor0[dic1[x]]
        return tensor0
    return new    

class d_tensor(Tensor0):
    # this needs to be difined
    # x,y = dic
    def __init__(self):
        self.A1 = Tensor1[self.test()]

class d_tensor1(object):
    def setdic(data1, data2):
        for x,y in zip(data1, data2):
            dic1[x] = int
            dic1[y] = float

    @globalize
    def main(dic):
        t = d_tensor()
        return dic

    def __init__(self, **dic):
        dic | dic1
        self.t0 = d_tensor1.main(**dic)
        

def run():
    a =["test" ]
    b =["test1"]
    d_tensor1.setdic(a, b)
    d = d_tensor1(**dic1)
    return d.t0

dic1 = {}
print(run())




