import yaml
import os
import subprocess


def export_environment():
    command = ["conda", "env", "export", "--no-builds"]
    
    # Open a file in write mode, then pipe the command's output into it
    with open("environment.yml", "w") as outfile:
        subprocess.run(command, stdout=outfile, check=True)
    
    
def change_name(yaml_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    path_name = data["name"]

    new_name = os.path.basename(path_name)
    data["name"] = new_name

    with open(yaml_file, 'w') as f:
        yaml.safe_dump(data, f, sort_keys=False)



if __name__ == "__main__":
    export_environment()
    change_name("environment.yml")