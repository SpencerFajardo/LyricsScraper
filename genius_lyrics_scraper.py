# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:40:05 2019

@author: Spencer
"""

# This scraper uses BeautifulSoup to manage web data
from bs4 import BeautifulSoup
import requests

# This function calls all the necessary methods
# to run the scraper and print the lyrics
def run_scraper():
    print_opening()
    artist_name = input("Enter the name of the artist: ")
    song_name = input("Enter the name of the song: ")
    # As per the opening, 'give me suggestions' does something different
    if (song_name == "give me suggestions"):
        get_suggestions(artist_name)
        
    else:
        get_lyrics(artist_name,song_name)

def print_opening():
    print("Welcome to GeniusScraper!")
    print()
    print("To find song lyrics, enter the name of the artist,")
    print("then enter the name of the song you want the lyrics for!")
    print()
    print("If you type in 'give me suggestions' instead of a song, you will receive")
    print("a few song options from your chosen artist!")
    print()
     
# this function checks the genius webpage
# for the given artist and returns to the user
# a list of their most popular songs
def get_suggestions(artist_name):
    artist_name = artist_name.replace(" ", "-")
    url = "http://genius.com/artists/" + artist_name
    
    # Requests allows us to search for url
    r = requests.get(url)
    data = r.text
    
    # Using BeautifulSoup to clean up web data
    soup = BeautifulSoup(data, 'html.parser')
    song = {}
    song["Names"] = [];
    
    # find the song names from the mini_card-title division
    for div in soup.find_all('div', attrs = {'class': 'mini_card-title'}):
        song["Names"].append(div.text.strip().split("\n"));
        
    print()
    for i in song["Names"]:
        print(i[0])
    
    song_name = input("Enter the name of the song: ")
    get_lyrics(artist_name,song_name)

# this function finds the lyrics for a given artist
# and the song given by the user    
def get_lyrics(artist_name, song_name):
    artist_name = artist_name.replace(" ", "-")
    song_name = song_name.replace(" ", "-")
    url = "http://genius.com/" + artist_name + "-" + song_name + "-lyrics"
    
    # Requests allows us to search for url
    r = requests.get(url)
    data = r.text
    
    # Using BeautifulSoup to clean up web data
    soup = BeautifulSoup(data, 'html.parser')
    song = {}
    song["Lyrics"] = [];
    
    # Find song lyrics and strip useless html stuff
    for div in soup.find_all('div', attrs = {'class': 'lyrics'}):
        song["Lyrics"].append(div.text.strip().split("\n"));
    
    # Finally, we print the lyrics
    print()
    if((len(song["Lyrics"]) < 1)):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("The song or artist was not found,")
        print("check for spelling errors and try again!")
        print()
        run_scraper();
    else:
        for i in song["Lyrics"][0]:
            print(i)
    
def main():
    run_scraper()
    
main()