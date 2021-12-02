# I've made a file report.txt with just copied data of all reports
with open("report.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

test_list = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


# Solution for Part 1
def multiplay_location_data(r_list):
    depth = 0
    horizontal_position = 0
    for line in r_list:
        if line.split()[0] == "forward":
            horizontal_position += int(line.split()[1])
        elif line.split()[0] == "down":
            depth += int(line.split()[1])
        elif line.split()[0] == "up":
            depth -= int(line.split()[1])
    return depth * horizontal_position


# Solution for Part 2
def multiplay_location_aim_data(r_list):
    aim = 0
    depth = 0
    horizontal_position = 0
    for line in r_list:
        if line.split()[0] == "forward":
            horizontal_position += int(line.split()[1])
            depth += (aim * int(line.split()[1]))
        elif line.split()[0] == "down":
            aim += int(line.split()[1])
        elif line.split()[0] == "up":
            aim -= int(line.split()[1])
    return depth * horizontal_position


if __name__ == '__main__':
    print(multiplay_location_aim_data(lines))
