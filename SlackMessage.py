import getopt
import os

import requests
import sys

from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()
# send slack message using slack api
def send_slack_message(message):
    slack_url = os.environ["SLACK_URL"]
    payload = '{"text":"%s"}' % message
    response = requests.post(slack_url, data=payload)
    print(response.text)


def main(argv):
    message = ""
    try:
        opts, args = getopt.getopt(argv, "hm:", ["messsage="])
    except getopt.GetoptError:
        print("SlackMessage.py -m <message>")
        sys.exit(2)
    if len(opts) == 0:
        message = "Hello world"
    for opts, arg in opts:

        if opts == "-h":
            print("SlackMessage.py -m <message>")
            sys.exit()
        elif opts in ("-m", "--message"):
            message = arg
    send_slack_message(message)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main(sys.argv[1:])
