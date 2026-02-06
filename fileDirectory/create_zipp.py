import zipfile
import os
import shutil

folder = "mkdir"
os.makedirs(folder, exist_ok=True)

# create sample files
with open(os.path.join(folder, "Value_one.txt"), "w") as f:
    f.write("This is file one")

with open(os.path.join(folder, "Value_two.txt"), "w") as f:
    f.write("This is file two")

# create zip
zip_path = os.path.join(folder, "create_file.zip")

with zipfile.ZipFile(zip_path, "w") as z:
    z.write(os.path.join(folder, "Value_one.txt"), "Value_one.txt")
    z.write(os.path.join(folder, "Value_two.txt"), "Value_two.txt")

# extract zip
with zipfile.ZipFile(zip_path, "r") as z:
    z.extractall(folder)

    extracted_files = z.namelist()
    print("Extracted files:", extracted_files)


#convert any dir to zip
shutil.make_archive("makedir","zip","mkdir")

