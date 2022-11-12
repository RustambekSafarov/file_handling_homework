def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x = data.read()
    y = 0
    for i in x:
        y +=1 
    # for i in data.split():
        
    return y

# Read data from file
print(main(open('txt_file/data02.txt','r+')))
