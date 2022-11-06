import threading
import time
import random


class FivePhilosophers(threading.Thread):
    still_eating = True

    def __init__(self, index, fork_left, fork_right):
        threading.Thread.__init__(self)
        self.index = index
        self.fork_left = fork_left
        self.fork_right = fork_right

    def run(self):
        while self.still_eating:
            time.sleep(random.randint(2, 10))
            print('Philosopher %s is thinking' % self.index)
            self.eat()

    def eating(self):
        print('Philosopher %s is eating' % self.index)
        time.sleep(random.randint(2, 10))
        print('Philosopher %s finishes eating' % self.index)

    def eat(self):
        fork_l = self.fork_left
        fork_r = self.fork_right
        while self.still_eating:
            fork_l.acquire()
            if fork_r.acquire(False):
                break
            fork_l.release()
            print(f'Philosopher %s swaps forks.' % self.index)
            fork_l, fork_r = fork_r, fork_l
        else:
            return
        self.eating()
        fork_r.release()
        fork_l.release()


if __name__ == '__main__':
    forks = [threading.Semaphore() for n in range(5)]
    philosophers = [FivePhilosophers(i, forks[i % 5], forks[(i+1) % 5]) for i in range(5)]

    FivePhilosophers.still_eating = True
    for p in philosophers:
        p.start()
    time.sleep(40)
    FivePhilosophers.still_eating = False
    print("Finish")

