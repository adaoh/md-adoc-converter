from os import write
import subprocess
import os.path
import re

# 'Image' class used to store image data from the Markdown files before conversion to Asciidoc.
class Image:

    def __init__(self):
        self.title = None
        self.path = None
        self.anchor = None
        self.width = 12*38
        self.height = None

# 'doxygen_to_markdown_equations' takes a source file with Doxygen syntax for equations as input and returns the file with standard Markdown syntax.
# It also removes '[TOC]' from the top of each file.
# A '#' is added to all section titles, except for the main section title of each file.
def doxygen_to_markdown_equations(src_file):
    
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
                
                # Skip '[TOC]' as table of contents are set by the index.adoc file.
                if "[TOC]" in edit_line:
                    edit_line = next(file_1)

                # 'fix_sections' adds one # to each section title, except for the main section title of each file.
                if "#" in line[:1]:
                    edit_line = fix_sections(edit_line)

                # Correcting invalid syntax.
                edit_line = edit_line.replace("\\f $", "\\f$")
 
                # Counting how many equations are in the current line. There are two occurrences per equation.
                occurrences = edit_line.count("\\f$")
                
                # If there are no equations, the line gets copied as it is.
                if occurrences == 0:
                    write_line = edit_line
                
                else:
                    write_line = ""

                # The following 'while' loop splits the line on the first two '\f$' elements.
                # Everything between '\f$' gets assigned to the variable 'equation', which gets altered into LaTeX syntax that Pandoc can recognize.
                # Everything after the second occurence of '\f$' gets assigned to the variable 'post', which gets handled identically to the original line by the next iteration of the loop.
                while occurrences > 0:
                    
                    # If there is only one occurence, all text after '\f$', including subsequent lines and up until the next occurence of '\f$', gets treated as a block expression.
                    if occurrences == 1:
                        
                        line_list = edit_line.split("\\f$")

                        pre = line_list[0]

                        # All spaces are removed from equations to avoid syntax errors.
                        equation = line_list[1].replace(" ", "")

                        next_line = next(file_1)
                        occurrences = next_line.count("\\f$")
                        
                        # Adds all subsequent lines to 'equation' until the next occurence of '\f$'.
                        while occurrences == 0:

                            equation += next_line.replace(" ", "")

                            next_line = next(file_1)
                            occurrences = next_line.count("\\f$")

                        line_list = next_line.split("\\f$", 1)

                        equation += line_list[0].replace(" ", "")
                        post = line_list[1]

                        occurrences = post.count("\\f$")

                    # Inline equations (two or more occurences of '\f$' on the same line) are handled here.
                    elif occurrences > 1:                        

                        line_list = edit_line.split("\\f$", 2)

                        pre = line_list[0]
                        equation = line_list[1].replace(" ", "")
                        post = line_list[2]

                        occurrences -= 2
                    
                    # Most equations in the original markdown files are stylized with '\mathrm{equation}'.
                    # '\mathrm' is added to all equations, so that the styling is consistent.
                    if "\\mathrm" not in equation:

                        equation = "\\mathrm{" + equation + "}"
                    
                    # In cases where equation x is stylized without surrounding braces {}, e.g. \f$ \mathrm x \f$, a space is readded to give correct syntax.
                    elif "\\mathrm{" not in equation:
                        
                        equation = equation.replace("\\mathrm", "\\mathrm ")
                    
                    # Fixes syntax. Further explanation at function definition.
                    equation = latex_syntax(equation)

                    # If the line contains no additional equations the line gets written.
                    if occurrences == 0:
                        write_line = write_line + pre + equation + post
                    
                    # If the line contains additional equations, the first part up to and including the handled equation gets written, 
                    # while the rest of the line gets sent to be handled by the next iteration of the 'while' loop.
                    else:
                        write_line = write_line + pre + equation
                        
                        edit_line = post


                file_2.write(write_line)

    return dst_file

# 'latex_syntax' adds spaces behind mathematical expressions such as greek letters and operators.
# Also fixes some syntax that pandoc has problems interpreting.
def latex_syntax(equation):

    eq = equation
    
    eq = eq.replace("\\left[", "[")
    eq = eq.replace("\\left", "")                    
    eq = eq.replace("\\right", "")
    eq = eq.replace("]", "\\]")
    eq = eq.replace("\\times", "\\times ")
    eq = eq.replace("\\Delta", "\\Delta ")
    eq = eq.replace("\\pi", "\\pi ")
    eq = eq.replace("\\rho", "\\rho ")
    eq = eq.replace("\\omega", "\\omega ")
    eq = eq.replace("\\approx", "\\approx ")
    eq = eq.replace("\\alpha", "\\alpha ")
    eq = eq.replace("\\beta", "\\beta ")
    eq = eq.replace("\\dot", "\\dot ")
    eq = eq.replace("\\cdot", "\\cdot ")
    eq = eq.replace("\\eta", "\\eta ")
    eq = eq.replace("\\gamma", "\\gamma ")
    eq = eq.replace("\\sigma", "\\sigma ")
    eq = eq.replace("\\varepsilon", "\\varepsilon ")
    eq = eq.replace("\\xi", "\\xi ")
    eq = eq.replace("\\phi", "\\phi ")
    eq = eq.replace("\\neq", "\\neq ")
    eq = eq.replace("\n", "")

    eq = "$" + eq + "$"

    return eq

