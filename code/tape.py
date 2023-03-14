from direction import Direction
import ctypes


class Tape:
    def __init__(self, word, index):
        self._word = word
        self._index = index
        self._last_index = len(self._word) - 1  # a limitação do tamanho da fita pode se tornar um problema posterior

        if self._index is None:
            self._index = 1

    def getword(self):
        copy = ctypes.pythonapi._PyUnicode_Copy
        copy.argtypes = [ctypes.py_object]
        copy.restype = ctypes.py_object
        return copy(self._word)

    def getindex(self):
        return self._index

    def getcaracter(self):
        return self._word[self._index]

    def write(self, caracter_to_write, direction):
        self._word = self._word[:self._index] + caracter_to_write + self._word[self._index + 1:]

        if Direction.R == direction and self._index != self._last_index:
            self._index += 1
        elif Direction.L == direction and self._index != 0:
            self._index -= 1

    @staticmethod
    def formatword(word, blank_symbol):
        return f'<{word}{blank_symbol}'
