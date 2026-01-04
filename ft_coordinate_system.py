import sys
import math
def calculate_distance(x1, y1,z1, x2, y2,z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def parse_coordinates(coordinates):
    numbers = coordinates.split(",")
    nums = ()
    for i in numbers:
        try:
            i = int(i)
        except ValueError as e:
            print(f'Parsing invalid coordinates: "{coordinates}"')
            print(f"Error parsing coordinates:",e)
            print(f"Error details- Type: {e.__class__.__name__},"
                  f" Args: ({e.args})")
            return None
        else:
            nums += (i,)
    print(f'Parsed coordinates: "{coordinates}"')
    print("Parsed position:",nums)
    print(f"distance between (0,0,0) and parsed position:"
          f" {calculate_distance(0,0,0,*nums):.2f}")
    return nums


# parse_coordinates("3,4,j")

print("=== Game Coordinate System ===")

position = (10, 20, 5)
orign = (0,0,0)
print("Position created:", position)
print(f"Distance from  between {orign} and {position}:"
      f" { calculate_distance(*orign,*position):.2f}")
print()
if len(sys.argv) == 1:
    print("No coordinates provided!")

else:
    coordinates = []
    for i in sys.argv[1:]:
        parsed = parse_coordinates(i)
        print()
        if parsed is not None:
            coordinates.append(parsed)
    print()
    print("Unpacking demonstration:")
    for cord in coordinates:
        print(f"Player at x={cord[0]}, y={cord[1]}, z={cord[2]}")
        print(f"Coordinates: X={cord[0]}, Y={cord[1]}, Z={cord[2]}")