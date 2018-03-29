def read_file(fname):
    file = open(fname, 'r')
    print('file' + fname + ':')
    for line in file:
        print(line, end='')
    file.close()
    
if __name__=='__main__':read_file('Data/file.txt')
