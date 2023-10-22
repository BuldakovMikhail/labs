from columns_ids import FETCH_COMPLETE, SYS_CNT


def place_fetch(data):
    res = []

    line = 1

    for i in range(1, len(data)):
        if data[i][FETCH_COMPLETE]:
            res.append((data[i - 1][SYS_CNT], line))

        line += 1

    return res
