import math

def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        math.nan: "Garlic",
        "0": "Zero",
        '': "Empty",
        False: "Fake"
    }
    object_type = type(object)
    input_type = type_names.get(object, "Type not found")
    # print(object_type)
    if (input_type != "Type not found"):
        print(input_type + ":", object, object_type)
    elif (object_type == float):
        print(type_names[math.nan] + ":", object, object_type)
    else:
        print(input_type)
    return 1