# Notes about pyautogui MultiMC Testing

- Use AWS/Jenkins VM/Bare metal Jenkins and poll main branch to see if modpack would work

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

    choco install git golang multimc python3 microsoft-visual-cpp-build-tools

    git clone https://github.com/comp500/packwiz
    cd packwiz
    go build
    go install .
    cd ..

    pip install pipenv
    git clone https://github.com/HenryFBP/rivers-of-iron-mc`
    cd rivers-of-iron-mc
    pipenv install