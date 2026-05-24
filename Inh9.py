class First:
    def a(self):
        print("inside method a")
    
    def b(self):
        print("Inside method b")

class Second (First):
    def c(self):
        print("Inside method c")

if __name__ == "__main__":
    obj = Second()
    r= obj
    r.a()
    r.b()
    r.c()