# 'fix_sections' adds one '#' to each section title, except for the main section title of each file.
# It also adds '\n' before each title, which fixes issues when there are no blank lines between paragraphs and subsequent section titles.
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

# 'pull_images' removes images from the Markdown files and stores their relevant data in 'Image' instances.
# The 'Image' names gets written in the location of the original images, so that 'push_images' can place the images at the correct positions with Asciidoc syntax.
def pull_images(src_file):
    name = os.path.splitext(os.path.basename(src_file))[0]
    dst_file = os.path.join(os.path.dirname(src_file), "..", name + ".markdown")

    os.makedirs(os.path.dirname(dst_file), exist_ok = True)

    # List of 'Image' instances, which is later returned and used as an argument for 'push_images'.
    image_list = []

    with open(src_file, mode = "r", encoding = "utf-8") as file_1: 

        with open(dst_file, mode = "w+", encoding = "utf-8") as file_2:
            
            for line in file_1:
                
                if "\\anchor" in line or "![" in line:
                    
                    try:
                        img = Image()
                        
                        if "\\anchor" in line:
                            
                            img.anchor = line.split()[1].strip()
                            
                            next_line = next(file_1)

                            if "![" in next_line:
                                
                                #img_data = re.split("\!\[|\]\(\@ref |\)\n", next_line)
                                img_data = re.split("\!\[|\]\(|\)\n", next_line)
                            else:
                                
                                next_line = next(file_1)

                                if "![" in next_line:
                                
                                    #img_data = re.split("\!\[|\]\(\@ref |\)", next_line)
                                    img_data = re.split("\!\[|\]\(|\)\n", next_line)
                        else:
                            
                            #img_data = re.split("\!\[|\]\(\@ref |\)", line)
                            img_data = re.split("\!\[|\]\(|\)\n", line)
                        try:
                            img.title = img_data[1].strip()
                        except:
                            print(line)

                        #illegal_title_symbols = [",", ".", "-", "(", "\)", ")"]
                        illegal_title_symbols = [",", ".", "-", "(", ")", "\)", "\("]

                        for symb in illegal_title_symbols:
                            
                            if symb in img.title:

                                img.title = img.title.replace(symb, "\\" + symb)

                        #img.path = "../" + img_data[2]
                        #img.path = "../" + img_data[2].replace("\@ref ", "")
                        if "figures" in img_data[2]:
                            
                            img.path = "../" + img_data[2].replace("@ref ", "")
                        
                        else:

                            img.path = "../figures/" + img_data[2].replace("@ref ", "")

                        file_2.write(img.title + "\n")

                        next_line = next(file_1)

                        if "@image" in next_line:
                            try:
                                img.width = int(re.split("width=|cm", next_line)[1])*38
                            except:
                                pass
                            
                        else:
                            file_2.write("\n")

                        image_list.append(img)
                    
                    except:
                        pass


                else:

                    file_2.write(line)

    return dst_file, image_list

# 'push_images' looks for lines matching the names of the 'Image' instances. If a match is found the instance's data gets written with Asciidoc syntax.
# Also adds '[discrete]\n' before all subsection titles of 'Release notes', to remove them from the table of contents as well as their section numbers.
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

                    elif "==" in line[:1]:
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

def run_asciidoctor(src_file, doc_title):
    subprocess.call(['asciidoctor', src_file, "--trace"])
    #subprocess.call(['asciidoctor-latex', '-b','html', src_file])
    #subprocess.call(['asciidoctor-web-pdf', src_file, "--trace"])
    #subprocess.call(['asciidoctor', '-o /../build/' + doc_title + '.html', src_file, "--trace"])
    #subprocess.call(['asciidoctor-web-pdf','-f', '-v', src_file, '-t /../build/' + doc_title + '.pdf', "--trace"])
    
# 'create_doc' takes an .adoc index file as input, which contains information on which section files to include in the final document.
def create_doc(index_file):
    with open(index_file, mode = "r", encoding = "utf-8") as file_1:
        doc_title = file_1.readline().split("=")[1].strip()
        
        for line in file_1:
            if "include::" in line:
                name = re.split("::|.adoc\[]", line)[1]

                markdown_src_file = os.path.join(os.path.dirname(index_file), "..", name + ".markdown")

                markdown_file_equations = doxygen_to_markdown_equations(markdown_src_file)
                markdown_stripped_images, image_list = pull_images(markdown_file_equations)

                asciidoc_file = run_pandoc(markdown_stripped_images)
                asciidoc_filled_images = push_images(asciidoc_file, image_list, "release_note" in name)

    run_asciidoctor(index_file, doc_title)
