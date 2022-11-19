def Push(p, v):
    global topo
    topo += 1
    p.insert(topo, v)

def Pop(p):
    global topo
    p.pop()
    topo -=1

def Ins_Ordenado(pilha,val):
    aux = []
    topoaux = -1
    global topo
    while (topo != -1 and val>pilha[topo]):
        topoaux +=1
        aux.insert(topoaux,pilha[topo])
        Pop(pilha)
    
    Push(pilha, val)    
    while topoaux!=-1:
        Push(pilha,aux[topoaux])
        aux.pop()
        topoaux-=1
    
    
def Esvaziar(pilha):
    global topo
    while topo!= -1:
        print(pilha[topo])
        Pop(pilha)








pilha =[]
topo=-1
while True:
    print("\n1 - Inserir na pilha")
    print("2 - Esvaziar a pilha")
    print("0 - Sair do programa")

    op = int(input("Digite a opcao: "))

    if op==0:
         break
    elif op==1:
        val = int(input("Digite o valor a inserir: "))
        if topo==-1:   # se pilha está vazia
            Push(pilha, val)
        else:
            if val < pilha[topo]:
                Push(pilha, val)
            else:
                Ins_Ordenado(pilha, val)


    elif op==2:
        Esvaziar(pilha)
