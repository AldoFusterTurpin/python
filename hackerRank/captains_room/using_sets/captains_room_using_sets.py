# ALDO FUSTER TURPIN

def find_captain_room(room_numbers: list[int]) -> int:
    # visited_rooms will contain all rooms at the end
    visited_rooms = set()

    rooms_appeared_more_than_once = set()

    for current_room in room_numbers:
        if current_room in visited_rooms:
            rooms_appeared_more_than_once.add(current_room)
        else:
            visited_rooms.add(current_room)

    difference = visited_rooms - rooms_appeared_more_than_once
    difference_list = list(difference)

    result = difference_list[0]
    return result


def main():
    K = int(input())
    room_numbers = input().split()
    room_numbers = [int(x) for x in room_numbers]

    captain_room = find_captain_room(room_numbers)
    print(captain_room)


if __name__ == "__main__":
    main()

# 1 1 1 2 3 3 3 3
# visited = 1, 2, 3
# rooms_appeared_more_than_once = 1, 3
# result should be 2

