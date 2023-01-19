def get_shop_list_by_dishes(dishes, person_count):
    needed = {i: cook_book[i] for i in dishes}
    res = {}
    for v in needed.values():
        for j in v:
            if j["ingredient_name"] in res:
                res[j["ingredient_name"]]["quantity"] +=  int(j["quantity"])*person_count
            else:
                res[j["ingredient_name"]] = {"measure": j["measure"], "quantity": int(j["quantity"])*person_count}
    return res

cook_book = {}
with open("recipes.txt", "rt", encoding = "utf-8") as file:
    for l in file:
        dishes = l.rstrip()
        amount = int(file.readline())
        ingredient_list = []
        for i in range(amount):
            row = file.readline().rstrip()
            ingredient_name, quantity, measure = row.split(" | ")
            ingredient_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure" : measure})
        file.readline()
        cook_book[dishes] = ingredient_list


print(get_shop_list_by_dishes(["Фахитос", 'Омлет'], 2))