# Analyse Product Sentiment with Youtube

## Summary

The model should take in the ticker symbol of a company and output a company sentiment score which will be a value between -1 and 1.

## Part 1 - Brand Names

* Try to parse consumer facing brands the publicly listed company in question owns. 
* This is because the brand names will be the only relevant names on YouTube. 

## Part 2 - Looking for Videos

* Query a YouTube API with the generated brand names. 
* Use a text classifier to judge the relevance of the video based on the video title, tags and description. 

## Part 3 - Video Understanding

* Get the auto generated YouTube subtitles for the specific video and analyse text using a text classifier. 
* This will output a sentiment score for the specific video about a specific brand and should then be weighted using the relevance score. 

## Future Considerations

* Use auto generated subtitle data to influence the relevance score of a video.
* Try to find a weighting justifying the importance of a specific brand name to the stock price. It might be possible to do this using past correlation data on the brand and the stock. 