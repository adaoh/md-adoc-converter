from os import write
import subprocess
import os.path
import re

# Image class used to store image information before converting to .adoc.
class Image:

    def __init__(self):
        self.title = None
        self.path = None
        self.anchor = None
        self.width = 12*38
        self.height = None

# Function that takes in source file with doxygen syntax and outputs file with standard markdown syntax.
def doxygen_to_markdown_formulas(src_file):
    
    # Copies name of input file and assigns output path and file at ./markdown/temp/'name'.markdown
    name = os.path.splitext(os.path.basename(src_file))[0]
    dst_file = os.path.join(os.path.dirname(src_file), "markdown", "temp", name + ".markdown")

    # Output directory is created if it does not exist.
    os.makedirs(os.path.dirname(dst_file), exist_ok = True)

    # Opens source file in read mode.
    with open(src_file, mode = "r", encoding = "utf-8") as file_1: 
        
        # Opens destination file in write+ mode.
        with open(dst_file, mode = "w+", encoding = "utf-8") as file_2:
            
            # The first line of the file remains unaltered.
            file_2.write(file_1.readline())
            next(file_1)

            # Iterate through each line in source file.
            for line in file_1:

                
                edit_line = line
                
                if "[TOC]" in edit_line:
                    edit_line = next(file_1)

                # fix_sections adds one # to each section title, except for the main section title of each file.
                if "#" in line[:1]:
                    edit_line = fix_sections(edit_line)

                edit_line = edit_line.replace("\\f $", "\\f$")
 
                occurrences = edit_line.count("\\f$")
                
                if occurrences == 0:
                    write_line = edit_line
                
                else:
                    write_line = ""

                while occurrences > 0:
                    
                    if occurrences == 1:
                        
                        line_list = edit_line.split("\\f$")

                        pre = line_list[0]
                        formula = line_list[1].replace(" ", "")

                        nextLine = next(file_1)
                        occurrences = nextLine.count("\\f$")

                        while occurrences == 0:

                            formula += nextLine.replace(" ", "")

                            nextLine = next(file_1)
                            occurrences = nextLine.count("\\f$")

                        line_list = nextLine.split("\\f$", 1)

                        formula += line_list[0].replace(" ", "")
                        post = line_list[1]

                        occurrences = post.count("\\f$")

                    elif occurrences > 1:                        

                        line_list = edit_line.split("\\f$", 2)

                        #print(line_list)

                        pre = line_list[0]
                        formula = line_list[1].replace(" ", "")
                        post = line_list[2]

                        occurrences -= 2

                    if "\\mathrm" not in formula:

                        formula = "\\mathrm{" + formula + "}"
                    
                    elif "\\mathrm{" not in formula:
                        
                        formula = formula.replace("\\mathrm", "\\mathrm ")

                    formula = latex_syntax(formula)

                    if occurrences == 0:
                        write_line = write_line + pre + formula + post
                    
                    else:
                        write_line = write_line + pre + formula

                    edit_line = post

                file_2.write(write_line)

    return dst_file

def latex_syntax(form):

    formula = form
    
    formula = formula.replace("\\left[", "[")
    formula = formula.replace("\\left", "")                    
    formula = formula.replace("\\right", "")
    formula = formula.replace("]", "\\]")
    formula = formula.replace("\\times", "\\times ")
    formula = formula.replace("\\Delta", "\\Delta ")
    formula = formula.replace("\\pi", "\\pi ")
    formula = formula.replace("\\rho", "\\rho ")
    formula = formula.replace("\\omega", "\\omega ")
    formula = formula.replace("\\approx", "\\approx ")
    formula = formula.replace("\\alpha", "\\alpha ")
    formula = formula.replace("\\beta", "\\beta ")
    formula = formula.replace("\\dot", "\\dot ")
    formula = formula.replace("\\cdot", "\\cdot ")
    formula = formula.replace("\\eta", "\\eta ")
    formula = formula.replace("\\gamma", "\\gamma ")
    formula = formula.replace("\\sigma", "\\sigma ")
    formula = formula.replace("\\varepsilon", "\\varepsilon ")
    formula = formula.replace("\\xi", "\\xi ")
    formula = formula.replace("\\phi", "\\phi ")
    formula = formula.replace("\\neq", "\\neq ")
    formula = formula.replace("\n", "")

    formula = "$" + formula + "$"

    return formula

