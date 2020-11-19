# Notes about pyautogui MultiMC Testing

- Use AWS/Jenkins VM/Bare metal Jenkins and poll main branch to see if modpack would work
- VM with VBox Guest Additions and DirectX support for OpenGL...
    - No OpenGL. This means no main menu. But, forge loading screen shows.
    - I can ditch the check for main menu IF it's detected that a VM is being used...
    - Then look for a black screen,
    - Then look for the string `Forge Mod Loader has successfully loaded (...) mods` in `C:\tools\MultiMC\instances\<NAME>\minecraft\logs\latest.txt`
    - Then loading is done for non-GPU instances.
    - Also, save the log in Jenkins.

- AWS pricing for GPU is garbage, cheaper to buy another PC
- Azure pricing for GPU is garbage, cheaper to buy another PC

## VirtualBox Jenkins Modpack CI/CT Notes

- You don't need a GPU. Minecraft will start black. The script takes this into account.
- 5120MB RAM
- Give Minecraft ~4GB RAM
- You must log into MultiMC.
- Disable VBox Guest Addition mouse integrations.

## Setup Commands

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

    choco install git golang multimc python3 microsoft-visual-cpp-build-tools

    git clone https://github.com/comp500/packwiz
    cd packwiz
    go build
    go install .
    cd ..

    pip install pipenv
    git clone https://github.com/HenryFBP/rivers-of-iron-mc
    cd rivers-of-iron-mc
    pipenv install