from .element import Element


class Menu:
    visibleObjects = 4
    _elements = []

    def add_element(self, element: Element):
        self._elements.extend(element)