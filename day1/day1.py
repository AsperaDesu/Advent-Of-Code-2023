def main():
    lines = []
    while True:
        try:
            lines.append(input())
        except Exception:
            break
        
    print(solve(lines))
        
def solve(lines : list):
    solution = 0
    for line in lines:
        number = []
        for word in line:
            if word.isdigit():
                number.append(word)
        solution += int(number[0] + number[-1])
    
    return solution        
    
    
if __name__ == '__main__':
    main()