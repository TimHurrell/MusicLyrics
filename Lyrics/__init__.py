import requests
import json
import sys
import statistics

def GetInputData():
     artist = input("Enter artist/ band name....   ")
     print("/n/n")
     return artist


def GetUrlForWebsite(artist):
     brainstring = (f'http://musicbrainz.org/ws/2/release/?query=artist:{artist};fmt=json;limit=100')
     return brainstring


def GetResponseArtistSongDataFromWebSite(brainstring):
     response = requests.get(brainstring)
     return response


def GetResponseLyricDataFromWebSite(artist,song):

     responselyric = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{song}')
     return responselyric



def GetSongFromSet(artist,songset):
    lyricnumberlist = []
    for song in songset:
        responselyric = GetResponseLyricDataFromWebSite(artist,song)
        lyric = GetLyricDataAsString(responselyric)
        lyriclist = CreateListofWordsFromLyricString(lyric)
        songinfo = mySongLyrics()
        songinfo.artist = artist
        songinfo.songname = song
        songinfo.numberofwords = len(lyriclist)
        songinfo.description()
        if songinfo.numberofwords > 1:
           lyricnumberlist.append(songinfo.numberofwords)
    return lyricnumberlist

def CreateListofWordsFromLyricString(lyricstring):
    try:
        lyricstring = lyricstring.replace('\n',' ')
        lyriclist = GetListFromTextString(lyricstring,' ')
        lyriclist = filter(None, lyriclist)
        revisedlist = [word for word in lyriclist if not ' ' in word]
    except Exception as e:       
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        print (template.format(type(e).__name__, e.args))
        revisedlist = [1]
    return revisedlist

def GetMeanAndMedianFromListofNumbers(lyricnumberlist):
    return sum(lyricnumberlist)/len(lyricnumberlist)
    print (f'Mean number of lyrics is  {sum(lyricnumberlist)/len(lyricnumberlist)}')  
    print (f'Median number of lyrics is  {statistics.median(lyricnumberlist)}')

def RemoveFinalNCharactersFromStringEnd(TextString,n):
    TextString = TextString[0:-n]
    return TextString

def GetSongTitleAsString(response): 
    songstring = ''
    a = 0
    for data in response.json()['releases']:
        a = a + 1
        release_status = data.get('status')
        release_title = data.get('title')
        release_type = data['release-group'].get('primary-type')
        try:
            if release_type == "Single" and release_status == "Official":
                songstring = songstring + release_title + "--"                   
        except Exception as e:       
            print (f'exception error {e} ')
    songstring = songstring.replace(' / ','--')
    return songstring


         

def GetLyricDataAsString(responselyric):
    if 'json' in responselyric.headers.get('Content-Type'):
        lyricstring = responselyric.json().get('lyrics')
    else:
        print('Response content is not in JSON format.')
        lyricstring = 'spam'
    if lyricstring is None:
        lyricstring = 'Nonetype'
        print('Empty Lyric String')
    return lyricstring


def GetListFromTextString(Textstring,delimiter):
    newlist = set(Textstring.split(delimiter))
    return newlist

def GetSetFromTextString(Textstring,delimiter):
    newset = set(Textstring.split(delimiter))
    return newset


class mySongLyrics:
    artist = "artist"
    songname = "name"
    numberofwords = 0

    def description(self):
         print (f'{self.artist} released "{self.songname}" which contained {self.numberofwords} words')



def main():    
    artist = GetInputData() 
    brainstring = GetUrlForWebsite(artist) 
    response = GetResponseArtistSongDataFromWebSite(brainstring)
    songstring = GetSongTitleAsString(response)
    songstring = RemoveFinalNCharactersFromStringEnd(songstring,2)
    titleset = GetSetFromTextString(songstring,'--')
    lyricnumberlist = GetSongFromSet(artist,titleset)
    GetMeanAndMedianFromListofNumbers(lyricnumberlist)


if __name__ == "__main__":
    main()






