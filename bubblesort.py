def bubblesort(liste):
    for i in range(0, len(liste)-1):
        swapped = False
        for j in range(0, len(liste)-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                swapped = True
        if swapped:
            break
    return liste

unsortiert = [100, 2, 4, 12, 1]
sortiert = bubblesort(unsortiert)
print(sortiert)
