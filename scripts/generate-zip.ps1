New-Item -Type Directory -Path output -Force

$version = Get-Content -Path "VERSION"

$compress = @{
  Path = "rivers-of-iron\*"
  DestinationPath = "output\rivers-of-iron-$VERSION.zip"
  Force = $TRUE
}

Compress-Archive @compress
