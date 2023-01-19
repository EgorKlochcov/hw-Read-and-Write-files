with open("file1.txt", "rt", encoding="utf-8") as f_1:
    res_1 = f_1.readlines()
with open("file2.txt", "rt", encoding="utf-8") as f_2:
    res_2 = f_2.readlines()

with open("ressult.txt", "x") as f_3:
    if len(res_1) >= len(res_2):
        f_3.writelines(["file1.txt\n", str(len(res_1))+"\n"])
        f_3.writelines(res_1)
        f_3.writelines(["\n","file2.txt\n", str(len(res_2))+"\n"])
        f_3.writelines(res_2)
    else:
        f_3.writelines(["file2.txt\n", str(len(res_2))+"\n"])
        f_3.writelines(res_2)
        f_3.writelines(["\n","file1.txt\n", str(len(res_1))+"\n"])
        f_3.writelines(res_1)