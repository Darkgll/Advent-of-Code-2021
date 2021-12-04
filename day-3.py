import collections

# I've made a file report.txt with just copied data of all reports
with open("report.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

test_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


# Solution for Part 1
def multiplay_binary_results(r_list):
    new_list = []
    new_line = ""
    gamma_rate_list = ""
    epsilon_rate_list = ""
    for n_index in range(len(r_list[0])):
        for line in r_list:
            new_line += line[n_index]
        new_list.append(new_line)
        new_line = ""
    for line in new_list:
        current_most_common = str(collections.Counter(line).most_common(1)[0][0])
        gamma_rate_list += current_most_common
        if current_most_common == "1":
            epsilon_rate_list += "0"
        else:
            epsilon_rate_list += "1"
    gamma_rate_list = int(gamma_rate_list, 2)
    epsilon_rate_list = int(epsilon_rate_list, 2)

    return gamma_rate_list * epsilon_rate_list


# Solution for Part 2
def multiplay_results_ratings(r_list):
    new_list = r_list
    ones = []
    zeros = []
    oxygen_generator_rating = ""
    CO2_scrubber_rating = ""
    # for oxyget generator rating
    if len(new_list) != 1:
        for n_index in range(len(new_list[0])):
            for line in new_list:
                if str(line[n_index]) == "1":
                    ones.append(line)
                elif str(line[n_index]) == "0":
                    zeros.append(line)
            if len(ones) >= len(zeros):
                new_list = ones
            elif len(zeros) > len(ones):
                new_list = zeros
            ones = []
            zeros = []
            if len(new_list) == 1:
                oxygen_generator_rating = str(new_list[0])
    # for CO2 scrubber rating
    new_list = r_list
    if len(new_list) != 1:
        for n_index in range(len(new_list[0])):
            for line in new_list:
                if str(line[n_index]) == "1":
                    ones.append(line)
                elif str(line[n_index]) == "0":
                    zeros.append(line)
            if len(zeros) <= len(ones):
                new_list = zeros
            elif len(ones) < len(zeros):
                new_list = ones
            ones = []
            zeros = []
            if len(new_list) == 1:
                CO2_scrubber_rating = str(new_list[0])
    oxygen_generator_rating = int(oxygen_generator_rating, 2)
    CO2_scrubber_rating = int(CO2_scrubber_rating, 2)
    return oxygen_generator_rating * CO2_scrubber_rating


if __name__ == '__main__':
    print(multiplay_results_ratings(lines))
