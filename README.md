# Rivers of Iron (RoI)

![Rivers of Iron (RoI)](icon.png)

Minecraft version 1.12.2

<https://www.curseforge.com/minecraft/modpacks/rivers-of-iron/>

## RELEASE Status (Not build.)

[![Release Status](https://travis-ci.com/HenryFBP/rivers-of-iron-mc.svg?branch=master)](https://travis-ci.com/HenryFBP/rivers-of-iron-mc)

## [Issues](ISSUES.md)

## [Description](DESCRIPTION.md)

## [Mods](mods)

### [Optimization](OPTIMIZATION.md)

## Playing

### Download it from here

See <https://github.com/HenryFBP/rivers-of-iron-mc/releases>.

You want to download the ZIP files called 'rivers-of-iron-release-*.zip'.

### Generating ZIP file

    packwiz cf export

Or...

    python3 Makefile.py

### Twitch

Look it up on Twitch (`Mods > MC > Browse Modpacks > Search > [Rivers of Iron]`)

Or...

`Mods > MC > My Modpacks > Create Custom Profile > or (import) a ...` and supply it the .ZIP file.

### DIY/MultiMC

Import the .ZIP file in MultiMC.

### Multiplayer

#### Singleplayer hosting

By default, port `25565` is used.

Try ZeroTier or just port forward.

#### Dedicated server

Taken from <https://www.reddit.com/r/MultiMC/comments/bfjbxr/multimc_modpack_server_how_to_do/elemvol?utm_source=share&utm_medium=web2x&context=3>

1. Import the pack into MultiMC/Twitch.
2. Download <https://adfoc.us/serve/sitelinks/?id=271228&url=https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.12.2-14.23.5.2854/forge-1.12.2-14.23.5.2854-installer.jar> (from <https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.12.2.html>)
3. Run the installer.
4. Change the path for the Forge installer to the installed modpack (e.g. `C:\tools\MultiMC\instances\rivers-of-iron-latest-v1.0.4-0714798\minecraft`)
5. Make sure 'Install Server' is checked.
6. Run the `.bat` or `.sh` file in the installed modpack folder.

## Redistributing this modpack

Go ahead! No license.

Read <https://authors.curseforge.com/knowledge-base/game-specific-support/120-how-to-create-a-modpack> for more info.

## CI

See <https://github.com/HenryFBP/gooeyiron>.

## Releasing

### Version conventions

#### X.n.n - Major:

- For massive game-breaking changes that warrant a new world.
- For missing block IDs, broken factories.

#### n.X.n - Minor:

- For new mods that do NOT remove blocks or break factories.
- For new quests.
- For tweaks that do not remove items.

#### n.n.X - Patch

- For small bugfixes.

### Via Git

1.  Switch branch to `release` -- i.e. `git checkout release`.
2.  Update the `release` branch to a state you want to release from.

    Example: `git merge master` to update `release` with all the commits from `master`.

3.  Run `git [diff|log] MOST_RECENT_VERSION` to see what's changed since last release
4.  Update the `RELEASE-NOTES.md` file. This is a log of all release notes.
5.  Optionally, run `python3 Makefile.py` and test the modpack. Fix and repeat 1-5 until it works.
6.  Make a commit for the `RELEASE-NOTES.md` file, and all other files you wish to be released.
    
    Note: the word `alpha` and `beta` will cause the releases to be tagged as such in CurseForge.

7.  Run `git tag -a vXXX -m "Releasing version XXX"`, `XXX` being the new release version.
8.  `git push origin release --tags`. Travis should make a .zip and upload it to Github.
9.  Run `git checkout master` and then `git merge release` and then `git push` to copy the tags and updates to the release notes over to `master` branch.

### Via CurseForge

This step requires a Git release to take place first.

On <https://www.curseforge.com/project/421665/files/upload>,

1.  Copy the release .ZIP file and upload it.
2.  Copy the [DESCRIPTION.md](DESCRIPTION.md) if it has changed.
3.  Copy the relevant parts of the [RELEASE-NOTES.md](RELEASE-NOTES.md).
4.  Wait for a mod to wake up and approve.

### Comparing releases (tags)

From <https://stackoverflow.com/questions/3211809/how-to-compare-two-tags-with-git>.

- `git diff v0.0.1 v0.0.3`: Comparing file changes between tags:
- `git diff v1.0.2`: Comparing file changes between a tag and the HEAD
- `git log v0.0.1..v0.0.3`: Comparing commits between tags

## Scripts

Mostly deprecated. Use `packwiz`.

## Tools

### PackWiz

<https://github.com/comp500/packwiz>

### Importing edited CurseForge zip files 

1. Put the ZIP file in `input/`
2. Execute the file `./scripts/import-zip-and-clobber-files.\[ps1/sh\]`. NOTE that this can delete files in `./`.

### Adding mods

    packwiz cf install
