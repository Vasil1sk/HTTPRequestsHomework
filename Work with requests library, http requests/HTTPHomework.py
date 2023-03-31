import requests
import yaml
from pprint import pprint

with open("token.yaml") as f:
    get_token = yaml.load(f, Loader=yaml.FullLoader)
    TOKEN = get_token["token"]

def get_smartest_superhero(superheroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    sh_dict = {}
    for i in response.json():
        if i["name"] in superheroes:
            sh_dict[i["name"]] = i["powerstats"]["intelligence"]
    smartest_superhero = list(max(sh_dict.items(), key=lambda x: x))
    return f"Самый умный супергерой(или злодей) {smartest_superhero[0]} с интеллектом {smartest_superhero[1]}"


pprint(get_smartest_superhero(["Hulk", "Captain America", "Thanos"]))

# class YandexDisk:
#     def __init__(self, token):
#         self.token = token
#
#     def _get_upload_link(self, disk_file_path):
#         upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = {
#             "Content-type": "application/json",
#             "Authorization": "OAuth {}".format(self.token)
#         }
#         params = {"path": disk_file_path, "overwrite": "true"}
#         response = requests.get(upload_url, headers=headers, params=params)
#         return response.json()
#
#     def upload_file_to_disk(self, disk_file_path, filename):
#         result = self._get_upload_link(disk_file_path=disk_file_path)
#         url = result.get("href")
#         response = requests.put(url, data=open(filename, "rb"))
#         response.raise_for_status()
#         if response.status_code == 201:
#             print("Success")
#
# if __name__ == "__main__":
#     ya = YandexDisk(token=TOKEN)
#     pprint(ya.upload_file_to_disk(disk_file_path="Python/File.txt", filename="FileToDisk.txt"))