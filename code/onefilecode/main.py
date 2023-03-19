import asyncio
from enum import Enum
import ctypes


class Transition:
    def __init__(self, destiny, caracter_to_write, direction):
        self.destiny = destiny
        self.caracter_to_write = caracter_to_write
        self.direction = direction


class Direction(Enum):
    L = 'E'
    R = 'D'
    I = 'I'

    @staticmethod
    def get_from_value(value):
        if Direction.L.value == value:
            return Direction.L
        elif Direction.R.value == value:
            return Direction.R
        else:
            return Direction.I


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
        copy = ctypes.pythonapi._PyUnicode_Copy
        copy.argtypes = [ctypes.py_object]
        copy.restype = ctypes.py_object
        return f'<{copy(word)}{blank_symbol}'


states = input().split(" ")
alphabet = input().split(" ")
alphabet_tape = input().split(" ")
start_tape = input()
blank_symbol = input()
transtions_number = int(input())
transtions = []

for count in range(0, transtions_number):
    transtions.append(input().split(" "))

initial_state = input()
end_states = input().split(" ")

machine = {}

for state_aux in states:
    machine[state_aux] = {}

    for transtion in transtions:
        if transtion[0] == state_aux:
            if machine[state_aux].get(transtion[1]) is None:
                machine[state_aux][transtion[1]] = []

            machine[state_aux][transtion[1]].append(Transition(
                transtion[2],
                transtion[3],
                Direction.get_from_value(transtion[4]))
            )

words = input().split(" ")


async def run_turing_machine(tape, final_states, state):
    while True:
        caracter = tape.getcaracter()
        transition_joker = machine[state].get('*')
        transitions_caracter = machine[state].get(caracter)
        all_transitions = []

        if transitions_caracter is not None:
            all_transitions = transitions_caracter.copy()

        if transition_joker is not None and transition_joker[0] not in all_transitions:
            all_transitions.append(transition_joker[0])

        if len(all_transitions) == 0:
            final_states.append(state)
            break
        elif len(all_transitions) == 1:
            tape.write(all_transitions[0].caracter_to_write, all_transitions[0].direction)
            state = all_transitions[0].destiny
            print(tape.getword())
        else:
            for transition_a in all_transitions:
                new_tape = Tape(tape.getword(), tape.getindex())

                if transition_a.caracter_to_write == '*':
                    caracter_to_write = caracter
                else:
                    caracter_to_write = transition_a.caracter_to_write

                new_tape.write(caracter_to_write, transition_a.direction)
                await run_turing_machine(new_tape, final_states, transition_a.destiny)

            break


async def main():
    for word in words:
        print('\n\n')
        final_states = []
        await run_turing_machine(Tape(Tape.formatword(word, blank_symbol), None), final_states, initial_state)
        print(final_states)

        accepted = False

        for final_state in final_states:
            if final_state in end_states:
                accepted = True
                break
        if accepted:
            print('S')
        else:
            print('N')


asyncio.get_event_loop().run_until_complete(main())
