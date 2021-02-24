import requests
import json
import sys

def GetInputData():
     artist = input("Enter artist/ band name....   ")
     print("You have entered " + artist)
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
     for song in songset:
         responselyric = GetResponseLyricDataFromWebSite(artist,song)
         lyricstring = GetLyricDataAsString(responselyric)
         lyricstring = lyricstring.replace('\n',' ')
         lyriclist = GetListFromTextString(lyricstring,' ')
         lyriclist = filter(None, lyriclist)
         y = [x for x in lyriclist if not ' ' in x]
         print(len(y))
     #print (lyric)

def RemoveFinalNCharactersFromStringEnd(TextString,n):
    TextString = TextString[0:-n]
    return TextString


def GetYearFromDate(date):
    Year = date[0:4]
    return Year



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
      lyricstring = responselyric.json()['lyrics']
      return lyricstring

def GetListFromTextString(Textstring,delimiter):
    newlist = set(Textstring.split(delimiter))
    return newlist

def GetSetFromTextString(Textstring,delimiter):
    newset = set(Textstring.split(delimiter))
    return newset


def ZipListsAndSortOnColumn(List1,List2,n,sorttype):
    zipped_list = (sorted(list(zip(List1, List2)), key=lambda x: x[n], reverse = sorttype))
    return zipped_list


artist = GetInputData() 
brainstring = GetUrlForWebsite(artist) 
response = GetResponseArtistSongDataFromWebSite(brainstring)
songstring = GetSongTitleAsString(response)
songstring = RemoveFinalNCharactersFromStringEnd(songstring,2)
titleset = GetSetFromTextString(songstring,'--')
GetSongFromSet(artist,titleset)


#responselyric = GetResponseLyricDataFromWebSite()
#lyricstring = GetLyricDataAsString(responselyric)
#lyricstring = lyricstring.replace('\n',' ')
#lyriclist = GetListFromTextString(lyricstring,' ')
#lyriclist = filter(None, lyriclist)
#y = [x for x in lyriclist if not ' ' in x]
#print (y)
#print(len(y))

#



#albumlist = GetListFromTextString(albumstring,'--')
#zipped_list = ZipListsAndSortOnColumn(albumlist, yearlist,1,True)


#ITERATION_LIMIT = 10
#for data in (zipped_list[0:ITERATION_LIMIT]):
#           print (data[0] + ' ' + data[1])



