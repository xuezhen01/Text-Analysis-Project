from nltk.corpus import stopwords
from unicodedata import category
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from mediawiki import MediaWiki
from thefuzz import fuzz

# Opening the data source 

wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")
# print(babson.title)
# print(babson.content)

# Text processing 
def text_frequencies(content):
    """
        This function returns the words in the website and counts the frequencies of the word and returns it in a dictionary
    """
    text_dict = {}

    for word in content.split():
        # transform word to lowercase
        word = word.lower()

        # update the dictionary
        text_dict[word] = text_dict.get(word, 0) + 1
    return text_dict         

def summary_stats(words):
    """
        this function removes stop words first & ensures that other characters e.g. numbers and special characters are not considered 
        and then identifies the top 10 words of the text, 
    """
    filtered_words = {}
    for word in words.keys():
        if word not in stopwords.words('english') and word.isalpha():
            filtered_words[word] = words[word]
        
    filtered_words =  dict(sorted(filtered_words.items(),key=lambda item: item[1], reverse=True))
    first10pairs = {k: filtered_words[k] for k in list(filtered_words)[:10]}

    return first10pairs

def perform_nltk(content):
    """this function performs mltk sediment analysis. It first removes the stop words
    and then gauges the mood of the text by providing the text analysis"""
    filtered_content = ""
    for word in content:
        if word not in stopwords.words('english') and word.isalpha():
            filtered_content += word
    score = SentimentIntensityAnalyzer().polarity_scores(filtered_content)
    return score

def text_similarity(text1, text2) :
    """This function uses Thefuzz library to compare text similarity with the wikipedia result for Babson college and Harvard University"""
    return fuzz.ratio(text1, text2)
    # fuzz.partial_ratio(text1, text2)
    # fuzz.token_sort_ratio(text1, text2)

def markov_analysis():
    import markovify

    # Build the Markov model
    text_model = markovify.Text(babson.content)

    # Print three randomly-generated sentences
    output = "The 3 generated sentences are: \n" 

    for i in range(3):
        # print(text_model.make_sentence())
        output += text_model.make_sentence() 
        output += "\n"

    return output
    

def main():
    text_dict = text_frequencies(babson.content)
    print("Words from this data source: \n", text_dict)
    print("==============================")

    summary_text = summary_stats(text_dict)
    print("Top 10 words in this text: \n", summary_text) 
    print("==============================")

    sediment_analysis = perform_nltk(babson.content)
    print("sediment analysis results: \n", sediment_analysis)
    print("==============================")

    school_page = wikipedia.page("Harvard University")
    similarity = text_similarity(babson.content, school_page.content)
    print("fuzz ratio is", similarity)
    print("==============================")

    print(markov_analysis())

if __name__ == '__main__':
    main()


