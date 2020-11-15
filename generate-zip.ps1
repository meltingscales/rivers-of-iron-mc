$version = Get-Content -Path "VERSION"

$compress = @{
  Path = "rivers-of-iron\*"
  DestinationPath = "rivers-of-iron-$VERSION.zip"
  Force = $TRUE
}

Compress-Archive @compress
