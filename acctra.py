import json
from datetime import datetime

with open("operations.json", encoding="utf8") as f:
    operations = json.load(f)


def format_date(date):
    """
    Formats date into DD-MM-YYYY
    :param date:
    :return:
    """
    string_parse_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    string_format_time = datetime.strftime(string_parse_time, "%d-%m-%Y")
    return string_format_time


def hide_sensitive_number(number):
    """
    Hides banking number.
    :param number:
    :return:
    """
    split_all = number.split()

    if split_all[0] == "Счет":
        hidden_number = "XX" + split_all[1][-4:]
        return "Счет " + hidden_number

    else:
        split_number = [split_all[-1][i:i + 4] for i in range(0, 16, 4)]
        # for i in range(0 , 16, 4):
        #     split_number.append(split_all[-1][i:i + 4])

        split_all.pop(-1)

        hidden_number = split_number[0] + " " + split_number[1][0:2] + "XX XXXX" + " " + split_number[3]
        return " ".join(split_all) + " " + hidden_number


def return_last_5():
    """
    Prints last 5 "EXECUTED" bank transactions sorted by date.
    :return:
    """
    operations_sorted_by_date = sorted(operations, key=lambda sort_line: sort_line["date"], reverse=True)
    x = 0
    for line in operations_sorted_by_date:
        if line["state"] == "CANCELED":
            continue
        print(format_date(line['date']), line['description'])
        if 'from' in line:
            print(hide_sensitive_number(line['from']), " -> ", hide_sensitive_number(line['to']))
        else:
            print(hide_sensitive_number(line['to']))
        print(line['operationAmount']['amount'], line['operationAmount']['currency']['code'])  # 'name'
        print("---")
        x += 1
        if x == 5:
            break


return_last_5()
