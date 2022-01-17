string = 'entten teentten teelika mentten hissun kissun vaapula kissun eelin keelin klot viipula vaapula vot puh pah pelistä pois'
arr = string.split(' ')

targets = [1, 2, 3, 4, 5, 6, 7, 8, 9]

complete = False
while complete != True:
    for s in arr:
        print (s)
        for i, t in enumerate(targets):
            if (i + 1 == (len(targets)) and s == 'pois'):
                print('\n')
                print (str(t) + ' on pois')
                complete = True
