#!/usr/bin/env python3

def addline(line, o, delimiter):
    outputstr = ""
    escape_chars = ["#", "$", "%", "&", "{", "}", "_", "~", "^", "\\"]
    for char in line:
        if char ==  delimiter:
            outputstr += "&"
        elif char in escape_chars:
            outputstr += "\\"+char
        else:
            outputstr += char
    outputstr += "\\\\ \\hline\n"
    o.write(outputstr)


def head_settup(line, o, delimiter):
    colum_num = 0
    colum_str = "c|"
    for char in line:
        if char ==  delimiter:
            colum_num += 1
    for i in range(colum_num):
        colum_str += "c|"
    o.write("\\begin{tabular}{|" + colum_str + "}\n")
    o.write("\\hline\n")

def end_settup(o):
    o.write("\\end{tabular}\n")

def newfilename(filename):
    outputfile = ""
    for char in filename:
        if char != ".":
            outputfile += char
        else:
            return outputfile + "_latex.txt"


def analysis(filename, delimiter):
    outputfile = newfilename(filename)
    print(outputfile)
    f = open(filename, "r")
    o = open(outputfile, "w")
    firstline = True

    for line in f.readlines():
        if firstline == True:
            head_settup(line, o, delimiter)
            addline(line, o, delimiter)
            firstline = False
        else:
            addline(line, o, delimiter)
    end_settup(o)

    f.close()  
    o.close()               

def main():                                                         
    input_txt = input("Input file name (path): ")
    delimiter = input("and input data separator: ")

    analysis(input_txt, delimiter)

if __name__ == '__main__':
    main()
