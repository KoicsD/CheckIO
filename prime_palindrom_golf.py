__author__ = 'KoicsD'


def golf(num):
    num += 1
    digs = [ord(d) - ord('0') for d in str(num)]
    while not ((True not in [num % i == 0 for i in range(2, num)]) and
               (False not in [(digs[i] == digs[-i-1]) for i in range(len(digs)//2)])):
        num += 1
        digs = [ord(d) - ord('0') for d in str(num)]
    return num
