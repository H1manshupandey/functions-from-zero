import wikipedia


def scrape(name, length = 2):
    results = wikipedia.summary(name, sentences = length)
    return results

print(scrape("Facebook"))