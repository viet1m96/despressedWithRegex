def process(text):
    str_arr = text.split()
    res = []
    i = 0
    while i < len(str_arr):
        model = str_arr[i]
        while i < len(str_arr) and str_arr[i] == model:
            i += 1
        if i == len(str_arr):
            res.append(model)
        else:
            picked = 1
            if len(str_arr[i]) > len(model):
                for j in range(0, len(model)):
                    if str_arr[i][j] != model[j]:
                        picked = 0
                        break
                if str_arr[i][len(model)].isalpha(): picked = 0
                if picked == 1:
                    model = str_arr[i]
                    i += 1
            res.append(model)
    return res

