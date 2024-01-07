def make_trie (word_array):
    trie = {}
    current = None
 
    for i in range(len(word_array)):
        current = trie
        for c in word_array[i]:
            if c not in current: 
                current[c] = {}
            current = current[c]
 
        current["value"] = i + 1

    return trie
 

def solve(line : str):
    english_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    root = make_trie(english_numbers)
    currentRoot = root
    
    frontier = DFS() 
    frontier.add(Node(line[0], Node(None, None)))
    
    result = ''
    
    for i in range(len(line)):
        node = frontier.frontier[i]
        print(f'Node : {node.state}') 
        
        vNode = node.state
        if vNode.isnumeric(): 
            result += vNode
            currentRoot = root
            print(f'    Digit {vNode} found in : {line}')
            print(f'Result : {result}')

        else:
            print(f'    word found : {vNode}')
            print(f'    Parent {node.parent.state}')
            print(f'    Condition : {node.parent in root}')
            if vNode in currentRoot:
                currentRoot = currentRoot[vNode]
            else:
                prev = node.parent
                if prev.state in root and vNode in (prevRoot := root[prev.state]):
                    currentRoot = prevRoot[node.state]
                elif vNode in root:
                    currentRoot = root[vNode]
                else:
                    currentRoot = root        
                    
            if 'value' in currentRoot:
                print(f'    Number String Found : {currentRoot["value"]} in {line}')
                result += str(currentRoot['value'])
                print(f'Result : {result}')
                
                if vNode in root:
                    currentRoot = root[vNode]
                else: 
                    currentRoot = root

        try:
            nextNode = line[i + 1]
        except IndexError:
            break
        print(f'Current root : {currentRoot}')
        child = Node(nextNode, parent = node)
        frontier.add(child) 
        print()
    
    return result


def calibrate(line : str): 
    numbers = solve(line)
    if len(numbers) != 0:
        result = int(numbers[0] + numbers[-1])
    else:
        result = 0 
        
    print(result)
    return result


def main():
    total = 0
    with open('input.txt', 'r') as lines:
        with open('found.txt', 'a') as file: 
            for line in lines: 
                answer = calibrate(line)
                file.write(f'{answer}\n')
                total += answer
                print()
                
    print(total)


class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent 


class DFS:
    def __init__(self):
        self.frontier = []

    def next(self):
        if front := self.frontier != []:
            self.frontier = front[1:]
    
    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        self.frontier.pop() 
    
    def containsState(self, state): 
        return any(node.state == state for node in self.frontier)

    def empty(self): 
        return len(self.frontier) == 0


if __name__ == '__main__':
    main()
    
    
