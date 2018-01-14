
# coding by Captain

class araba():


    def __init__(self,marka,model,renk):
        self.marka = marka
        self.model = model
        self.renk = renk

    def bilgilerigöster(self):
        print("Marka: {}\nModel: {}\nRenk: {}".format(self.marka,self.model,self.renk))

    def bilgigir(self):
        self.marka = input("Marka giriniz: ")

        self.model = input("Model giriniz: ")

        self.renk = input("Renk giriniz: ")



a1 =araba("","","")

a1.bilgigir()

a1.bilgilerigöster()





























