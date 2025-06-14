import os 

def CountFileContent():
    fobj = open("Data.txt","r")
    content = fobj.read()
    fobj.close()
    
    lines = content.splitlines()
    num_lines = len(lines)

    words = content.split()
    num_words = len(words)

    num_chars = len(content)

    print("Number of lines",num_lines) 
    print("Number of words",num_words)
    print("Number of Characters ",num_chars)

    
def main():
    CountFileContent()

if __name__ == "__main__":
    main()