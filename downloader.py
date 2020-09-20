#!/usr/bin/env python

import sys

import argparse

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from pytube import YouTube


options = webdriver.ChromeOptions()

options.headless = True

# Disables Selenium loggs
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def url_from_video_name(name: str) -> str:
    """Get a youtube video url from video name

    Parameters
    ----------
    name: str
        the name of the video you want to get the url of

    Returns
    -------
    str
        a string that represents the video url of the given name
    """

    search_query = "+".join(name.split())

    search_url = f"https://www.youtube.com/results?search_query={search_query}"

    driver.get(search_url)

    element = driver.find_element_by_xpath('//*[@id="thumbnail"]')

    video_url = element.get_attribute("href")

    return video_url


def download_song(song: str, path: str):
    """Download a song to a specific location

    Parameters
    ----------
    song: str
        the name of the song you want to download
    path: str
        the path to where the song will be downloaded to
    """

    url = url_from_video_name(song)

    video = YouTube(url).streams.filter(only_audio=True).first()

    video.download(path)


def download_songs(songs: list, path: str):
    """Download a list of songs to a specific location

    Parameters
    ----------
    songs: list
        the name of the songs you want to download
    path: str
        the path to where the song will be downloaded to
    """

    for song in songs:
        print(f"Downloading {song}")
        download_song(song, path)

    print("Download Completed!")


def getArguments() -> tuple:
    """Get parsed command line arguments

    Returns
    -------
    tuple
        a tuple that contains the command line arguments (SONGS: str, PATH: str)
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--song", required=True, dest="songs",
                        help="names of the songs you want to download")
    parser.add_argument("-p", "--path", required=True, dest="path",
                        help="the path to where the songs will be downloaded to")

    args = parser.parse_args()

    return (args.songs.split(","), args.path)


def main():
    songs, path = getArguments()
    download_songs(songs, path)
    driver.close()


if __name__ == "__main__":
    main()
