import sys
from babbler import Babbler

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
        percentages[key] = count // total
    return percentages

def getnode(name):
    global numnodes
    global names
    if name not in names:
        names[name] = f'N{nodes:03d}'
        nodes += 1
    return names[name]

def main(n, filename):
    babbler = Babbler(n)
    babbler.add_file(filename)
    
    st = ''
    startpct = percents(babbler.get_starters())
    for starter in startpct.keys():
        name = getnode(starter)
        st += f'start -> {name} [label = {startpct[starter]:0.2f}];\n'

    links = ''
    tovisit = startpct.keys()
    visited = set()
    while len(tovisit) > 0:
        state = tovisit.pop()
        if state in visited:
            continue
        visited.add(state)

        name = getnode(state)
        if not babbler.has_successor(state):
            links += f'{name} -> end [label = 1.0]\n'
            continue

        successorpct = percents(babbler.get_successors(state))
        for nextnode in successorpct.keys():
            if nextnode not in visited:
                tovisit.append(nextnode)
            nextname = getnode(nextnode)
            links += f'{name} -> {nextname} [label = {successorpct[nextnode]:0.2f}];\n'
    
    nodes = ''
    global names
    for state, name in names.items():
        nodes += f'{name} [label={state}]\n'


    # TODO: convert visited into nodes with labels
    # figure out transition labels

    graph = """
digraph finite_state_machine {
	rankdir=LR;
	#size="8,5"
	node [shape = doublecircle]; start end;
	node [shape = circle];
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