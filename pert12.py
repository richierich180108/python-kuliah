#file = open('file_example\\file_example.txt','r')
with open('file_example\\file_example.txt','r') as file:

    content = file.read(20)
    file.close()
    print(content)