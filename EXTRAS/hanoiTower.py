def torre_hanoi(n):
    torres = {
        "A" : list(range(n,0,-1)),
        "B" : [],
        "C" : []
    }
    nombres  =["A", "B","C"]
    
    def mover(origen, destino): 
        disco = torres[origen].pop() 
        torres = destino.append(disco)
        print(f"Mover disco {disco}: {origen} -> {destino}")

    def mover_disco1():
        for i in range(3):
            # Busca en qué torre está el disco 1
            torre = nombres[i]
            
            if torres[torre] and torres[torre][-1] == 1: #-1 es el ultimo elemento
                posicion = i
                break
            
        if n % 2 == 0: 
            nueva_posicion = (posicion+1) % 3 #mod de tres para siempre usar A,B,C
        else:
            nueva_posicion = (posicion-1)% 3
            
        mover(nombres[posicion], nombres[nueva_posicion])
        
    def mover_otro_disco():
        for torre in nombres:
            if torres[torre] and torres[torre][-1] == 1: 
                torre_disco_1 = torre
                break
            
        otras = []
        
        for torre in nombres:
            if torre != torre_disco_1:
                otras.append(torre)
        
        torre1 = otras[0]
        torre2 = otras[1]        
                
                

