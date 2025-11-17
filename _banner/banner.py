import os


def determine_banner(path_from: str, path_to: str = "_banner/_banner.qmd") -> str:
    return (
        "\n\n"
        + R"{{< include "
        + os.path.relpath(path_to, path_from)
        + R" >}}"
        + "\n\n"
    )


def apply_banner(
    standalone_files: list[str] = ["setup.qmd"],
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

        banner = determine_banner(os.path.dirname(file))

        if banner in content:
            print("WARNING: Banner is already in ", file)
            continue

        # Find end of YAML
        i = content.find("---", content.find("---") + 3) + 4

        new_content = "".join((content[:i], banner, content[i:]))

        with open(file, "w") as f:
            f.write(new_content)


def remove_banner(
    standalone_files: list[str] = ["setup.qmd"],
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

        banner = determine_banner(os.path.dirname(file))

        new_content = content.replace(banner, "")

        with open(file, "w") as f:
            f.write(new_content)


if __name__ == "__main__":
    apply_banner()
