import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

def generate_word_cloud(text):
    # Split the text into individual words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Generate a word cloud from the word counts
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_counts)

    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Example usage
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Pellentesque et risus id neque lobortis efficitur.
Nunc ullamcorper neque at placerat mollis.
Curabitur tempus malesuada metus, id cursus nulla aliquet nec.
Nulla facilisi. Etiam tempus dapibus orci nec pharetra.
"""

generate_word_cloud(text)
