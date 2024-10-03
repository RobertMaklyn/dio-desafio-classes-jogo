
class Heroi:
    TIPOS_VALIDOS = ["guerreiro", "mago", "monge", "ninja"]

    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido! Escolha entre: {', '.join(self.TIPOS_VALIDOS)}")
        self.tipo = tipo

   
    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"

       
        print(f"O {self.tipo} atacou usando {ataque}")



try:
    heroi1 = Heroi("Arthur", 30, "guerreiro")
    heroi2 = Heroi("Merlin", 150, "mago")
    heroi3 = Heroi("Lee", 25, "monge")
    heroi4 = Heroi("Hanzo", 28, "ninja")
    

   
    heroi1.atacar()  
    heroi2.atacar()  
    heroi3.atacar()  
    heroi4.atacar()  

except ValueError as e:
    print(e)
