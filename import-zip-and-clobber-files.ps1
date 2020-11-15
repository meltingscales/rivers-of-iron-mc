echo "This script will copy and overwrite all files from 'input/*.zip' INTO the folder 'rivers-of-iron/'."

$filenum = Get-ChildItem input/*.zip -Recurse -File | Measure-Object | %{$_.Count}

echo "$filenum files in 'input/*.zip' "

if ( "1" -ne $filenum )
{
	echo "Less or more than 1 zip file in 'input/*.zip'. Halting."
	Exit(1)
} else {
	echo "1 File detected in 'input/*.zip'... Extracting..."
}

$filepath = Get-ChildItem input/*.zip


Expand-Archive -LiteralPath $filepath -DestinationPath rivers-of-iron/ -Force