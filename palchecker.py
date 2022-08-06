#双端队列应用之“回文词”判定 回文词格式：abcba toot 上海自来水来着海上

from deque import Deque

def palchecker(aSting):
    chardeque = Deque()

    for ch in aSting:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("上海自来水来自海上"))
print(palchecker("radar"))