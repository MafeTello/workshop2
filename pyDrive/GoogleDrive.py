from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from decouple import config

credentials_dir = "/home/maria-fernanda/Desktop/workshop2/PyDrive/credentials_module.json"
id_f = config("Google_Folder")

def login():
    try:
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(credentials_dir)
        if gauth.access_token_expired:
            gauth.Refresh()
            gauth.SaveCredentialsFile(credentials_dir)
        else:
            gauth.Authorize()
    except Exception as err:
        print(err)
    
    return GoogleDrive(gauth)


def Create_file(filename, content, id_folder=id_f):
    credentials = login()
    file = credentials.CreateFile({"title": filename,
                                      "parents": [{"kind": "drive#fiLelink", "id": id_folder}]})
    file.SetContentString(content)
    file.Upload()


def Upload_file(path_file, id_folder=id_f):
    credentials = login()
    file = credentials.CreateFile({"parents": [{"Kind": "drive#fileLink","id": id_folder}]})
    file["title"] = path_file.split("/")[-1]
    file.SetContentFile(path_file)
    file.Upload()



if __name__ == "__main__":
    Create_file("testWorkshop2.txt", "holi holi", "1uX723HTbBtuEdze_6xVfDOnrH3059G_t")
    Upload_file("../Data/merge.csv", "1uX723HTbBtuEdze_6xVfDOnrH3059G_t")
    pass