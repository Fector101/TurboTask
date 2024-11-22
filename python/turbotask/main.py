import argparse
from .helper import redText,greenText,readFile,writeFile
from .workers.basic import removeComments, myStrip
import os


def remove_whitespace(input_css_file_path, output_file_path="TurboTask-output/no_whitespace.css",return_=False,comments=False):
    
    # Error Checking for when function is imported directly
    if not os.path.exists(input_css_file_path):
        print(f'{redText(input_css_file_path)} does not exist.')
        
    # Point to Another Function If Folder Path Passed In.
    if(os.path.isdir(input_css_file_path)):
        processDirectory(input_css_file_path, output_file_path)
        return
    
    initial_css=readFile(input_css_file_path)
    if initial_css == None:
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
    
def processDirectory(input_directory, output_directory="TurboTask-output"):
    """Recursively process all .css files in the provided directory."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create output directory if it doesn't exist
    
    exclude_dirs=[ 'node_modules', '.git' ,output_directory]
     
    for root, dirs, files in os.walk(input_directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(".css"):  # Check if the file is a CSS file
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, input_directory)  # Get relative path of the file
                
                # Create corresponding output directory if it doesn't exist
                output_file_path = os.path.join(output_directory, relative_path)
                output_file_dir = os.path.dirname(output_file_path)
                if not os.path.exists(output_file_dir):
                    os.makedirs(output_file_dir)

                # Remove whitespaces and write to the output file
                remove_whitespace(input_file_path, output_file_path)

def main():
    """Main function to handle command-line arguments and call appropriate functions."""
    parser = argparse.ArgumentParser(prog="TurboTask")
    subparsers = parser.add_subparsers(dest="command")
    
    remove_whitespace_parser = subparsers.add_parser("noWhiteSpace", help="Removes all whitespace in CSS File or All CSS Files in Given Dir")
    remove_whitespace_parser.add_argument("input_css_path", help="The Input CSS File or Folder Path argument")
    
    # Optional argument for the output folder (default is 'TurboTask-output')
    remove_whitespace_parser.add_argument("output_path", nargs="?", default="TurboTask-output", help="The optional Output File Path argument. Default is 'TurboTask-output")
    
    args = parser.parse_args()
    
    if args.command == "noWhiteSpace":
        if os.path.exists(args.input_css_path):
            remove_whitespace(args.input_css_path, args.output_path)
        else:
            print(f'{redText(args.input_css_path)} does not exist.')

if __name__ == "__main__":
    main()
