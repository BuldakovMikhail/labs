from columns_ids import (
    FETCH_COMPLETE,
    SYS_CNT,
    UNIT_ISSUE0_NEW_REQ,
    UNIT_WB0_DONE,
    UNIT_WB0_ID,
)


def place_fetch(data):
    res = []

    line = 1

    for i in range(1, len(data)):
        if data[i][FETCH_COMPLETE]:
            res.append((data[i - 1][SYS_CNT], line))

        line += 1

    return res


def place_alu(data):
    res = []
    line = 0
    prev_id = data[0][UNIT_WB0_ID]

    for i in range(0, len(data)):
        if prev_id != data[i][UNIT_WB0_ID]:
            prev_id = data[i][UNIT_WB0_ID]
            line += 1

        if data[i][UNIT_WB0_DONE] and data[i][UNIT_ISSUE0_NEW_REQ]:
            res.append((data[i][SYS_CNT], line))

    return res
