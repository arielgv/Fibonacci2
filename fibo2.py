import time
#the module time allows to make a delay in the time between numbers are displayed
def fibosec():
    n1 = 0
    n2 = 1
    counter = 0

    if counter == 0 :
        counter = counter + 1
        yield n1
        time.sleep(0.3)
    if counter == 1 :
        yield n2
        time.sleep(0.3)
        counter=counter+1
    while True:
        aux = n1 + n2
        n1 = n2
        n2 = aux
        time.sleep(0.3)
        yield aux

if __name__ == "__main__":
    fibo2=fibosec()
    for element in fibo2:
        print(element)
        time.sleep(0.3)


