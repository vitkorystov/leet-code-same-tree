from collections import defaultdict

# Given tickets with cities pair, needs create full route:
# [("Belgrade", "Moscow"), ("Erevan", "Tokyo"), ("Tokyo", "Baku"), ("Moscow", "Erevan")]
# -> ["Belgrade", "Moscow", "Erevan", "Tokyo", "Baku"]


def solution(ticket_list: list[tuple[str]]):
    d = defaultdict(set)
    for ticket in ticket_list:
        d[ticket[0]].add(ticket[1])
        d[ticket[1]].add(ticket[0])

    for k, v in d.items():
        if len(v) == 1:
            start_point = k
            break
    else:
        raise

    res = [start_point]
    tickets_number = len(ticket_list)
    for i in range(tickets_number):
        next_point_list = list(d[start_point])
        if len(next_point_list) == 1:
            next_point = next_point_list[0]
            res.append(next_point)
        else:
            for city in next_point_list:
                if city not in res:
                    next_point = city
                    res.append(next_point)
                    break
            else:
                raise
        start_point = next_point
    return res


print(solution([("Belgrade", "Moscow"), ("Erevan", "Tokyo"), ("Tokyo", "Baku"), ("Moscow", "Erevan")]))
