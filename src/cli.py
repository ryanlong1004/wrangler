"""CLI for wrangler"""
import argparse
import glob
import pathlib


parser = argparse.ArgumentParser(
                    prog='wrangler',
                    description='Parses and transcribes yaml files to lua scripts',
                    epilog='Text at the bottom of help')

parser.add_argument('paths', nargs='*', type=pathlib.Path)
parser.add_argument('--output-path', type=pathlib.Path)

# if path, process all yaml files
# if file, process file
def files_from_path(_path):
    if _path.is_dir():
            for _file in glob.glob(_path, recursive=True):
                yield _file
                
def get_queue(_paths):
    """creates generator of files for parsing"""
    for _path in _paths:
        if _path.is_dir():
            yield files_from_path(_path)
        yield _path
        
def get_work():
    args = parser.parse_args()
    return {
        'output_path': args.output_path, 
        'queue': get_queue(args.paths)
    }
    
if __name__ == "__main__":
    pass
    
        