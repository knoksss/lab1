class SymbolError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return 'SymbolError, {0} '.format(self.message)
    
class BracketError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return 'BracketError, {0} '.format(self.message)
    
class BracketBalanceError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return 'BracketBalanceError, {0} '.format(self.message)
    
class CorrectionError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return 'CorrectionError, {0} '.format(self.message)