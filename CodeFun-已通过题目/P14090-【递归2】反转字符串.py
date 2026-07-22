def str_reverse(tar):
    if len(tar)==1 or tar is None:
        return tar
    new_tar=list(tar)
    new_tar = new_tar[1:] + [new_tar[0]]
    new_tar=''.join(new_tar)
    return str_reverse(new_tar[:-1])+new_tar[-1]

if __name__=="__main__":
    s=input()
    print(str_reverse(s))
