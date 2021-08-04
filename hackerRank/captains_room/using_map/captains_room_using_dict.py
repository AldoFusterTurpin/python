# ALDO FUSTER TURPIN

def create_rooms_count_map(room_numbers):
    rooms_count_map = dict()

    for room in room_numbers:
        if room in rooms_count_map:
            count = rooms_count_map[room]
            rooms_count_map[room] = count + 1
        else:
            rooms_count_map[room] = 1
    return rooms_count_map

# captain's room should appear just once in 'rooms_count_map' because he is alone in his room


def find_unique_room(rooms_count_map):
    for room_number, count in rooms_count_map.items():
        if count == 1:
            return room_number

    # Not found. In this context impossible due to exercise statement
    return -1


def find_captain_room(room_numbers: list[int]) -> int:
    rooms_count_map = create_rooms_count_map(room_numbers)
    return find_unique_room(rooms_count_map)


def main():
    K = int(input())
    room_numbers = input().split()
    room_numbers = [int(x) for x in room_numbers]

    captain_room = find_captain_room(room_numbers)
    print(captain_room)


if __name__ == "__main__":
    main()
