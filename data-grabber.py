import pokebase as pb
from PIL import Image
import requests
import urllib.request 
import os
import csv

def get_images(start, end):
    for i in range (start,end):
        try:
            mon = pb.pokemon(i)

            # if image already exists, move to next
            if os.path.isfile(f'images/{mon.name}.png'):
                print("already have " + mon.name)
                continue
            else:
                print("don\'t have " + mon.name)

            # Get Images
            print("fetching " + mon.name + ". . . . ", end="")
            image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{mon.id}.png"
            data = requests.get(image_url).content
            f = open(f'images/{mon.name}.png','wb')
            f.write(data) 
            f.close()

            image = Image.open(f'images/{mon.name}.png')
            new_image = image.resize((120, 120))
            new_image.save(f'images/{mon.name}.png')
            print("done!")

            
            # print(mon.name)
            # for type_slot in mon.types:
            #     print('{}: {}'.format(type_slot.slot, type_slot.type.name.title()))
            # image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{mon.id}.png"
            # print(image_url)

        except:
            print("couldn\'t find something! breaking :(")
            break


def build_csv(start, end):
    with open('names_and_types.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["name", "type1", "type2", "image_path"]
        
        writer.writerow(field)

        for i in range (start,end):
            try:
                mon = pb.pokemon(i)
                print("writing data for " + mon.name + ". . . . ", end="")

                info = []
                info.append(mon.name)
                for i in range(2):
                    if i > len(mon.types) - 1:
                        info.append(None)
                    else:
                        info.append(mon.types[i].type.name)
                info.append(f'images/{mon.name}.png')
                writer.writerow(info)
                print("done!")
            except:
                print("couldn\'t write row! breaking :(")
                break


if __name__ == "__main__":
    build_csv(1,1100)
    # get_images(1,1100)