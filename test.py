from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

# Example predictions and references
predictions = [
    'The quick brown fox jumps over the lazy dog.',
    'The fast brown fox leaps over the lazy dog.', ' '
]

references = [
    ['The quick brown fox jumps over the lazy dog.'],
    ['A fast brown fox jumps over the lazy dog.'],
    ['The Normans settled in Normandy, France, starting in 911 AD, when the French King granted land to the Viking leader Rollo.\n']
]

# Initialize the smoothing function (optional, helps avoid zero BLEU score for cases with no exact match)
smoothing_function = SmoothingFunction().method1

# Calculate BLEU score with smoothing
bleu_score = corpus_bleu(references, predictions, smoothing_function=smoothing_function)

# Print the result
print(f'BLEU Score: {bleu_score}')
