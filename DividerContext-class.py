class DividerContext:

    def __init__(self, symbol):
        self.symbol = symbol

    def __enter__(self):
        print(10*self.symbol)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(10*self.symbol)


a = "#"
with DividerContext(a):
    print("Hallo")
