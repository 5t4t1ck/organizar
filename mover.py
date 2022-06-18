from PIL import Image
import os

downloadsFolder = "/home/statick/Downloads/"
picturesFolder = "/home/statick/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".webp"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(
                picturesFolder + "compressed_" + filename, optimize=True, quality=60
            )
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)
            
        if extension in [".mp4"]:
            musicFolder = "/home/statick/Videos/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/home/statick/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)
            

        if extension in [".iso"]:
            musicFolder = "/home/statick/Isos/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)


        if extension in [".pdf"]:
            musicFolder = "/home/statick/Documents/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)

        if extension in [".gz", ".zip"]:
            musicFolder = "/home/statick/Comprimidos/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)

        if extension in [".sh", ".run", ".xpi"]:
            musicFolder = "/home/statick/Comprimidos/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)
