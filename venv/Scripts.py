# вид бафов: (вид)(цель)
# ds - божественный щит | hp+/-(число) | st+/-(число) - +/- (число) сила | bc - боевой клич|
# ch - рывок | tt - провокация |
# по цели: a - все | r(число) - рандомные | s - сама карта | c(число) - выбрать карты
def select(prompt,b,p=()): #приглашение, ограничение на число, список подоходящих строк
    f=True              #только для строк прописать b=0
    while f:
        try:
            n=input(prompt)
            if n not in p:
                n=int(n)
                if -1<n<b:
                    f=False
                else:
                    raise ValueError
            else:
                f=False
        except ValueError:
            print("Input Error. Try it again.")
    return n
def update_queue(inp):
    f=open("queue.txt")