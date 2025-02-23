import requests
import os
import sys

# 🔥 CONFIGURATION 🔥
GITHUB_REPO = "alexisheraud/game-launcher"  # Remplace avec ton repo
VERSION_URL = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/version.txt"
LATEST_RELEASE_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
NOM_FICHIER = "game.exe"  # Nom de l'exécutable du jeu

# Vérifier la version en ligne
def get_version_en_ligne():
    try:
        response = requests.get(VERSION_URL)
        if response.status_code == 200:
            return response.text.strip()
    except:
        return None

# Vérifier la version locale
def get_version_locale():
    if os.path.exists("version.txt"):
        with open("version.txt", "r") as f:
            return f.read().strip()
    return "0"

# Télécharger la nouvelle version
def telecharger_derniere_version():
    response = requests.get(LATEST_RELEASE_URL)
    if response.status_code == 200:
        latest_release = response.json()
        for asset in latest_release["assets"]:
            if asset["name"] == NOM_FICHIER:
                download_url = asset["browser_download_url"]
                print("Téléchargement de la mise à jour...")
                jeu = requests.get(download_url, stream=True)
                with open(NOM_FICHIER, "wb") as f:
                    for chunk in jeu.iter_content(1024):
                        f.write(chunk)
                print("Mise à jour terminée !")
                return True
    return False

# Comparaison des versions
version_en_ligne = get_version_en_ligne()
version_locale = get_version_locale()

if version_en_ligne and version_locale != version_en_ligne:
    print(f"Nouvelle version disponible : {version_en_ligne}")
    if telecharger_derniere_version():
        with open("version.txt", "w") as f:
            f.write(version_en_ligne)
        os.startfile(NOM_FICHIER)
        sys.exit()
else:
    print("Le jeu est déjà à jour.")
    os.startfile(NOM_FICHIER)
