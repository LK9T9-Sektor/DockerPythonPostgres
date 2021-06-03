import docker
import os
import pathlib
import sys

# App folder
app_path = r'app'
# DB Folder
image_path = r'database'
# DB Init script name
db_script_name = 'init_db.py'
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
    
    # Checking if image is already exists
    if len(client.images.list(name=image_tag)) == 0:
        # If not, create image
        image = client.images.build(
            path=path,
            tag=image_tag,
            rm=True
            )
        print(image)

    # Checking if container is already running
    if len(client.containers.list(filters= {'ancestor': image_tag})) == 0:
        # If not, run container
        print("Start to run image: ", image_tag)
        client.containers.run(image=image_tag, ports={'5432/tcp': ('127.0.0.1', 5432)})

    # Path to the app scripts
    script_path = os.path.join(current_folder, app_path)
    os.system('python ' + script_path + '/' + db_script_name)
    
except (Exception) as error:
    print("Docker build error: ", error)
