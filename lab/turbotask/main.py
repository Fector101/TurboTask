import argparse





def remove_whitespace(input_css_file_path, output_file_path="TurboTask/no_whitespace.css",return_=False,comments=False):
    no_comments=''
    with open(input_css_file_path, mode='r') as data:
        no_comments=data.read()

    if not comments:
        no_comments=removeComments(CODE) 

    no_whitespaces=myStrip(no_comments)

    if return_:
        return no_whitespaces
    with open(output_file_path,'w')as file:
        file.write(no_whitespaces)




def somecommand(somepath, optionalpath=None):
    print(f"Running somecommand with:")
    print(f"Some path: {somepath}")
    if optionalpath:
        print(f"Optional path: {optionalpath}")
    else:
        print("No optional path provided.")

def main():
    parser = argparse.ArgumentParser(prog="TurboTask")
    subparsers = parser.add_subparsers(dest="command")
    
    remove_whitespace_parser = subparsers.add_parser("removeWhiteSpace", help="Removes all whitespace and comments in CSS File")
    remove_whitespace_parser.add_argument("input_css_file_path", help="The Input CSS File Path argument")
    remove_whitespace_parser.add_argument("output_file_path", nargs="?", default="TurboTask/no_whitespace.css", help="The optional Output File Path argument. Default is 'TurboTask/no_whitespace.css'")
    
    
    # somecommand_parser = subparsers.add_parser("somecommand", help="Run some command")
    # somecommand_parser.add_argument("somepath", help="The required path argument")
    # somecommand_parser.add_argument("optionalpath", nargs="?", help="The optional path argument")
    
    args = parser.parse_args()
    if args.command == "removeWhiteSpace":
        remove_whitespace(args.input_css_file_path, args.output_file_path)

if __name__ == "__main__":
    main()

