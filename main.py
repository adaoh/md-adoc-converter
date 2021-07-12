import library
import argparse

parser = argparse.ArgumentParser(description = "Creates document from index file")
parser.add_argument("ind_file", type = str, help = "index file in userguide\\asciidoc\\")
args = parser.parse_args()


if __name__ == '__main__':
    index_file = args.ind_file

    library.create_doc(index_file)