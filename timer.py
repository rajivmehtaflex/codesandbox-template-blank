import timeit

def timer(number,repeat):
    def wrapper(func):
        runs=timeit.repeat(func,repeat=repeat,number=number)
        print(sum(runs)/len(runs))

    return wrapper