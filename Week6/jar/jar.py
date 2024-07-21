import emoji

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return (emoji.emojize(":Cookie:") * self.size)

    def deposit(self, n):
        if(self.size + n > self.capacity):
            raise ValueError
        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self.capacity

    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Non-positive Capacity")
        self.capacity = capacity

    @property
    def size(self):
        return self.size

    def size(self,size):
        if size < 0:
            raise ValueError("Insuffiicent Cookies")
        if size > self.capacity:
            return ValueError("Overcapacity")
        self.size = size

def main():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    print(str(jar))

main()
