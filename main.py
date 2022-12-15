from collections import deque
# the_stack = deque()

class GrammerHandler:
    def __init__(self):
        self.grammar = [
            ['S', 'AA'],
            ['A', 'aA|B|c'],
            ['B', 'b']
            ]
        self.driver()

    def driver(self):
        '''Driver function to lead the wave!...'''
        self.calculate_firsts()
        print(self.grammar)

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
            for x,r in enumerate(self.grammar):
                
                for y,s in enumerate(rule[1]):
                    if s == '|':
                        follows.append(rule[1][y+1])
            self.grammar[i].append(follows)

    def check_left_reccursion(self):
        '''Checks for any left reccursion in the grammar. Returns bool()'''
        for i,r in enumerate(self.grammar):
            if r[0] in r[2]:
                return True
        return False




if __name__ == '__main__':
    agent = GrammerHandler()
