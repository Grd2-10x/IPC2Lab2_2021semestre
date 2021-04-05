import Nodo

class lista_circular:
    def leer(data):
        for a in data:
         print("calculando")
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insertar(self, cliente):
        if self.size == 0:
            self.head = Nodo(cliente=cliente)
            self.head.next = self.head
        else:
            new_node = Nodo(cliente=cliente, next=self.head.next)
            self.head.next = new_node
        self.size += 1

    def imprimir(self):
        if self.head is None:
            return
        node = self.head
        print(node.cliente.no_habitacion, node.cliente.nombre, end=" => ")
        while node.next != self.head:
            node = node.next
            print(node.cliente.no_habitacion, node.cliente.nombre, end=" => ")

    def eliminar(self, no_habitacion):
        node = self.head
        previous = None

        while True:
            if node.cliente.no_habitacion == no_habitacion:
                if previous is not None:
                    previous.next = node.next
                else:
                    while node.next != self.head:
                        node = node.next
                    node.next = self.head.next
                    self.head = self.head.next
                self.size -= 1
                return True
            elif node.next == self.head:
                return False

            previous = node
            node = node.next

    def ordenar(self, no_habitacion):
        for path in range(1, len(self.linked_list_circular)):
            for num in range(len(self.linked_list_circular) - path):
                if self.linked_list_circular[num] > self.linked_list_circular[num + 1]:
                    temp = self.linked_list_circular[num]
                    self.linked_list_circular[num] = self.linked_list_circular[num + 1]
                    self.linked_list_circular[num + 1] = temp