
# Monty Hall: 3 doors. 1 car. 2 goats.
# Game host knows where the car is (i.e. he always
# chooses a goat-door

# Simulate 1000  games using three doors for each
# strategy (swap / not swap) and show the results in
# such a way as to make it easy to compare the effects
# of each strategy.

from random import randrange, choice

class montyhall(object):
    
    def setup(self, num_doors):
        doors = [False] * num_doors
        car_index = randrange(len(doors))
        doors[car_index] = True
        return doors

    def choosers_knowing_host(self, door_list):

        #5, car is at 6
        guest_index = randrange(len(door_list))

        # [0, 1, 2, 3, 4, 7, 8, 9]
        potential_host_doors = [i for i, door in enumerate(door_list) if door == False and i != guest_index]

        host_index = choice(potential_host_doors)

        return guest_index, host_index
    
    def choosers_blind_host(self, door_list):

        #5, car is at 6
        guest_index = randrange(len(door_list))

        # [0, 1, 2, 3, 4, 6, 7, 8, 9]
        potential_host_doors = [i for i, door in enumerate(door_list) if i != guest_index]

        host_index = choice(potential_host_doors)

        return guest_index, host_index

    def jumper_guest(self, door_list, guest_index, host_index):
        leftover_doors = [i for i, door in enumerate(door_list) if i != guest_index and i != host_index]
        jumper_index = choice(leftover_doors)
        return jumper_index

stayer_guest_knowing_host_wins = 0
jumper_guest_knowing_host_wins = 0
i = 0
while i < 1000:
    door_list = montyhall().setup(3)
    guest_index, host_index = montyhall().choosers_knowing_host(door_list)

    #version of guest that stayed
    stayer_guest_knowing_host_wins += door_list[guest_index]

    #version of guest that jumped
    jumper_index = montyhall().jumper_guest(door_list, guest_index, host_index)
    jumper_guest_knowing_host_wins += door_list[jumper_index]

    i += 1

stayer_guest_blind_host_wins = 0
jumper_guest_blind_host_wins = 0

i = 0
while i < 1000:

    door_list = montyhall().setup(3)
    guest_index, host_index = montyhall().choosers_blind_host(door_list)

    #version of guest that stayed
    stayer_guest_blind_host_wins += door_list[guest_index]

    #version of guest that jumped
    jumper_index = montyhall().jumper_guest(door_list, guest_index, host_index)
    jumper_guest_blind_host_wins += door_list[jumper_index]

    i += 1

print("Results (1000 simulations, 3 doors):")
print(f"If the host knows where the car is, staying at the original door wins you the car {stayer_guest_knowing_host_wins} times. Swapping to another door / the leftover door wins you the car {jumper_guest_knowing_host_wins} times. The latter strategy (counter-intuitively) doubles our chances of winning the car because the host DID NOT MAKE AN IGNORANT CHOICE. S/he will never anti-climatically reveal the car for us.")

print(f"OTOH, if the host DOESN'T know where the car is (weird), staying wins you the car {stayer_guest_blind_host_wins} times. And swapping to another door / the leftover door wins you the car {jumper_guest_blind_host_wins} times. It's only in this scenario (a weird one, since 1/3 of the time the game host picks the winning door with the car and ruins the potential tension of the show), swapping or staying doesn't matter so much.")
