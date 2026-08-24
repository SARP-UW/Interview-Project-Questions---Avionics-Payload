import random
from collections import deque


def sensor(start=100.0):
    signal = start
    velocity = 0.0

    while True:
        velocity += random.gauss(0, 0.15)
        velocity *= 0.95 
        velocity = max(-1.5, min(1.5, velocity))

        signal += velocity

        noise = random.gauss(0, 0.75)

        yield signal + noise


def smooth(x:list):
    # TODO: implement your smoothing method
    return x[0]


def main():
    numbers = sensor()

    data_history = deque()
    history_size = 5

    for i in range(1000):
        data_history.append(next(numbers))
        if(len(data_history) > history_size):
            data_history.popleft()

        print(smooth(list(data_history)))

if __name__ == "__main__":
    main()