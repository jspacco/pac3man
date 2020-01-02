import sys
from babbler import Babbler

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

def main(n, filename):
    babbler = Babbler(n)
    babbler.add_file(filename)
    
    nodes = 1
    visited = dict()

    st = ''
    startpct = percents(babbler.get_starters())
    for starter in startpct.keys():
        if starter not in visited:
            visited[starter] = f'N{nodes:03d}'
            nodes += 1
        st += f'start -> {visited[starter]} [label = {startpct[starter]:0.2f}];\n'

    tovisit = list(set(babbler.get_starters()))
    
    #while len(tovisit) > 0:
        # pop node
        # if visited, continue
        # compute transition percentages
        # 
    
    # TODO: convert visited into nodes with labels
    # figure out transition labels

    graph = """
digraph finite_state_machine {
	rankdir=LR;
	#size="8,5"
	node [shape = doublecircle]; start end;
	node [shape = circle];
    %s
}
    """ % (st,)

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