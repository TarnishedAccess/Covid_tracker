import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page_URL = "https://www.worldometers.info/coronavirus/country/algeria/"
page = requests.get(page_URL)

#This is the issue for long bootup. Optimize this#
soup = BeautifulSoup(page.content, "html.parser")
list2 = soup.find_all(class_="col-md-12")
daily = list2[1]
script = str(daily.find("script"))
script_list = script.split("series")
data_list = script_list[2].split("name")
line = data_list[1].splitlines()
satanizer = line[4].lstrip()
bruh = satanizer.split("data:")
CBT = bruh[1].split("}")
cases_list = CBT[0].lstrip()
striptation = cases_list.split("[")
striptation_2 = striptation[1].split("]")
case = striptation_2[0].split(",")

list3 = soup.find_all("script")
x = str(list3[25])
y = x.split("series")
z = str(y[2]).split("[")
deaths = str(z[2]).split("]")
deaths = deaths[0]
deaths_list = deaths.split(",")
#######

print("days since pandemic start:", len(case))
print("last reported daily cases:", case[len(case)-1])

exit_mark = False
while exit_mark == False:
    query = input("\nN:quit | D:graph(daily) | T:graph(total) | L:list | else, num of cases of day(n)\n")
    if query.lower() == "n":
        exit_mark = True
        exit
    elif query.lower() == "l":
        total = 26
        total_deaths = 2
        for i in range(27, len(case)-50):
            total = total + int(case[i])
            total_deaths = total_deaths + int(deaths_list[i])
        maximum = 0
        for cbt in range(27, len(case)):
            if int(case[cbt]) > int(maximum):
                maximum = case[cbt]
                maximum_day = cbt
        for y in range(len(case)-50, len(case)):
            difference = int(case[y]) - int(case[y-1])
            total = total + int(case[y])
            total_deaths = total_deaths + int(deaths_list[y])
            print("day: ", y+1, " |infected: ", case[y], "|difference: ", difference, "|total: ", total, "|deaths: ", deaths_list[y], "|total deaths: ", total_deaths)
        infection_percent = (total*100)/43000000
        print("\nPeak: Day", maximum_day+1, "with", maximum, "infected")
        print("Percent of populace infected:", round(infection_percent, 2), "% (presumably lol)")
    elif query.lower() == "d":
        xaxis = []
        yaxis = []
        for y in range(27, len(case)):
            yaxis.append(int(case[y]))
            xaxis.append(int(y+1))
        plt.plot(xaxis, yaxis)
        plt.xlabel("days")
        plt.ylabel("infections per day")
        plt.title("'Rona virus stats in algeria")
        plt.show()
    elif query.lower() == "t":
        xaxis = []
        yaxis = []
        total = 0
        for y in range(27, len(case)):
            xaxis.append(int(y+1))
            total = total + int(case[y])
            yaxis.append(int(total))
        plt.plot(xaxis, yaxis)
        plt.xlabel("days")
        plt.ylabel("infections total")
        plt.title("'Rona virus stats in algeria")
        plt.show()        
    else:
        day = int(query)
        if case[day-1] == 'null':
            print("0 cases")
        else:
            print(case[day-1], "cases")




# 1032
