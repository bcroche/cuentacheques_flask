

class Mochila:
    def __init__(self) -> None:
        self.elementos = []
        self.numero_cheques = 0
        self.valor_actual = 0
        
    

    def add(self, numCheques,valorCheque):
        self.elementos.append((numCheques, valorCheque))
        self.numero_cheques += numCheques
        self.valor_actual += numCheques*valorCheque
    def peso(self):
        return self.valor_actual
    def cheques(self):
        return self.numero_cheques
    def copy(self):
        newM = Mochila()
        newM.elementos= self.elementos.copy()
        newM.numero_cheques= self.numero_cheques
        newM.valor_actual = self.valor_actual
        return newM



def reset(n, lista):
        for e in range(n, len(lista)):
            lista[e] = (0,0)

class ChequesSolver:
    cheques = 0
    niveles= 0
    soluciones_analizadas = 0

    def __init__(self, cheques):
        self.cheques = cheques
        self.cheques.sort()
        #print("Tipos de cheques: ", self.cheques)        



    def calculaRec(self, cantidad, nivel, mochila: Mochila, mochilaCand: Mochila):
        if nivel == self.niveles:
            #print ("Caso base", mochilaCand)
            self.soluciones_analizadas= self.soluciones_analizadas + 1

            
            pCand= mochilaCand.peso()
            pMochila= mochila.peso()
            if pCand > cantidad:
                return mochila
            if pCand > pMochila:
                #mochila= mochilaCand
                return mochilaCand
            else:
                if pCand == pMochila:
                    nCand= mochilaCand.cheques()
                    nMochila= mochila.cheques()
                    if nCand < nMochila:
                        #mochila= mochilaCand
                        return mochilaCand
            return mochila
        else:
            #print ("Caso recursivo")
            
            pesoCand = mochilaCand.peso()
            maxCheques= int((cantidad - pesoCand) / self.cheques[nivel]) 
            temp = mochilaCand.copy()
            for i in range(maxCheques+1):
                #reset(nivel, mochilaCand)                                
                mochilaCand.add(i, self.cheques[nivel])
                mochila = self.calculaRec(cantidad, nivel + 1, mochila, mochilaCand)                
                mochilaCand= temp.copy()
        return mochila



    

    def calcula(self,cantidad):
        mochila= Mochila()
        mochilaCand = Mochila()
        self.niveles= len(self.cheques)
        print("Mochila: ", mochila.elementos)
        mochila= self.calculaRec(cantidad, 0, mochila, mochilaCand)
        return mochila
    
    





    


