#cinema
typeOfProjection = input()
rowsNum = int(input())
columnsNum = int(input())
cinemaCapacity = rowsNum * columnsNum
totalTicketRevenue = 0

if typeOfProjection == "Premiere":
    totalTicketRevenue = cinemaCapacity * 12.00
    print(f"{totalTicketRevenue:.2f} USD")
elif typeOfProjection == "Normal":
    totalTicketRevenue = cinemaCapacity * 7.50
    print(f"{totalTicketRevenue:.2f} USD")
elif typeOfProjection == "Discount":
    totalTicketRevenue = cinemaCapacity * 5.00
    print(f"{totalTicketRevenue:.2f} USD")

