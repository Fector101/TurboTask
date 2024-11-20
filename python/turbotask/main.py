# Add code if User passes a folder path and not a file will check for css files and folders in folder 
# and put new version with noWhiteSpace in TurboTask-output folder with same naming convention for folders and files
# Also maybe change command from noWhiteSpace to noWhiteSpace
import argparse
from .helper import redText,greenText,readFile,writeFile
from .workers.basic import removeComments, myStrip


def remove_whitespace(input_css_file_path, output_file_path="TurboTask/no_whitespace.css",return_=False,comments=False):
    initial_css=readFile(input_css_file_path)
    if initial_css == 'error--33*/901438-*--2324':
        return
        
    if not comments:
        initial_css=removeComments(initial_css) 

    no_whitespaces=myStrip(initial_css)

    if return_:
        return no_whitespaces
    
    writeFile(
        content=no_whitespaces,
        file_path=output_file_path,
        good_msg=f"Successfully Created a File without WhiteSpace in {greenText(output_file_path)}",
        error_msg=f"Failed to write File Output in'{redText(output_file_path)}'"
        )
    


def main():
    parser = argparse.ArgumentParser(prog="TurboTask")
    subparsers = parser.add_subparsers(dest="command")
    
    remove_whitespace_parser = subparsers.add_parser("noWhiteSpace", help="Removes all whitespace and comments in CSS File")
    remove_whitespace_parser.add_argument("input_css_file_path", help="The Input CSS File Path argument")
    remove_whitespace_parser.add_argument("output_file_path", nargs="?", default="TurboTask/output/no_whitespace.css", help="The optional Output File Path argument. Default is 'TurboTask/output/no_whitespace.css'")
    
    args = parser.parse_args()
    if args.command == "noWhiteSpace":
        remove_whitespace(args.input_css_file_path, args.output_file_path)

if __name__ == "__main__":
    main()
