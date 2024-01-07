import pandas as pd
import re

def main():
    with open('input.txt', 'r', newline = '') as file:
        frame = []
        
        for line in file:
            game, results = line.strip().split(':')
            gameID = re.search('(\d+)', game)
            gameID = int(gameID.group(0))
            result = results.split(';')
            
            for round in result:
                matches = re.findall('(\d+) (blue|red|green)', round)                
                temp = {'ID' : gameID,
                        'red' : 0,
                        'green' : 0,
                        'blue' : 0}
                        
                for count, color in matches:
                    temp[color] = int(count)
                    
                frame.append(temp)  
                
    print('MATCH RESULT')
    red = int(input('Red : '))            
    blue = int(input('Blue : '))
    green = int(input('Green : '))
            
    df = pd.DataFrame(frame)
    df['passedTest'] = (df['red'] <= red) & (df['green'] <= green) & (df['blue'] <= blue)
    
    df_pct = df.groupby('ID')['passedTest'].mean().reset_index()
    pt1Solution = df_pct.query('passedTest == 1')['ID'].sum()
    
    df_max = df.groupby('ID')[['red', 'green', 'blue']].max()
    df_max['power'] = df_max['red'] * df_max['green'] * df_max['blue']
    pt2Solution = df_max['power'].sum() 

    print(pt2Solution)


if __name__ == '__main__':
    main() 