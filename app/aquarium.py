import threading
import random
import time
from queue import Queue
from .models import Fish

class FishProcess(threading.Thread):
    def __init__(self, fish_id, fish):
        super().__init__()
        self.fish_id = fish_id
        self.fish = fish

    def run(self):
        while self.fish.lifespan > 0:
            print(f"Fish {self.fish_id} ({self.fish.gender}) is swimming. Lifespan: {self.fish.lifespan}")
            time.sleep(random.uniform(0.5, 2))
            self.fish.lifespan -= 1
        print(f"Fish {self.fish_id} ({self.fish.gender}) has died.")

class BreedingProcess(threading.Thread):
    def __init__(self, male_queue, female_queue, offspring_queue):
        super().__init__()
        self.male_queue = male_queue
        self.female_queue = female_queue
        self.offspring_queue = offspring_queue

    def run(self):
        while True:
            male_fish = self.male_queue.get()
            female_fish = self.female_queue.get()
            
            offspring_gender = random.choice(['male', 'female'])
            offspring_lifespan = random.randint(5, 20)
            offspring = Fish(offspring_gender, offspring_lifespan)
            
            self.offspring_queue.put(offspring)

            self.male_queue.task_done()
            self.female_queue.task_done()

class Aquarium:
    def __init__(self):
        self.male_queue = Queue()
        self.female_queue = Queue()
        self.offspring_queue = Queue()

    def populate_aquarium(self):
        male_fish_count = random.randint(1, 10)
        female_fish_count = random.randint(1, 10)

        for i in range(male_fish_count):
            lifespan = random.randint(5, 20)
            male_fish = Fish('male', lifespan)
            self.male_queue.put(male_fish)

        for i in range(female_fish_count):
            lifespan = random.randint(5, 20)
            female_fish = Fish('female', lifespan)
            self.female_queue.put(female_fish)

    def start_simulation(self):
        breeding_thread = BreedingProcess(self.male_queue, self.female_queue, self.offspring_queue)
        breeding_thread.start()

        fish_threads = []
        for i in range(self.male_queue.qsize() + self.female_queue.qsize()):
            fish = self.offspring_queue.get() if i >= self.male_queue.qsize() else self.male_queue.get()
            fish_thread = FishProcess(i + 1, fish)
            fish_thread.start()
            fish_threads.append(fish_thread)

        for thread in fish_threads:
            thread.join()

        self.male_queue.join()
        self.female_queue.join()
        self.offspring_queue.join()
