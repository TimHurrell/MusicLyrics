import unittest
from Lyrics import GetSetFromTextString
from Lyrics import GetMeanAndMedianFromListofNumbers
from Lyrics import GetUrlForWebsite
from Lyrics import CreateListofWordsFromLyricString
from Lyrics import RemoveFinalNCharactersFromStringEnd
from Lyrics import GetLyricDataAsString
from Lyrics import GetSongTitleAsString
from Lyrics import GetSongFromSet


class TestString(unittest.TestCase):
    def test_filter(self):

        """
        Test filter is true
        
        """
        string1 = 'Prove It--Little Johnny Jewel'

        result = list(GetSetFromTextString(string1,'--'))
        self.assertIs(result[1],'Little Johnny Jewel')

    def test_mean(self):
        """
        Test filter is true
        
        """
        list1 =[99,109]

        result = GetMeanAndMedianFromListofNumbers(list1)
        self.assertEqual(result, 104)
    
    def test_url1(self):
        """
        Test filter is true
        
        """
        string1 = 'Queen'

        result = GetUrlForWebsite(string1)
        self.assertEqual(result, 'http://musicbrainz.org/ws/2/release/?query=artist:Queen;fmt=json;limit=100')
    
    
    def test_songwordlist(self):
        """
        Test filter is true
        
        """
        string1 = 'I want to break free. I want to break free'

        

        result = CreateListofWordsFromLyricString(string1)
        self.assertEqual(result[5], 'I')

    
    def test_characterremove(self):
        """
        Test filter is true
        
        """
        string1 = 'I want to break free. I want to break free'
        result = RemoveFinalNCharactersFromStringEnd(string1,5)
        self.assertEqual(result, 'I want to break free. I want to break')
    
    
    def test_testlyric(self):
        """
        Test filter is true
        
        """

        result = GetLyricDataAsString({"lyrics":"Flash - ah - Saviour of the universe\r\nFlash"})
        self.assertEqual(result, 'Flash - ah - Saviour of the universe Flash')
    
    
    def test_testsongtitle(self):
        """
        Test filter is true
        
        """

        result = GetSongTitleAsString({"created":"2021-03-12T17:00:18.435Z","count":219,"offset":0,"releases":[{"id":"e1d326d6-dc5c-4d84-b305-7b437d4c7623","score":100,"status-id":"1156806e-d06a-38bd-83f0-cf2284a808b9","count":1,"title":"Summerstage Central Park NYC 6/16/2007","status":"Official","text-representation":{"language":"eng"},"artist-credit":[{"name":"Television","artist":{"id":"490bde43-5edb-4a93-b3b3-7a0465fd8909","name":"Television","sort-name":"Television"}}],"release-group":{"id":"8353c09e-1f69-4852-8cec-2954fd7a0063","type-id":"6fd474e2-6b58-3102-9d17-d6f7eb7da0a0","primary-type-id":"f529b476-6e62-324f-b0aa-1f3e33d313fc","title":"Summerstage Central Park NYC 6/16/2007","primary-type":"Single","secondary-types":["Live"],"secondary-type-ids":["6fd474e2-6b58-3102-9d17-d6f7eb7da0a0"]},"date":"","country":"US","release-events":[{"date":"","area":{"id":"489ce91b-6658-3307-9877-795b68554c98","name":"United States","sort-name":"United States","iso-3166-1-codes":["US"]}}],"track-count":11,"media":[{"format":"CD-R","disc-count":0,"track-count":11}]}]})
        print (result)
        self.assertEqual(result, 'Flash - ah - Saviour of the universe Flash')

    
    def test_testsongfromset(self):
        """
        Test filter is true
        
        """

        songset = ['Prove It', 'Little Johnny Jewel']

        result = GetSongFromSet('Television',songset)
        print (result)
        self.assertEqual(result[0], 99)




#def GetSongFromSet(artist,songset):
  
 

   
        
 

# why does it work/ not work
if __name__ == '__main__':  
    unittest.main()

 
