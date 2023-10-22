import pandas as pd


def output_to_xlsx(dictionary: dict(), excel=True, csv=False) -> None:
    """
    Необходимо передать словарь вида:
    {
        'Letter' : [(x1, y1), (x2, y2), ...], ....
    }
    По ключу в словаре хранится буква, которую необходимо вставить, по значению
    массив кортежей с координатами вставки. Координаты вставки: x - такт, y - номер строки, индексация с 1.
    """
    max_x = max([i[0] for _, v in dictionary.items() for i in v])
    max_y = max([i[1] for _, v in dictionary.items() for i in v])

    df = pd.DataFrame(index=range(1, max_y + 1), columns=range(1, max_x + 1))

    for key, value in dictionary.items():
        for t in value:
            df.loc[t[0], t[1]] = key

    if excel:
        df.to_excel("solution.xlsx")
    if csv:
        df.to_csv("solution.csv")


# test = {"X": [(i + 1, i + 1) for i in range(30)]}

# output_to_xlsx(test)
