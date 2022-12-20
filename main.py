from collections import deque
# the_stack = deque()

class GrammerHandler:
    def __init__(self):
        self.grammar = [        # @ denotes epsilon
            ['S', '(A)|@'],
            ['A', 'TE'],
            ['E', '&TE|@'],
            ['T', '(A)|a|b|c'],
            ]
        self.driver()

    def driver(self):
        '''Driver function to lead the wave!'''
        self.calculate_firsts()
        self.calculate_follows()
        self.show()

        if not self.check_left_reccursion():
            print("No left Reccursion. You are good to go!")
        else:
            print("Left Reccursion Detected!")
            return
        
    def calculate_firsts(self):
        '''Directly appends first list to individual rules list inside grammar lists.'''
        for i,rule in enumerate(self.grammar):
            firsts = [rule[1][0]] + [rule[1][x+1] for x,s in enumerate(rule[1]) if s == '|']
            self.grammar[i].append(firsts)

        # Simplifying for any capital variables in firsts calculated
        changing = True
        while changing:
            changing = False
            for i,rule in enumerate(self.grammar):
                for x,s in enumerate(rule[2]):
                    if s.isupper():
                        changing = True
                        for y,sr in enumerate(self.grammar):
                            if s == sr[0]:
                                self.grammar[i][2].pop(x)
                                for st in sr[2][::-1]:
                                    if not st in self.grammar[i][2]:
                                        self.grammar[i][2].insert(x,st)

                    

    def calculate_follows(self):
        '''Directly appends follow list to individual rules list inside grammar lists.'''
        for i,rule in enumerate(self.grammar):
            follows = []
            new_follows = []
            for x,r in enumerate(self.grammar):
                if rule[0] in r[1]:
                    for y,s in enumerate(r[1]):
                        if rule[0] == s:
                            inc = y+1
                            execute = True
                            while execute:
                                if inc < len(r[1]) and not r[1][inc] == '|':
                                    if r[1][inc].isupper():
                                        # get the first of 'f' in self.grammar
                                        for ef in self.grammar:
                                            if r[1][inc] == ef[0]:
                                                follows.extend([e for e in ef[2] if e != '@'])
                                                if '@' in ef[2]:
                                                    inc += 1
                                                    break
                                                else:
                                                    execute = False
                                    else:
                                        follows.append(r[1][inc])
                                        break
                                else:
                                    if rule[0] == r[0]:
                                        follows.append('$')
                                    else:
                                        new_follows.append(r[0])
                                    break;
            if len(follows) == 0:
                follows.append("$")
            follows.append(new_follows)
            self.grammar[i].append(follows)
        
        # Solve new follows
        for i,rule in enumerate(self.grammar):
            follows = rule[3][:-1]
            if len(rule[3][-1]) > 0:
                for x,f in enumerate(rule[3][-1]):
                    z = [nf[3] for nf in self.grammar if f == nf[0]]
                    for st in z:
                        follows.extend(st)
            self.grammar[i][3] = sorted(set(follows)) # Remove duplicates and sort follows and than save

                

    def check_left_reccursion(self):
        '''Checks for any left reccursion in the grammar. Returns bool()'''
        for i,r in enumerate(self.grammar):
            if r[0] in r[2]:
                return True
        return False

    def show(self):
        for i in self.grammar:
            print(i)




if __name__ == '__main__':
    agent = GrammerHandler()
