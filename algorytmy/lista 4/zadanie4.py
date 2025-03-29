class BinaryTree:
    def __init__(self, value=None, parent=None):
        """
        Inicjalizacja węzła drzewa binarnego.
        :param value: Wartość przechowywana w węźle.
        :param parent: Rodzic węzła (instancja BinaryTree lub None).
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def set_root(self, value):
        """
        Ustawia wartość korzenia drzewa.
        :param value: Nowa wartość korzenia.
        """
        self.value = value

    def set_left(self, node):
        """
        Ustawia lewe dziecko węzła.
        :param node: Węzeł (BinaryTree) do ustawienia jako lewe dziecko.
        """
        self.left = node
        if node:
            node.parent = self

    def set_right(self, node):
        """
        Ustawia prawe dziecko węzła.
        :param node: Węzeł (BinaryTree) do ustawienia jako prawe dziecko.
        """
        self.right = node
        if node:
            node.parent = self

    def get_left(self):
        """
        Pobiera lewe dziecko węzła.
        :return: Instancja BinaryTree lub None.
        """
        return self.left

    def get_right(self):
        """
        Pobiera prawe dziecko węzła.
        :return: Instancja BinaryTree lub None.
        """
        return self.right

    def get_parent(self):
        """
        Pobiera rodzica bieżącego węzła.
        :return: Instancja BinaryTree lub None.
        """
        return self.parent

    def get_sibling(self):
        """
        Pobiera rodzeństwo bieżącego węzła.
        :return: Instancja BinaryTree lub None.
        """
        if not self.parent:
            return None
        if self.parent.left == self:
            return self.parent.right
        elif self.parent.right == self:
            return self.parent.left
        return None

    def get_children(self):
        """
        Pobiera dzieci bieżącego węzła.
        :return: Lista zawierająca lewe i prawe dziecko (lub None, jeśli brak).
        """
        return [self.left, self.right]

    def get_root(self):
        """
        Pobiera korzeń drzewa, zaczynając od bieżącego węzła.
        :return: Instancja BinaryTree będąca korzeniem.
        """
        current = self
        while current.parent:
            current = current.parent
        return current

    def draw(self, level=0):
        """
        Wizualizacja drzewa binarnego w formie tekstowej.
        :param level: Poziom węzła (używane do przesunięcia tekstu).
        """
        if self.right:
            self.right.draw(level + 1)
        print("    " * level + str(self.value))
        if self.left:
            self.left.draw(level + 1)