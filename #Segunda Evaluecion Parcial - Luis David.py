import csv #El nombre del archivo es Arbol - Luis David Ixquiac Sac - 1521223

class Nodo:
    def __init__(self, pregunta=None, nodo_si=None, nodo_no=None, dato=None):
        self.pregunta = pregunta
        self.nodo_si = nodo_si
        self.nodo_no = nodo_no
        self.dato = dato

def preorder(nodo):
    if nodo is not None:
        res = [nodo.pregunta if nodo.pregunta else nodo.dato]
        res.extend(preorder(nodo.nodo_si))
        res.extend(preorder(nodo.nodo_no))
        return res
    return []

def inorder(nodo):
    if nodo is not None:
        res = []
        res.extend(inorder(nodo.nodo_si))
        res.append(nodo.pregunta if nodo.pregunta else nodo.dato)
        res.extend(inorder(nodo.nodo_no))
        return res
    return []

def postorder(nodo):
    if nodo is not None:
        res = []
        res.extend(postorder(nodo.nodo_si))
        res.extend(postorder(nodo.nodo_no))
        res.append(nodo.pregunta if nodo.pregunta else nodo.dato)
        return res
    return []

def exportar_arbol(nodo):
    with open("arbol.csv", "w", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Preorder"] + preorder(nodo))
        writer.writerow(["Inorder"] + inorder(nodo))
        writer.writerow(["Postorder"] + postorder(nodo))

def construir_arbol(preorder, inorder):
    if not preorder or not inorder:
        return None

    raiz = Nodo(pregunta=preorder[0])
    idx_raiz = inorder.index(preorder[0])

    raiz.nodo_si = construir_arbol(preorder[1:idx_raiz + 1], inorder[:idx_raiz])
    raiz.nodo_no = construir_arbol(preorder[idx_raiz + 1:], inorder[idx_raiz + 1:])

    return raiz

def agregar_animal(nodo, animal):
    nueva_pregunta = input("Por favor, ingresa una pregunta que distinga un(a) {} de un(a) {}: ".format(animal, nodo.dato))
    nueva_respuesta = input("¿Cuál es la respuesta para {}? (si/no): ".format(animal)).lower()
    nuevo_nodo = Nodo(pregunta=nueva_pregunta, dato=animal)
    if nueva_respuesta == 'si':
        nodo.nodo_si = nuevo_nodo
        nodo.nodo_no = Nodo(dato=nodo.dato)
    else:
        nodo.nodo_no = nuevo_nodo
        nodo.nodo_si = Nodo(dato=nodo.dato)

def hacer_adivinanza(nodo):
    if nodo.pregunta:
        respuesta = input(nodo.pregunta + " (si/no): ").lower()
        if respuesta == 'si':
            if nodo.nodo_si:
                hacer_adivinanza(nodo.nodo_si)
            else:
                print("¡Adiviné correctamente! El animal es un(a) {}.".format(nodo.dato))
        elif respuesta == 'no':
            if nodo.nodo_no:
                hacer_adivinanza(nodo.nodo_no)
            else:
                print("¡Adiviné correctamente! El animal es un(a) {}.".format(nodo.dato))
        else:
            print("Respuesta inválida. Por favor, responde con 'si' o 'no'.")
            hacer_adivinanza(nodo)
    else:
        adivinanza = input("¿Es un(a) {}? (si/no): ".format(nodo.dato)).lower()
        if adivinanza == 'si':
            print("¡Adiviné correctamente! El animal es un(a) {}.".format(nodo.dato))
        else:
            nuevo_animal = input("¡Vaya! ¿Qué animal era entonces? ")
            if nuevo_animal not in [nodo.dato for nodo in [nodo.nodo_si, nodo.nodo_no] if nodo]:
                agregar_animal(nodo, nuevo_animal)
            else:
                print("¡Ya conozco ese animal!")
            otra_vez = input("¿Quieres jugar de nuevo? (si/no): ").lower()
            if otra_vez == 'si':
                jugar()

def jugar():
    raiz = Nodo(pregunta="¿Vive en el agua?", 
                nodo_si=Nodo(pregunta="¿Tiene aletas?", 
                              nodo_si=Nodo(dato="pez"), 
                              nodo_no=Nodo(dato="rana")), 
                nodo_no=Nodo(pregunta="¿Tiene patas?", 
                             nodo_si=Nodo(dato="ave"), 
                             nodo_no=Nodo(dato="serpiente")))
    
    hacer_adivinanza(raiz)

def menu():
    while True:
        print("\nMENU:")
        print("1. Jugar")
        print("2. Exportar árbol a CSV")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            jugar()
        elif opcion == '2':
            raiz = Nodo(pregunta="¿Vive en el agua?", 
                        nodo_si=Nodo(pregunta="¿Tiene aletas?", 
                                      nodo_si=Nodo(dato="pez"), 
                                      nodo_no=Nodo(dato="rana")), 
                        nodo_no=Nodo(pregunta="¿Tiene patas?", 
                                     nodo_si=Nodo(dato="ave"), 
                                     nodo_no=Nodo(dato="serpiente")))
            exportar_arbol(raiz)
            print("El árbol se ha exportado correctamente a 'arbol.csv'")
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

menu()

