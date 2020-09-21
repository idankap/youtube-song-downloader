# YouTube Song Downloader
Download songs from YouTube simply by typing their names

## Installation
To use, download the .zip and extract the contents, or clone the repository by typing

```bash
git clone https://github.com/idankap/youtube-song-downloader.git
```

Add the youtube-song-downloader bin directory to your system `PATH` using one of the two following methods:

### Windows
1. Temporary: Open cmd and execute the command `set PATH="%PATH%;path\to\youtube-song-downloader\bin"`.
2. Permanent: Open cmd as administrator and execute the command `setx /M PATH "%PATH%;path\to\youtube-song-downloader\bin"`.

## Usage
* Execute the command `ysd -s <songs-names> -p <path>`
* And that's it!

### Atributes
The ysd command requires some attributes:

Atribute | Required | Description | Requirements
--- | --- | --- | ---
`-s` or `--songs` | True | The names of the songs you want to download | wrap in quotation marks and each name is separated by a comma
`-p` or `--path` | True | The path to where the songs will be downloaded to | wrap in quotation marks

## License
Licensed under the [MIT License](https://opensource.org/licenses/MIT)
