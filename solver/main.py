# Столбики :  sys_cnt, fetch_complete, pc_id

from parser import parse_data
from solvers import place_fetch
from format_ouptut import output_to_excel


def main():
    data = parse_data()
    fetch = place_fetch(data)

    dic = {"F": fetch}
    output_to_excel(dic)


if __name__ == "__main__":
    main()
