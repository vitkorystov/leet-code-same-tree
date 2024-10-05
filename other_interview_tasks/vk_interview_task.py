
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

keys = list(original.keys())
while keys:
    key = keys[0]
    value = original.get(key)
    if not isinstance(value, dict):
        loop_result[key] = value
    else:
        nested_keys = value.keys()
        for k in nested_keys:
            new_key = f"{key}.{k}"
            original[new_key] = value.get(k)
            keys.append(new_key)
    del original[key]
    keys.remove(key)


assert loop_result == expected
