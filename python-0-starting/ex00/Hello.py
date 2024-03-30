ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

## --------list---------
ft_list[1] = "World!"


## --------tuple---------
# tmp = list(ft_tuple)
# tmp[1] = "France!"
# ft_tuple_1 = tuple(tmp)
ft_tuple = (ft_tuple[0], "France!")

## --------set---------
ft_set.remove("tutu!")
ft_set.add("Paris!")


## --------dict---------
ft_dict["Hello"] = "42Paris!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)