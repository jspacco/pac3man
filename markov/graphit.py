import sys
from babbler import Babbler

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

numnodes = 1
names = {}

def frequencies(items):
    counts = {}
    for i in items:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    return counts

def percents(items):
    freqs = frequencies(items)
    percentages = {}
    total = sum(freqs.values())
    for key, count in freqs.items():
        percentages[key] = count / total
    return percentages

def getnode(name):
    global numnodes
    global names
    if name not in names:
        names[name] = f'N{numnodes:03d}'
        numnodes += 1
    return names[name]

def fix(state, word):
    if word is None:
        return None
    if ' ' not in state:
        return word
    return state[state.index(' ')+1:] + ' ' + word

def main(n, filename):
    babbler = Babbler(n)
    babbler.add_file(filename)
    
    st = ''
    startpct = percents(babbler.get_starters())
    for starter in startpct.keys():
        name = getnode(starter)
        st += f'start -> {name} [label = {startpct[starter]:0.2f} fontsize="36"];\n'

    links = ''
    tovisit = list(startpct.keys())
    visited = set()
    while len(tovisit) > 0:
        state = tovisit.pop(0)
        eprint(f'state {state}')
        if state in visited:
            continue
        visited.add(state)

        name = getnode(state)
        if not babbler.has_successor(state):
            links += f'{name} -> end [label = 1.0 fontsize="36"];\n'
            continue

        eprint(f'{state} successors: {babbler.get_successors(state)}')
        
        successors = [(word, fix(state, word)) for word in babbler.get_successors(state)]
        eprint(f'successors of {state}: {successors}')
        
        successorpct = percents(successors)
        eprint(f'successorpct {successorpct}')
        
        for (word, nextstate), weight in successorpct.items():
            if word == 'EOL':
                links += f'{name} -> end [label = "{weight:.2f}" fontsize="36"];\n'
                continue
            nextname = getnode(nextstate)
            if nextname not in visited:
                tovisit.append(nextstate)
            links += f'{name} -> {nextname} [label = "{word}\\n{weight:0.2f}" fontsize="36"];\n'
    
    nodes = ''
    global names
    for state, name in names.items():
        nodes += f'{name} [label="{state}"];\n'


    graph = """
digraph finite_state_machine {
	rankdir=LR;
	size="8,5"
	node [shape = doublecircle fontsize="36"]; start end;
	node [shape = circle fontsize="36"];
    %s
    %s
    %s
}
    """ % (nodes, st, links)

    print(graph)

if __name__ == '__main__':
    n = 3
    filename = 'tests/test2.txt'
    sys.argv.pop(0)
    if len(sys.argv) > 0:
        n = int(sys.argv.pop(0))
    if len(sys.argv) > 0:
        filename = sys.argv.pop(0)
    main(n, filename)