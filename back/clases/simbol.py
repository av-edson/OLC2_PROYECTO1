class SimbolVariable():
    def __init__(self,nom,tipo,valor,env,fil,col):
        self.nombre = str(nom)
        self.tipo = str(tipo)
        self.valor = str(valor)
        if len(self.valor) > 40:
            self.valor = self.valor[:40]
        self.ambito = str(env)
        self.fila = str(fil)
        self.columna = str(col)