import math

#seats = (("Liberal", 11, 7404), ("Yukon Party", 6, 6272), ("NDP", 2, 4928))
def GallagherIndex(seats):
    totalVotes = 0
    totalSeats = 0
    for party in seats:
        totalVotes += party[2]
        totalSeats += party[1]
    print(totalVotes, totalSeats)
    difList = list()
    for party in seats:
        print(party)
        votePer = (party[2]/totalVotes)*100
        seatPer = (party[1]/totalSeats)*100
        print(votePer, seatPer)
        dif = abs(votePer-seatPer)
        difSquared = dif**2
        difList.append(difSquared)
    sumDif = 0.0
    print(difList)
    for dif in difList:
        sumDif += dif
    halfSumDif = sumDif/2.0
    sqrtHalfSumDif = math.sqrt(halfSumDif)
    return sqrtHalfSumDif


if __name__ == "__main__":
    seats = (("Liberal", 184, 6943276), ("Conservatives", 99, 5613614), ("NDP", 44, 3470350), ("BQ", 10, 821144), ("Green", 1, 602944))
    print(GallagherIndex(seats))