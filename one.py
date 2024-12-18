def main():
    # get input
    with open("input.txt") as file:
        # separate into arrays
        one = []
        two = []

        for line in file.readlines():
            [i, j] = line.split()
            one.append(int(i))
            two.append(int(j))

        # sort arrays
        one.sort()
        two.sort()

        # get distances
        output_one = 0
        for i in range(len(one)):
            output_one += abs(one[i] - two[i])

        print(output_one)

        output_two = 0
        for i in one:
            output_two += (i * two.count(i))

        print(output_two)


if __name__ == "__main__": main()