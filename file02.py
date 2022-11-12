def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x = 0
    for i in data.split():
        x += 1
    return data

# Read data from file
print(main(open('txt_file/data02.txt').readlines()))