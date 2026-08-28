



def generate_data():
    data = []
    steps = {1: 0}

    for i in range(1, 10000):
        x = i
        path = []
        while x not in steps:
            path.append(x)
            if x % 2 == 0:
                x //= 2
            else:
                x = x * 3 + 1

        count = steps[x]
        for value in reversed(path):
            count += 1
            steps[value] = count
        data.append(steps[i])

    return data



# The challenge. Play around with these numbers.
# Write some scripts to see if there are patterns
# Do some data analysis on it.  Do not look up the 
# sequence online.  Do not google the algorithm.

# The idea of the challenge is just to see how you 
# approach tricky data, and what methods you attempt

# Do not be concerned if you don't find much.  The methods
# are what matter much more than any solutions.
def main():
    data = generate_data()
    print(data)

if __name__ == "__main__":
    main()
        
