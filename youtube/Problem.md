# Analyse Product Sentiment with Youtube

## Summary

The model should take in the ticker symbol of a company and output a company sentiment score which will be a value between -1 and 1.

## Use cases

* The model will primarily be used for consumer facing companies which sell basic products or services with a mass-market or niche market appeal. 
* YouTube is a haven for people to give their opinions on their daily lives and there is no shortage of this. 
* The site is used for product reviews (e.g. make-up, games, technology, home appliances, new product unboxings) with channels boasting millions of subscribers. 
* Firstly we will try to analyse 2 markets: make-up and technology. 
* Within make-up there is scope to analyse videos giving positive or negative opinions on new companies and products. 

## Part 1 - Brand Names

* Try to parse consumer facing brands the publicly listed company in question owns. 
* This is because the brand names will be the only relevant names on YouTube. 

## Part 2 - Looking for Videos

* Query a YouTube API with the generated brand names. 
* Use a text classifier to judge the relevance of the video based on the video title, tags and description. 

## Part 3 - Video Understanding

* Get the auto generated YouTube subtitles for the specific video and analyse text using a text classifier. 
* This will output a sentiment score for the specific video about a specific brand and should then be weighted using the relevance score. 

## Future Development

* Use auto generated subtitle data to influence the relevance score of a video.
* Try to find a weighting justifying the importance of a specific brand name to the stock price. It might be possible to do this using past correlation data on the brand and the stock. 
* Factor in geographical data to analyse product and service launches/usage/sentiment in a specific region e.g. a soap brand by Unilever might be performing well in emerging markets however influence might be decreasing in developed economies. 
* Analyse advertisments and marketing campaigns companies make on highly influential YouTube channels.
* Analyse relevant video comments for sentiment. 