def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }
    object_type = type(object)
    input_type = type_names.get(object_type, "Type not found")
    if (object_type == str):
        print(object, "is in the kitchen", object_type)
    elif (input_type != "Type not found"):
        print(input_type, ":", object_type)
    else:
        print(input_type)

    return 42