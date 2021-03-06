#!/bin/python3
from formats.links import links
from helpMessage import helpMessage
from send import sendFolder, sendFile
import os
from dotenv import load_dotenv
from cli import cli, isCommandOption
import signal

from shortenLink import shortenLink

# preprocess variables
# environment variables
load_dotenv()
server = os.environ["DESTINATION_SERVER"]
port = int(os.environ["DESTINATION_PORT"])
user = os.environ["DESTINATION_USER"]
host_path = os.environ["DESTINATION_HOST_PATH"]
server_path = os.environ["DESTINATION_SERVER_PATH"]

# trap keyboardinterrupt
def sigint_handler(signal, frame):
    print('\nStopped by KeyboardInterrupt')
    exit(0)


signal.signal(signal.SIGINT, sigint_handler)

if (isCommandOption("h", "help")):
    helpMessage()
    quit()
if ("links" in cli.instructions):
    links(cli.file)

if (os.path.isdir(cli.file)):
    sendFolder(cli.file, not ("yes" in cli.instructions))
else:
    sendFile(cli.file)

print("files available at:")

fileLink = f"https://{server}{server_path}{os.path.basename(cli.file)}"
if ("shorten" in cli.instructions):
    fileLink = shortenLink(fileLink)

print(fileLink)
