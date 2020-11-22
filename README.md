## Mods

See <rivers-of-iron/modlist.html>.

## Releasing

1.  Switch branch to `release`.
2.  Update the `release` branch to a state you want to release from.

    Example: `git merge master` to update `release` to `master`.

3.  Update the `VERSION` file. This file will be used by Jenkins to tag the release.
4.  Make a commit for the `VERSION` file

## CI

See <https://github.com/HenryFBP/gooeyiron>.

## Scripts

Mostly deprecated. Use `packwiz`.

## Playing

### Generating ZIP file

    packwiz cf export

### Twitch

Look it up on Twitch (`Mods > MC > Browse Modpacks > Search > [Rivers of Iron]`)

Or...

`Mods > MC > My Modpacks > Create Custom Profile > or (import) a ...` and supply it the .ZIP file.

### DIY/MultiMC

Import the .ZIP file in MultiMC.

## Redistributing this modpack

Go ahead! No license.

Read <https://authors.curseforge.com/knowledge-base/game-specific-support/120-how-to-create-a-modpack> for more info.

## Tools

### PackWiz

<https://github.com/comp500/packwiz>

### Importing edited CurseForge zip files 

1. Put the ZIP file in `input/`
2. Execute the file `./scripts/import-zip-and-clobber-files.\[ps1/sh\]`. NOTE that this can delete files in `./`.

### Adding mods

    packwiz cf install