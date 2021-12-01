# I've made a file report.txt with just copied data of all reports
with open("report.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# Solution for Part 1
def count_increases_part_1(r_list):
    counted_increases = 0
    for line in range(1, len(r_list)):
        if int(r_list[line]) > int(r_list[line-1]):
            counted_increases += 1
    return counted_increases


# Solution for Part 2
def count_increases_part_2(r_list):
    counted_increases = 0
    sum_list = []
    for number in range(len(r_list)):
        try:
            sum_list.append(int(r_list[number])+int(r_list[number+1])+int(r_list[number+2]))
        except IndexError:
            continue
    for line in range(1, len(sum_list)):
        if int(sum_list[line]) > int(sum_list[line-1]):
            counted_increases += 1
    return counted_increases


if __name__ == '__main__':
    print(count_increases_part_2(lines))
