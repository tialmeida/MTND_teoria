import sys


class Edge:
    def __init__(self, start, read_letter, end, written_letter, direction):
        self.start = start
        self.read_letter = read_letter
        self.end = end
        self.written_letter = written_letter
        self.direction = direction


class Vertice:
    is_initial = False
    is_final = False

    def __init__(self, dado):
        self.dado = dado


class Fork:
    def __init__(self):
        self.vertice_initial = None
        self.edges = []
        self.vertices = []

    def add_vertice(self, data):
        vertice = Vertice(data)
        self.vertices.append(vertice)

    def add_edge(self, start_data, read_letter, end_data, written_letter, direction):
        inicio = self.getvertice(start_data)
        fim = self.getvertice(end_data)

        aresta = Edge(inicio, read_letter, fim, written_letter, direction)

        self.edges.append(aresta)

    def getvertice(self, data):
        for v in self.vertices:
            if v.dado == data:
                return v

    def setinitial(self, data):
        for v in self.vertices:
            if v.dado == data:
                v.is_initial = True
                self.vertice_initial = v
                break

    def setfinal(self, data):
        for v in self.vertices:
            if v.dado == data:
                v.is_final = True
                break

    def is_recognized(self, w, lim_left, lim_right):  # MT
        word = list(w)
        word.insert(0, lim_left)
        word.insert(word.__len__(), lim_right)

        T = [(self.vertice_initial, 1, word)]
        end = False
        accepted = False

        while True:
            for t in T:
                found = False
                for a in self.edges:
                    if a.start == t[0] and (a.read_letter == t[2][t[1]]):
                        nextWord = t[2].copy()
                        nextWord[t[1]] = a.written_letter

                        if a.direction == 'D':
                            head = t[1] + 1
                        elif a.direction == 'E':
                            head = t[1] - 1
                        else:
                            head = t[1]

                        if head == nextWord[nextWord.__len__() - 1]:
                            nextWord.insert(nextWord.__len__(), lim_right)

                        nextState = a.end
                        T.append((nextState, head, nextWord))
                        found = True

                if found is False and t[0].is_final:
                    accepted = True
                    end = True
                    break

                T.remove(t)

                if T.__len__() == 0:
                    end = True
                    break

            if end is True:
                break

        if accepted:
            return "S"
        else:
            return "N"


fork = Fork()

word = ''
words = []
out = sys.stdout

states = sys.stdin.readline()
for s in states.rstrip():
    if s != ' ':
        fork.add_vertice(s)

alphabet = sys.stdin.readline()
for a in alphabet:
    if a != ' ':
        alphabet = alphabet + a

alphabet_tape = sys.stdin.readline()
for a in alphabet_tape:
    if a != ' ':
        alphabet = alphabet_tape + a

lim_left = sys.stdin.readline().rstrip()
lim_right = sys.stdin.readline().rstrip()
n_transitions = sys.stdin.readline().rstrip()

n = 0
while n < int(n_transitions):
    transitions = sys.stdin.readline()
    if transitions.rstrip() != '':
        n = n + 1
        fork.add_edge(start_data=transitions[0], read_letter=transitions[2], end_data=transitions[4],
                      written_letter=transitions[6], direction=transitions[8])

start_state = sys.stdin.readline()
fork.setinitial(start_state.rstrip())

final_states = sys.stdin.readline()
for s in final_states.rstrip():
    if s != ' ':
        fork.setfinal(s)

input_words = sys.stdin.readline()
count = 0
for p in input_words.rstrip():
    if p != ' ':
        word = word + p
    else:
        words.append(word)
        word = ''

    count = count + 1

    if count == len(input_words.rstrip()):
        words.append(word)

for w in words:
    out.write(fork.is_recognized(w, lim_left, lim_right) + '\n')
