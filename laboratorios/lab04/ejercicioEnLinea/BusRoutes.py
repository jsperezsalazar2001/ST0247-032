# This algorithm calculates the minimum number of hours that a company have to pay because of extra hours


def busRoutes(filename):
    results = []
    try:
        file = open(filename, "r", encoding='utf-8')
        line = file.readline()
        while line != "":
            line = line.split(" ")
            if len(line) == 3 and (line[0] != '0' and line[1] != '0' and line[2] != '0'):
                parameters = line
                drivers = file.readline().split(" ")
                routes = file.readline().split(" ")
                drivers.sort(key=lambda x: x, reverse=True)
                routes.sort(key=lambda x: x)

                for i in range(int(parameters[0])):
                    drivers[i] = int(drivers[i]) + int(routes[i])
                hours = 0
                for i in range(len(drivers)):
                    if drivers[i] > int(parameters[1]):
                        hours += drivers[i] - int(parameters[1])

                results.append(hours * int(parameters[2]))
            line = file.readline()
        file.close()
        print(results)
    except:
        print("File not found")


busRoutes("test1.txt")
