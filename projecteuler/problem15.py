def problem15(size):
    def middle(previous=[1, 2, 1]):
        if len(previous) == size + 1:
            return previous
        temp = list(previous)
        temp.insert(0, 0)
        temp.append(0)
        current = [1] * (len(previous) + 1)
        for i in xrange(len(temp) - 1):
            current[i] = temp[i] + temp[i + 1]
        return middle(current)
    return sum([x * x for x in middle()])
            
if __name__ == '__main__':
    print problem15(20)
