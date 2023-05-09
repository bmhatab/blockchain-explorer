import pandas

txt = """ 

WETH:
0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2

protocolFeeRecipient:
0x4E1D26bFeF49938673227A80eCC732Bead86735B

"""

# Convert text to lowercase
txt_lower = txt.casefold()

# Split text into words
words = txt_lower.split()

# Filter for words beginning with '0x', these are characters of the ethereum contract addresse.
new_words = [word for word in words if word.startswith('0x')]

# Create a list of unique words, checking for duplicates
# A set is a collection of unique elements, meaning that each element appears only once in the set

unique_words = list(set(new_words))

# Create a list of JSON objects
json_objs = [{'address': word} for word in unique_words]

# Convert list to pandas series
result = pandas.Series(json_objs)

# Convert series to JSON and save to file
result.to_json('data.json', orient='split', index=False)





