

from pkgLinkedList.LinkedList import LinkedList;

print("practica de como se trabaja con las listas de tipo linked")
print("Inicialización")
linkedList = LinkedList();
print("Carga");

linkedList.insertStart(12);
linkedList.insertEnd(122);
linkedList.insertEnd(3);
linkedList.insertStart(31);

linkedList.traverseList();

linkedList.remove(12);
print ("borrado")
linkedList.traverseList();