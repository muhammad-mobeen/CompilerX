import re

class LexicalAnalyzer:
    def __init__(self):
        self.expression = None
        self.identifier_pattern = "[a-zA-Z]"
        self.operator_pattern = "(\+|-|\*|\/|=|>|<|\^)+"
        self.constant_pattern = "\d+"
        self.punctuator_pattern = "(\(|\)|\[|\]|\{|\})"
        self.special_char_pattern = "(\$|&|\||%|!)"
        self.lexical_analysis = {}

    def identify(self):
        self.lexical_analysis = {
            "Identifiers": re.findall(self.identifier_pattern, self.expression),
            "Constants": re.findall(self.constant_pattern, self.expression),
            "Operators": re.findall(self.operator_pattern, self.expression),
            "Punctuators": re.findall(self.punctuator_pattern, self.expression),
            "Special": re.findall(self.special_char_pattern, self.expression)
        }
    
    def show(self):
        for key, value in self.lexical_analysis.items():
            print(key, '->', value)


if __name__ == '__main__':
    analyze = LexicalAnalyzer()
    analyze.expression = "a+(b*c)"
    # analyze.expression = "39+(50*26)"
    analyze.identify()
    analyze.show()