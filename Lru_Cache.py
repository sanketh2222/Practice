from functools import lru_cache
val=int(input("Cached value"))

@lru_cache(maxsize=1)
def some_work(n):
    print("doing somework")
    time.sleep(n)
    print("grand success")
    return n

try except and finally and else:
if __name__ == '__main__':

    some_work(3)
    print("second")
    print(some_work(3))
    print("third")
    print(some_work(3))
    print(some_work(3))