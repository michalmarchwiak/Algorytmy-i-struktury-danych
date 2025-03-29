class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        """
        Inicjalizacja węzła drzewa binarnego.
        :param value: Wartość węzła
        :param left: Lewe dziecko (BinaryTree lub None)
        :param right: Prawe dziecko (BinaryTree lub None)
        """
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, node):
        """
        Ustawienie lewego dziecka węzła.
        :param node: Instancja BinaryTree
        """
        self.left = node

    def set_right(self, node):
        """
        Ustawienie prawego dziecka węzła.
        :param node: Instancja BinaryTree
        """
        self.right = node

    def get_left(self):
        """
        Pobranie lewego dziecka węzła.
        :return: Instancja BinaryTree lub None
        """
        return self.left

    def get_right(self):
        """
        Pobranie prawego dziecka węzła.
        :return: Instancja BinaryTree lub None
        """
        return self.right

    def draw(self, level=0):
        """
        Wizualizacja drzewa binarnego w formie tekstowej.
        :param level: Poziom węzła (używane do przesunięcia tekstu)
        """
        if self.right:
            self.right.draw(level + 1)
        print("    " * level + str(self.value))
        if self.left:
            self.left.draw(level + 1)

# Tworzenie drzewa dla wyrażenia (((5 + 2) * (2 - 1)) / ((2 + 9) + ((7 - 2) - 1)) * 8)
root = BinaryTree('/')
left_subtree = BinaryTree('*')
left_subtree.set_left(BinaryTree('+'))
left_subtree.set_right(BinaryTree('-'))
left_subtree.left.set_left(BinaryTree(5))
left_subtree.left.set_right(BinaryTree(2))
left_subtree.right.set_left(BinaryTree(2))
left_subtree.right.set_right(BinaryTree(1))

right_subtree = BinaryTree('+')
right_subtree.set_left(BinaryTree('+'))
right_subtree.set_right(BinaryTree('-'))
right_subtree.left.set_left(BinaryTree(2))
right_subtree.left.set_right(BinaryTree(9))
right_subtree.right.set_left(BinaryTree('-'))
right_subtree.right.set_right(BinaryTree(1))
right_subtree.right.left.set_left(BinaryTree(7))
right_subtree.right.left.set_right(BinaryTree(2))

root.set_left(left_subtree)
root.set_right(right_subtree)
tree = BinaryTree('*')
tree.set_left(root)
tree.set_right(BinaryTree(8))

tree.draw()