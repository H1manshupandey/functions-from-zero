import wikipedia

def scrape(name = "Microsoft", length = 2):
    results = wikipedia.summary(name, sentences = length)
    return results