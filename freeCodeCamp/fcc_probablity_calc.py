import random
import copy



class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)
    

    def draw(self, num):
        all_removed = []
        if(num > len(self.contents)):
            return self.contents


        for i in range(num):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        expected_copy = copy.deepcopy(expected_balls)
        colors_gotten = copy_hat.draw(num_balls_drawn)

        for color in colors_gotten:
            if color in expected_copy:
                expected_copy[color] -= 1 

        if(all(x <= 0 for x in expected_copy.values())):
            m += 1

    return m / num_experiments





hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.draw(3))

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)