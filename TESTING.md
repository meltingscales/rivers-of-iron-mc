# Testing

## Editing FTB Quests

	/ftbquests editing_mode true

## Copying quests/configs over

Just copy all the files you want new users of the modpack to use in `MC_INSTANCE_FOLDER_NAME/config` into `rivers-of-iron/overrides`.

The quests are stored in `MC_INSTANCE_FOLDER_NAME/config/ftbquests/normal/` so they get copied too.

Also see `copy-quests-from-multimc.py`.

## Testing configs

You can just copy all the files `rivers-of-iron/overrides/**` into your Minecraft instance's config folder to test them.

This works for quests too.

## Debugging orespawn

	//replacenear 80 sand,sandstone,grass,dirt,stone,gravel,water,wood,leaves,log air

	//replacenear 80 wildnature:dried_sand,wildnature:slate,wildnature:phyllite,wildnature:gneiss,wildnature:epidosite,wildnature:marble,wildnature:basalt,wildnature:pumice air

	//replacenear 80 wildnature:limestone,wildnature:gypsum,wildnature:umber,wildnature:dolomite,wildnature:conglomerate,wildnature:chalk,wildnature:syenite,wildnature:hardened_sandstone,wildnature:pegmatite,wildnature:carbonatite,wildnature:pumice air

	//replacenear 80 mekanism:oreblock air