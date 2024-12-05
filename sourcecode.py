import os

def birthdayCakeCandles(candles):
    maxi = max(candles)
    count = candles.count(maxi)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')
    fptr.close()
