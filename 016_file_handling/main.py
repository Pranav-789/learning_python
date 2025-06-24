#file handling involves performing CRUD operations on a file

# helloFile = open(r'C:\Users\prana\OneDrive\Desktop\learning_python\016_file_handling\hello.txt')
# print(helloFile.read())

# r = open("superman.txt", 'w')
r = open("superman.txt", 'a')

# r.write("Hello this is Pranav and I am writing inside this file")
r.write("and I am appending some content to file")
r.close()