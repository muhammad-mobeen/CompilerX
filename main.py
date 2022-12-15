from collections import deque
# the_stack = deque()

class GrammerHandler:
    def __init__(self):
        self.grammar = [
            ('S', 'AA'),
            ('A', 'aA|b')
            ]

    def driver(self):
        if not self.check_left_reccursion():
            print("No left Reccursion. You are good to go!")

    def check_left_reccursion(self):
        '''Checks for any left reccursion in the grammar. Returns bool()'''
        for r in self.grammar:
            if r[0] == self.getFirst(r):
                return True
        return False

    def getFirst(self, rule):
        '''Returns the list of Firsts on a given rule'''
        firsts = [rule[1][0]]
        for i,item in enumerate(rule[1]):
            if item == '|':
                firsts.append(rule[1][i])
        return firsts



if __name__ == '__main__':
    pass