from bs4 import BeautifulSoup
import requests , os , re , json , platform
from colorama import Fore,init
init()
def clear_terminal():
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')
clear_terminal()
print(Fore.RED + " [+] " + Fore.GREEN + "Give me your target : ")
url = input()
print(Fore.RED + " [+] " + Fore.GREEN + "Give me your file name for save data : ")
file = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# for save all name , id , js var etc...
list_all_for_save = []
# for name attribute
name_attributes = soup.find_all(attrs={"name": True})
print(Fore.RED + " [*] "+ Fore.YELLOW + "echo all name : ")
for attribute in name_attributes:
    print(Fore.WHITE + str(attribute["name"]))
    list_all_for_save.append(attribute["name"])
#for if attribute
id_attributes = soup.find_all(attrs={"id": True})
print(Fore.RED + " [*] "+ Fore.YELLOW + "echo all id : ")
for attribute in id_attributes:
    print(Fore.WHITE + str(attribute["id"]))
    list_all_for_save.append(attribute["id"])
#js variable
script_tags = soup.find_all("script")
javascript_variables = []
print(Fore.RED + " [*] "+ Fore.YELLOW + "echo all js var : ")
for script_tag in script_tags:
    script_content = script_tag.get_text()
    pattern = r'\b(?:var|const|let)\s+([a-zA-Z_][a-zA-Z0-9_]*)\b'
    matches = re.findall(pattern, script_content)
    javascript_variables += matches
for variable in javascript_variables:
    print(Fore.WHITE + variable)
    list_all_for_save.append(variable)
#json keys
conetnt = response.content
soup = BeautifulSoup(conetnt, "html.parser")
scripts = soup.find_all("script")
print(Fore.RED + " [*] "+ Fore.YELLOW + "echo all Json Key object : ")
for script in scripts:
    if "application/ld+json" in script.get("type", ""):
        json_data = script.string.strip()      
        data = json.loads(json_data)
        for key, value in data.items():
            print(Fore.WHITE + key)
            list_all_for_save.append(key)
#save all data into a file
file_path = os.path.join("assets", file)
with open(file_path,"w") as word_list:
    for item in list_all_for_save:
        word_list.write(item + "\n")