import os
import shutil

def copy_static_to_public(src, dst):
    def copy_recursively(src,dst):
        for item in os.listdir(src):
            src_path=os.path.join(src,item)
            dst_path=os.path.join(dst,item)
            
            if os.path.isfile(src_path):
                shutil.copy(src_path, dst_path)
                print (f"Copied {src_path} to {dst_path}")
            else:
                os.mkdir(dst_path)
                print(f"Entering directory {src_path}")
                copy_recursively(src_path, dst_path)
    
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Deleting current files {dst}")
    os.mkdir(dst)
    print(f"Created fresh file {dst}")
    print("Starting recursive copying")
    copy_recursively(src,dst)            