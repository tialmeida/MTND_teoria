import asyncio
from transition import Transition
from direction import Direction
from tape import Tape

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
        else:
            for transition_a in all_transitions:
                new_tape = Tape(tape.getword(), tape.getindex())

                if transition_a.caracter_to_write == '*':
                    caracter_to_write = caracter
                else:
                    caracter_to_write = transition_a.caracter_to_write

                new_tape.write(caracter_to_write, transition_a.direction)
                await run_turing_machine(new_tape, final_states, transition_a.destiny)
                return

    accepted = False

    for final_state in final_states:
        if final_state in end_states:
            accepted = True
            break

    if accepted:
        print('S')
    else:
        print('N')


async def main():
    for word in words:
        await run_turing_machine(Tape(Tape.formatword(word, blank_symbol), None), [], initial_state)


asyncio.get_event_loop().run_until_complete(main())
