import time


def get_horses(callback):
    f = open("res/random horses.txt", "r")
    horse_ranks = f.read().splitlines()
    f.close()
    for i in range(len(horse_ranks)):
        callback(horse_ranks[i])
        time.sleep(0.1)

if __name__ == '__main__':
    print(get_horses(print))