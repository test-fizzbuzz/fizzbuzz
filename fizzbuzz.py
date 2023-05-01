def fizzbuzz(num:int):
    for i in range(1, num+1):
        if i % 3 == 0:
            print("fizz")
        else:
            print(num)


if __name__=="__main__":
    fizzbuzz(15)
