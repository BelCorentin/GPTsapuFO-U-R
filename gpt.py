import requests

with open("key.txt", "r") as f:
    key = f.readline()


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


print(f"{bcolors.WARNING} \n HAL: \n I am ready to hear your query \n {bcolors.ENDC}")

while True:
    user_input = input("")
    data = {
        "input": {
            "Can I use Hydra, the python lib for a custom machine learning experiment?": user_input
        }
    }
    headers = {"Authorization": f"Basic {key}"}
    response = requests.post(
        "https://dashboard.scale.com/spellbook/api/v2/deploy/y2527z8",
        json=data,
        headers=headers,
    )

    print(f"{bcolors.WARNING} \n HAL: {response.json()}  {bcolors.ENDC}")
