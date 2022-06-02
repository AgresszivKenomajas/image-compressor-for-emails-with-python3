from PIL import Image
import PIL
import os

directory = "source_images/"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        print(os.path.join(directory, filename))
        file_with_path = os.path.join(directory, filename)
        image = Image.open(file_with_path)
        width, height = image.size
        image = image.resize((width // 2, height // 2))
        image.save("exported_images/%s"% file)
        print("saved..")
        continue
    else:
        continue

