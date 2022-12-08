f = open("inputs/7.txt", "r")

lines = [x for x in f]

directories = {}

cwd = ""

for i in range(len(lines)):
    # remove /n from lines
    x = lines[i].strip()
    # shell command
    if x[0] == "$":
        print(f"cwd: {cwd}")
        print(f"x: {x}")
        chars = x.split(" ")
        # cd command
        if chars[1] == 'cd':
            # remove last folder
            if chars[2] == "..":
                # remove last folder from file path
                cwd = ''.join(folder + ";" for folder in cwd.split(";")[:-2])
                continue
            # normal cd command
            else:
                # add file path to end of current working directory, separate folders with ;
                cwd += chars[2] + ";"
                # skip the "ls" command
                i += 2
                # Initialize folder if haven't visited already
                if cwd not in directories:
                    directories[cwd] = 0
                # Parse directories/files until you hit the next command
                while i < len(lines) and lines[i][0] != "$":
                    # If directory -> move on and ignore
                    if lines[i].split(" ")[0] == "dir":
                        i += 1
                        continue
                    # If file
                    else:
                        # For all folders in the file path, (starting from root), add size of file to total sum
                        folders = cwd.split(";")[:-1]
                        build_dir = ""
                        for folder in folders:
                            build_dir += folder + ";"
                            directories[build_dir] += int(lines[i].split(" ")[0])
                    i += 1

print(directories)

totalAmt = directories["/;"] - (70000000 - 30000000)

ans = 70000000000
for (key, val) in directories.items():
    if val > totalAmt:
        ans = min(ans, val)

print(ans)