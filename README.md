# Rivers of Iron (RoI)

## RELEASE Status (Not build.)

[![Release Status](https://travis-ci.com/HenryFBP/rivers-of-iron-mc.svg?branch=master)](https://travis-ci.com/HenryFBP/rivers-of-iron-mc)

## Mods

See <rivers-of-iron/modlist.html>.

### Optimization

See <OPTIMIZATION.md>

## Playing

### Download it from here

See <https://github.com/HenryFBP/rivers-of-iron-mc/releases>.

You want to download the ZIP files called 'rivers-of-iron-release-*.zip'.

### Generating ZIP file

    packwiz cf export

### Twitch

Look it up on Twitch (`Mods > MC > Browse Modpacks > Search > [Rivers of Iron]`)

Or...

`Mods > MC > My Modpacks > Create Custom Profile > or (import) a ...` and supply it the .ZIP file.

### DIY/MultiMC

Import the .ZIP file in MultiMC.

### Multiplayer

By default, port `25565` is used.

Try ZeroTier or just port forward.

## Redistributing this modpack

Go ahead! No license.

Read <https://authors.curseforge.com/knowledge-base/game-specific-support/120-how-to-create-a-modpack> for more info.

## CI

See <https://github.com/HenryFBP/gooeyiron>.

## Releasing

1.  Switch branch to `release` -- i.e. `git checkout release`.
2.  Update the `release` branch to a state you want to release from.

    Example: `git merge master` to update `release` with all the commits from `master`.

3.  Update the `RELEASE-NOTES.md` file. This is a log of all release notes.
4.  Make a commit for the `RELEASE-NOTES.md` file, and all other files you wish to be released.
5.  Run `git tag -a vXXX -m "Releasing version XXX"`, `XXX` being the new release version.
6.  `git push origin release --tags`. Travis should make a .zip and upload it to Github.

### Comparing releases (tags)

From <https://stackoverflow.com/questions/3211809/how-to-compare-two-tags-with-git>.

- git diff v0.0.1 v0.0.3
- git log v0.0.1..v0.0.3

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