from bs4 import BeautifulSoup

import os
import sys


def _get_app_name(input_message="Enter an app name: "):
    try:
        app_name = sys.argv[1]
    except IndexError:
        app_name = input(input_message)

    # Validate app name
    allowed_app_names = []
    for item in os.listdir("."):
        if os.path.isdir(item) and not item.startswith("."):
            allowed_app_names.append(item)

    if app_name not in allowed_app_names:
        input_message = f"This app name doesn't exist. Please choose an app name in {allowed_app_names}: "
        app_name = _get_app_name(input_message)

    return app_name


def _get_version_number():
    try:
        version_number = sys.argv[2]
    except IndexError:
        version_number = input("Enter a version number: ")

    return version_number


def _get_protocol(input_message="Enter a protocol (https or ssh): "):
    try:
        protocol = sys.argv[3]
    except IndexError:
        protocol = input(input_message)

    allowed_protocols = ["https", "ssh"]
    if protocol not in allowed_protocols:
        input_message = f"This protocol is not supported. Please choose one in {allowed_protocols}: "
        protocol = _get_protocol(input_message)

    return protocol


if __name__ == "__main__":
    app = _get_app_name()
    version = _get_version_number()
    protocol = _get_protocol()

    with open("commit_message.txt", "w") as f:
        commit_message = f"chore({app}): release version {version}"
        f.write(commit_message)

    with open(f"{app}/index.html", "r+") as html:
        soup = BeautifulSoup(html, 'html.parser')
        new_a = soup.new_tag("a")
        new_a["href"] = f"git+{protocol}://git@github.com/briefmnews/{app}.git@{version}#egg={app}-{version}"
        new_a.string = f"{app}-{version}"
        soup.html.body.insert(0, new_a)

    with open(f"{app}/index.html", "w") as html:
        html.write(str(soup.prettify()))

    sys.stdout.write(commit_message)
