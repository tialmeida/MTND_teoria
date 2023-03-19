# import asyncio
# import time
#
#
# async def a():
#     time.sleep(5)
#     print('After')
#
#
# async def main():
#     print('Before')
#     await a()
#
#
# asyncio.get_event_loop().run_until_complete(main())
# import ctypes
#
# copy = ctypes.pythonapi._PyUnicode_Copy
# copy.argtypes = [ctypes.py_object]
# copy.restype = ctypes.py_object
#
# s1 = 'xxxxxxxxxxxxx'
# s2 = copy(s1)
#
# print(id(s1), id(s2))  # False

# x = [1, 2, 3, 4, 5]
# if 6 in x:
#   print("Encontrou!")

#
# copy = ctypes.pythonapi._PyUnicode_Copy
# copy.argtypes = [ctypes.py_object]
# copy.restype = ctypes.py_object
# word = 'Tiago'
# word_copy = copy(word)
# word_copy += word_copy[:2] + 'A' + word_copy[3:]
#
# print(word)
# print(word_copy)


def run_tm(config, tape_input):
    # Lendo as configurações da máquina de Turing
    states = config[0].split()
    input_alphabet = config[1].split()
    tape_alphabet = config[2].split()
    leftmost_symbol = config[3]
    blank_symbol = config[4]
    transitions_count = int(config[5])
    transitions = {}
    for i in range(transitions_count):
        t = config[i + 6].split()
        state, symbol, new_state, new_symbol, direction = t[0], t[1], t[2], t[3], t[4]
        transitions[(state, symbol)] = (new_state, new_symbol, direction)

    initial_state = config[6 + transitions_count]
    final_states = config[7 + transitions_count].split()

    # Inicializando a fita
    tape = Tape(tape_input, blank_symbol, leftmost_symbol)

    # Inicializando a máquina de Turing
    tm = TuringMachine(states, input_alphabet, tape_alphabet, transitions,
                       initial_state, final_states)

    # Rodando a máquina de Turing
    tm.run(tape)

    # Verificando se a palavra foi aceita ou rejeitada
    if tm.current_state in final_states:
        return 'Aceita'
    else:
        return 'Rejeitada'
