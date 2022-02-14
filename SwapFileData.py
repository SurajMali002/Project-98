def swapFileData():
  File1 = input("Enter the original file: ")
  File2 = input("Enter the file to be swapped: ")
  with open(File1, 'r') as a:
    data_a = a.read()
  with open(File2, 'r') as b:
    data_b = b.read()
  with open(File1, 'w+') as a:
    a.write(data_b)
  with open(File2, 'w+') as b:
    b.write(data_a)
  print("Your file has been swapped. Check it!")

swapFileData()