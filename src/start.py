import docker
import os
import sys
import pathlib

# DB Folder
image_path = r'database'
# Image name
image_tag = 'db-postgre'

# Creating docker client
client = docker.from_env()

client.info()

try:
    # Getting path where script was running
    current_folder = pathlib.Path(__file__).parent.absolute()
    print(current_folder)

    # Path to the database image
    path = os.path.join(current_folder, image_path)
    print(path)

    # Creating image
    image = client.images.build(
        path=path,
        tag=image_tag,
        rm=True
        )
    print(image)

    # Running comtainer
    client.containers.run(image=image_tag, ports={'5432/tcp': ('127.0.0.1', 5432)})
except (Exception) as error:
    print("Docker build error: ", error)
