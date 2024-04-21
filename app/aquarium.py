import random

from .models import Aquarium, Fish


def generate_random_fish(aquarium):
    x = random.randint(0, aquarium.width - 1)
    y = random.randint(0, aquarium.height - 1)
    gender = random.choice(["male", "femlae"])
    lifespan = random.randint(10, 30)
    return Fish.objects.create(aquarium=aquarium, x_position=x, y_position=y, gender=gender, lifespan=lifespan)

def move_fish(fish):
    aquarium = fish.aquarium
    possible_moves = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]
    movement = random.choice(possible_moves)
    new_x = (fish.x_position + movement[0]) % aquarium.width
    new_y = (fish.y_position + movement[1]) % aquarium.height
    fish.x_position = new_x
    fish.y_position = new_y
    fish.save()
    return f"{fish.gender} fish moved {abs(movement[0])} cells {'right' if movement[0] > 0 else 'left'} and {abs(movement[1])} cells {'down' if movement[1] > 0 else 'up'}"

def reproduce(fish1, fish2, existing_fishes):
    if fish1.gender != fish2.gender:
        if fish1.x_position == fish2.x_position and fish1.y_position == fish2.y_position:
            offspring_gender = random.choice(['male', 'female'])
            offspring_lifespan = random.randint(10, 30)  # Example lifespan range (in seconds)
            offspring = Fish.objects.create(aquarium=fish1.aquarium, x_position=fish1.x_position, y_position=fish1.y_position, gender=offspring_gender, lifespan=offspring_lifespan)
            for existing_fish in existing_fishes:
                if offspring.x_position == existing_fish.x_position and offspring.y_position == existing_fish.y_position:
                    if (offspring.gender == existing_fish.gender) and (offspring.id != existing_fish.id):
                        offspring.delete()
                        return None
            return f"Reproduction: Male fish and Female fish produced a {offspring.gender} offspring at position ({fish1.x_position}, {fish1.y_position})"
        else:
            return None
    else:
        return None
