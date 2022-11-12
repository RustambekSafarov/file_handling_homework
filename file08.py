def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l = 0
    for i in data:
        if i.isdigit():
            if int(i) > l:
                l = int(i)

print(main(open('txt_file/data08.txt').read()))
