from .aquarium import generate_random_fish, move_fish, reproduce
from .models import Aquarium, Fish


def simulate_aquarium():
    aquarium = Aquarium.objects.first()
    if aquarium is None:
        return "No aquarium found. Please create an aquarium first."
    elif Fish.objects.count() < aquarium.height * aquarium.width:
        new_fish = generate_random_fish(aquarium)
        movements = []
        for fish in Fish.objects.all():
            movement = move_fish(fish)
            movements.append(movement)
        existing_fishes = list(Fish.objects.all())
        for fish1 in existing_fishes:
            for fish2 in existing_fishes:
                if fish1 != fish2:
                    reproduction_message = reproduce(fish1, fish2, existing_fishes)
                    if reproduction_message is not None:
                        movements.append(reproduction_message)
        for fish in Fish.objects.all():
            fish.lifespan -= 1
            if fish.lifespan <= 0:
                fish.delete()
                movements.append(f"{fish.gender} fish died at position ({fish.x_position}, {fish.y_position})")
        for movement in movements:
            print(movement)
        return "New fish created and movements logged"
    else:
        return "Aquarium is full"
