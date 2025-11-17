import os

BANNER = "\n\n" + R"{{< include ../_banner/_banner.qmd >}}" + "\n\n"


def apply_banner(
    standalone_files: list[str] = ["setup.md"],
    dirs: list[str] = ["Workshops/", "Projects/"],
) -> None:
    files = [
        path + file
        for path in dirs
        for file in os.listdir(path)
        if os.path.isfile(path + file)
    ] + standalone_files

    for file in files:
        with open(file) as f:
            content = f.read()

        if BANNER in content:
            print("WARNING: Banner is already in ", file)
            continue

        # Find end of YAML
        i = content.find("---", content.find("---") + 3) + 4

        new_content = "".join((content[:i], BANNER, content[i:]))

        with open(file, "w") as f:
            f.write(new_content)


def remove_banner(
    standalone_files: list[str] = ["setup.md"],
    dirs: list[str] = ["Workshops/", "Projects/"],
) -> None:

    files = [
        path + file
        for path in dirs
        for file in os.listdir(path)
        if os.path.isfile(path + file)
    ] + standalone_files

    for file in files:
        with open(file) as f:
            content = f.read()

        new_content = content.replace(BANNER, "")

        with open(file, "w") as f:
            f.write(new_content)


if __name__ == "__main__":
    apply_banner()
