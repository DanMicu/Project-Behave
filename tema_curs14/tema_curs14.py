

class Dreptunghi():
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return f'Dreptunghiul nostru are o lungime de {self.lungime}, o latime de {self.latime} si este {self.culoare}'

    def aria(self):
        return  self.latime * self.lungime

    def perimetrul(self):
        return  2*(self.lungime + self.latime)

    def schimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare








