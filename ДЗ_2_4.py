def sum_of_elements(counts, number=1, summary=0):
    if counts == 0:
        print(summary)
        return
    summary += number
    number = number/2*(-1)
    counts -= 1
    sum_of_elements(counts, number, summary)


sum_of_elements(3)
