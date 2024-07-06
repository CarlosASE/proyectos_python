import graphviz
import tempfile
import os

class NodoAVL:
    def __init__(self, key):
        self.key = key
        self.altura = 1
        self.izquierdo = None
        self.derecho = None

class ArbolAVL:
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho)

    def rotar_derecha(self, y):
        x = y.izquierdo
        T2 = x.derecho

        x.derecho = y
        y.izquierdo = T2

        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        x.altura = 1 + max(self.obtener_altura(x.izquierdo), self.obtener_altura(x.derecho))

        return x

    def rotar_izquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo

        y.izquierdo = x
        x.derecho = T2

        x.altura = 1 + max(self.obtener_altura(x.izquierdo), self.obtener_altura(x.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))

        return y

    def insertar(self, nodo, key):
        if not nodo:
            return NodoAVL(key), None
        elif key < nodo.key:
            nodo.izquierdo, padre = self.insertar(nodo.izquierdo, key)
            if padre is None:
                padre = nodo
        else:
            nodo.derecho, padre = self.insertar(nodo.derecho, key)
            if padre is None:
                padre = nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierdo), self.obtener_altura(nodo.derecho))

        balance = self.obtener_balance(nodo)

        if balance > 1 and key < nodo.izquierdo.key:
            return self.rotar_derecha(nodo), padre

        if balance < -1 and key > nodo.derecho.key:
            return self.rotar_izquierda(nodo), padre

        if balance > 1 and key > nodo.izquierdo.key:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo), padre

        if balance < -1 and key < nodo.derecho.key:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo), padre

        return nodo, padre

    def nodo_minimo(self, nodo):
        if nodo is None or nodo.izquierdo is None:
            return nodo
        return self.nodo_minimo(nodo.izquierdo)

    def borrar(self, raiz, key):
        if not raiz:
            return raiz
        elif key < raiz.key:
            raiz.izquierdo = self.borrar(raiz.izquierdo, key)
        elif key > raiz.key:
            raiz.derecho = self.borrar(raiz.derecho, key)
        else:
            if raiz.izquierdo is None:
                return raiz.derecho
            elif raiz.derecho is None:
                return raiz.izquierdo
            temp = self.nodo_minimo(raiz.derecho)
            raiz.key = temp.key
            raiz.derecho = self.borrar(raiz.derecho, temp.key)
        if raiz is None:
            return raiz

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierdo), self.obtener_altura(raiz.derecho))
        balance = self.obtener_balance(raiz)

        if balance > 1 and self.obtener_balance(raiz.izquierdo) >= 0:
            return self.rotar_derecha(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecho) <= 0:
            return self.rotar_izquierda(raiz)
        if balance > 1 and self.obtener_balance(raiz.izquierdo) < 0:
            raiz.izquierdo = self.rotar_izquierda(raiz.izquierdo)
            return self.rotar_derecha(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecho) > 0:
            raiz.derecho = self.rotar_derecha(raiz.derecho)
            return self.rotar_izquierda(raiz)

        return raiz

    def buscar(self, nodo, key):
        if nodo is None or nodo.key == key:
            return nodo
        if key < nodo.key:
            return self.buscar(nodo.izquierdo, key)
        return self.buscar(nodo.derecho, key)

    def recorrido_preorden(self, nodo):
        if not nodo:
            return
        print(nodo.key, end=" ")
        self.recorrido_preorden(nodo.izquierdo)
        self.recorrido_preorden(nodo.derecho)

    def recorrido_inorden(self, nodo):
        if not nodo:
            return
        self.recorrido_inorden(nodo.izquierdo)
        print(nodo.key, end=" ")
        self.recorrido_inorden(nodo.derecho)

    def recorrido_postorden(self, nodo):
        if not nodo:
            return
        self.recorrido_postorden(nodo.izquierdo)
        self.recorrido_postorden(nodo.derecho)
        print(nodo.key, end=" ")

    def mostrar_arbol(self, nodo):
        dot = graphviz.Digraph(comment='Arbol AVL')
        self.agregar_nodos(dot, nodo)
        filename = tempfile.mktemp(suffix='.png')
        dot.format = 'png'
        dot.render(filename, view=True)

    def agregar_nodos(self, dot, nodo):
        if nodo:
            dot.node(str(nodo.key))
            if nodo.izquierdo:
                dot.edge(str(nodo.key), str(nodo.izquierdo.key))
                self.agregar_nodos(dot, nodo.izquierdo)
            if nodo.derecho:
                dot.edge(str(nodo.key), str(nodo.derecho.key))
                self.agregar_nodos(dot, nodo.derecho)

def main():
    arbol_avl = ArbolAVL()
    raiz = None

    while True:
        entrada = input("Ingrese el valor del nodo (o 'mostrar' para terminar, 'borrar' para eliminar un nodo, 'buscar' para buscar un nodo): ")
        if entrada.lower() == 'mostrar':
            break
        elif entrada.lower() == 'borrar':
            borrar_valor = input("Ingrese el valor del nodo a borrar: ")
            try:
                key = int(borrar_valor)
                raiz = arbol_avl.borrar(raiz, key)
                print(f"Nodo borrado: {key}")
                arbol_avl.mostrar_arbol(raiz)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif entrada.lower() == 'buscar':
            buscar_valor = input("Ingrese el valor del nodo a buscar: ")
            try:
                key = int(buscar_valor)
                nodo_encontrado = arbol_avl.buscar(raiz, key)
                if nodo_encontrado:
                    print(f"Nodo encontrado: {nodo_encontrado.key}")
                    arbol_avl.mostrar_arbol(nodo_encontrado)  # Mostrar gráficamente el nodo encontrado
                else:
                    print("Nodo no encontrado.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            try:
                key = int(entrada)
                raiz, padre = arbol_avl.insertar(raiz, key)
                if padre:
                    print(f"Nodo insertado: {key}, Padre: {padre.key}")
                else:
                    print(f"Nodo insertado: {key} (es la raíz)")
                arbol_avl.mostrar_arbol(raiz)
            except ValueError:
                print("Por favor, ingrese un número válido o 'mostrar' para terminar.")
            
    # Recorridos
    print("\nPreorden del árbol AVL:")
    arbol_avl.recorrido_preorden(raiz)
    print("\n\nInorden del árbol AVL:")
    arbol_avl.recorrido_inorden(raiz)
    print("\n\nPostorden del árbol AVL:")
    arbol_avl.recorrido_postorden(raiz)

if __name__ == "__main__":
    main()