# Implementacja klasy BinaryTree
class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        """
        Inicjalizacja węzła drzewa binarnego.
        :param value: Wartość przechowywana w węźle.
        :param left: Lewe dziecko (BinaryTree lub None).
        :param right: Prawe dziecko (BinaryTree lub None).
        """
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, node):
        """Ustawia lewe dziecko węzła."""
        self.left = node
        if node:
            node.parent = self

    def set_right(self, node):
        """Ustawia prawe dziecko węzła."""
        self.right = node
        if node:
            node.parent = self

    def get_left(self):
        """Pobiera lewe dziecko węzła."""
        return self.left

    def get_right(self):
        """Pobiera prawe dziecko węzła."""
        return self.right

    def draw(self, level=0):
        """Wizualizacja drzewa binarnego w formie tekstowej."""
        if self.right:
            self.right.draw(level + 1)
        print("    " * level + str(self.value))
        if self.left:
            self.left.draw(level + 1)

# Funkcja do liczenia pochodnej
def derivative(tree, var):
    """
    Liczy pochodną wyrażenia reprezentowanego przez drzewo binarne.
    :param tree: Korzeń drzewa binarnego (BinaryTree).
    :param var: Zmienna, względem której liczymy pochodną (str).
    :return: Nowe drzewo binarne reprezentujące pochodną wyrażenia.
    """
    if not tree:
        return None
    if tree.value == var:  # Zmienna
        return BinaryTree(1)
    if isinstance(tree.value, (int, float)):  # Stała
        return BinaryTree(0)

    if tree.value == '+':  # Dodawanie
        return BinaryTree('+', derivative(tree.get_left(), var), derivative(tree.get_right(), var))
    if tree.value == '-':  # Odejmowanie
        return BinaryTree('-', derivative(tree.get_left(), var), derivative(tree.get_right(), var))
    if tree.value == '*':  # Mnożenie (iloczyn)
        left = BinaryTree('*', derivative(tree.get_left(), var), tree.get_right())
        right = BinaryTree('*', tree.get_left(), derivative(tree.get_right(), var))
        return BinaryTree('+', left, right)
    if tree.value == '/':  # Dzielenie
        numerator = BinaryTree('-', 
                        BinaryTree('*', derivative(tree.get_left(), var), tree.get_right()), 
                        BinaryTree('*', tree.get_left(), derivative(tree.get_right(), var)))
        denominator = BinaryTree('*', tree.get_right(), tree.get_right())
        return BinaryTree('/', numerator, denominator)
    if tree.value == '^':  # Potęgowanie (x^n)
        if isinstance(tree.get_right().value, (int, float)):
            exponent = tree.get_right().value
            new_exp = BinaryTree(exponent - 1)
            left = BinaryTree('*', BinaryTree(exponent), BinaryTree('^', tree.get_left(), new_exp))
            return BinaryTree('*', left, derivative(tree.get_left(), var))

    return None

# Test pochodnej: Wyrażenie x^2 + 3x
expression = BinaryTree('+',
    BinaryTree('^', BinaryTree('x'), BinaryTree(2)),  # x^2
    BinaryTree('*', BinaryTree(3), BinaryTree('x'))   # 3x
)

# Liczenie pochodnej
result = derivative(expression, 't')

# Rysowanie drzewa wejściowego i wynikowego
print("Drzewo wejściowe (x^2 + 3x):")
expression.draw()

print("\nDrzewo wynikowe (pochodna):")
result.draw()