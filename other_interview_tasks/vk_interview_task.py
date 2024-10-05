
# Convert nested dict to flat dict:

original = {
    "squadName": "Super hero squad",
    "members": {
        "secretIdentity": "Dan Jukes",
        "info": {
            "name": "Molecule Man",
            "age": 29
        }
    }
}

expected = {
    "squadName": "Super hero squad",
    "members.secretIdentity": "Dan Jukes",
    "members.info.name": "Molecule Man",
    "members.info.age": 29,
}


# 1) Solution with recursion
result_dict_rec = dict()


def rec(d: dict, prefix: str | None = None):
    for k, v in d.items():
        new_key = k if prefix is None else f"{prefix}.{k}"
        if not isinstance(v, dict):
            result_dict_rec[new_key] = v
        else:
            rec(v, new_key)


rec(original)

assert result_dict_rec == expected


# 2) Solution with loop
loop_result = dict()

for key, value in original.items():
    if not isinstance(value, dict):
        loop_result[key] = value
    else:
        prefix = ''
        length_inner_dict = 0
        prefix_inner_dict = ''
        while value:
            k, v = value.popitem()
            if isinstance(v, dict):
                value.update(v)
                prefix = f'{key}.{k}'
                length_inner_dict = len(v)
                prefix_inner_dict = k

            else:
                if length_inner_dict > 0:
                    loop_result[f'{prefix}.{k}'] = v
                    length_inner_dict -= 1
                else:
                    loop_result[f'{prefix}.{k}'.replace(f'.{prefix_inner_dict}', '')] = v


assert loop_result == expected