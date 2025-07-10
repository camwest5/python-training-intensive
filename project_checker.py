import os
import pandas as pd
# Go through all the project folders and check 

# 1. Data
# 2. Requirements

root = os.getcwd()

for path, dirs, files in os.walk("Projects"):
    os.chdir(root)


    if path == "Projects":
        continue

    for filename in files:
        if filename[-4:] != ".qmd":
            continue

        with open(path + "/" + filename) as project:
            source = project.read()

        print()
        print(f"Checking \033[1m{path + '/' + filename}\033[0m...")


        # Check data loads
        load_start = 0
        while True:
            load_start = source.find("pd.read", load_start + 1)

            if load_start == -1:
                break
            
            load_end = source.find(")", load_start) + 1
            
            load_command = source[load_start:load_end]

            os.chdir(path)

            try: 
                exec(load_command)
            except FileNotFoundError:
                print(f"\033[31mBAD DATA PATH\033[0m")
            except Exception as e:
                print(f"Encountered {e}")
            else:
                print(f"\033[32mDATA OK\033[0m\t ({load_command})")
                

        # Check dependencies
        import_start = 0
        while True:
            import_start = source.find("import", import_start + 1)

            if import_start == -1:
                break
            
            import_end = source.find("\n", import_start)

            import_command = source[import_start:import_end]

            try: 
                exec(import_command)
            except ModuleNotFoundError:
                print(f"\033[31mBAD REQS\033[0m")
            except Exception as e:
                print(f"Encountered '{e}'")
            else:
                print(f"\033[32mREQS OK\033[0m\t ({import_command})")



