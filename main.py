from pytube import YouTube
import sys
import urllib.request
import re

class main():
    search = []
    allargs = len(sys.argv)
    for i in range(2, allargs):
        search.append(sys.argv[i])
    
    searchLink = "https://www.youtube.com/results?search_query="
    for i in search:
        if i == allargs:
            searchLink = searchLink + i
        else:
            searchLink = searchLink + i + "+"
    searchLink = searchLink[:-1]
    searchResults = urllib.request.urlopen(searchLink)
    video_ids = re.findall(r"watch\?v=(\S{11})", searchResults.read().decode())
    downloadLink = "https://www.youtube.com/watch?v=" + video_ids[0]
    
    print("Download...")
    Download = YouTube(downloadLink).streams.get_highest_resolution()
    DownloadPath = sys.argv[1]
    Download.download(DownloadPath)
    print("Download complete!")

if __name__ == "__main__":
    main()
