import ast

class SyntaxTree():
    def __init__(self):
        self.expression = None

    def generate_syntax_tree(self):
        self.tree = ast.parse(self.expression)

    def show(self):  
        print(f"{self.tree.__class__.__name__}: {ast.dump(self.tree,indent = 3)}")
        for child in ast.iter_child_nodes(self.tree):
            child
        

if __name__ == 'main':
    tree_obj = SyntaxTree()
    tree_obj.expression = "a+(b*c)"
    tree_obj.generate_syntax_tree()
    tree_obj.show()