def fix_sections(line):

    fixed_line = line

    if "####" in line[:4]:
        fixed_line = line[:4].replace("####", "\n#####") + line[4:]

    elif "###" in line[:3]:
        fixed_line = line[:3].replace("###", "\n####") + line[3:]

    elif "##" in line[:2]:
        fixed_line = line[:2].replace("##", "\n###") + line[2:]

    elif "#" in line[:1]:
        fixed_line = line[:1].replace("#", "\n##") + line[1:]

    return fixed_line

def pull_images(src_file):
    name = os.path.splitext(os.path.basename(src_file))[0]
    dst_file = os.path.join(os.path.dirname(src_file), "..", name + ".markdown")

    os.makedirs(os.path.dirname(dst_file), exist_ok = True)

    image_list = []

    with open(src_file, mode = "r", encoding = "utf-8") as file_1: 

        with open(dst_file, mode = "w+", encoding = "utf-8") as file_2:
            
            for line in file_1:
                
                if "\\anchor" in line or "![" in line:
                    
                    img = Image()
                     
                    if "\\anchor" in line:
                        
                        img.anchor = line.split()[1].strip()
                        
                        nextLine = next(file_1)

                        if "![" in nextLine:
                            
                            img_data = re.split("\!\[|\]\(\@ref |\)\n", nextLine)
                        
                        else:
                            
                            nextLine = next(file_1)

                            if "![" in nextLine:
                            
                                img_data = re.split("\!\[|\]\(\@ref |\)", nextLine)

                    else:
                        
                        img_data = re.split("\!\[|\]\(\@ref |\)", line)

                    img.title = img_data[1].strip()

                    illegal_title_symbols = [",", ".", "-", "(", "\)", ")"]

                    for symb in illegal_title_symbols:
                        
                        if symb in img.title:

                            img.title = img.title.replace(symb, "")

                    img.path = "../" + img_data[2]

                    file_2.write(img.title + "\n")

                    nextLine = next(file_1)

                    if "@image" in nextLine:
                        try:
                            img.width = int(re.split("=|cm", nextLine)[1])*38
                        except:
                            pass
                        
                    else:
                        file_2.write("\n")

                    image_list.append(img)
                    


                else:

                    file_2.write(line)

    return dst_file, image_list

def push_images(src_file, image_list, release_notes = False):
    name = os.path.splitext(os.path.basename(src_file))[0]
    dst_file = os.path.join(os.path.dirname(src_file), "..", name + ".adoc")

    os.makedirs(os.path.dirname(dst_file), exist_ok = True)

    with open(src_file, mode = "r", encoding = "utf-8") as file_1: 

        with open(dst_file, mode = "w+", encoding = "utf-8") as file_2:
            
            first_line = True

            for line in file_1:

                if release_notes:
                    
                    if first_line:
                        file_2.write(line)
                        first_line = False
                        line = next(file_1)

                    elif "==" in line:
                        file_2.write("[discrete]\n")

                image = False
                
                for img in image_list:

                    if img.title == line.strip():

                        block_img = "." + img.title + "\nimage::" + img.path + "[" + img.title + "," + str(img.width) + "]\n"

                        file_2.write(block_img)

                        image = True

                        break

                if image == False:
                    file_2.write(line)

    return dst_file

def run_pandoc(src_file):

    name = os.path.splitext(os.path.basename(src_file))[0]
    dst_file = os.path.join(os.path.dirname(src_file), "..", "asciidoc", "temp", name + ".adoc")

    os.makedirs(os.path.dirname(dst_file), exist_ok = True)

    subprocess.call(['pandoc', src_file, "-s", "-o", dst_file])

    return dst_file

def run_asciidoctor(src_file):
    subprocess.call(['asciidoctor', src_file, "--trace"])
    subprocess.call(['asciidoctor-web-pdf', src_file, "--trace"])

def create_doc(index_file):
    
    with open(index_file, mode = "r", encoding = "utf-8") as file_1: 
        
        for line in file_1:
            
            if "include::" in line:

                name = re.split("::|.adoc\[]", line)[1]

                markdown_src_file = os.path.join(os.path.dirname(index_file), "..", name + ".markdown")

                markdown_file_formulas = doxygen_to_markdown_formulas(markdown_src_file)

                markdown_stripped_images, image_list = pull_images(markdown_file_formulas)

                asciidoc_file = run_pandoc(markdown_stripped_images)

                asciidoc_filled_images = push_images(asciidoc_file, image_list, "release_note" in name)

    run_asciidoctor(index_file)
