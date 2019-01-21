# Regular Expressions module
import re

# These are the patterns we're going to look for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but not the other!'

for pattern in patterns:
    print("I'm searching for: "+ pattern)

    if re.search(pattern, text):
        # Returns true if finds the match
        print("MATCH!")

    else:
        print("NO MATCH!")


# re.search is a re.Match obj
match = re.search('term1',text)
print(match)
# <re.Match object; span=(22, 27), match='term1'>
# type <class '_sre.SRE_Match'>
# Index of starting
print(match.start())

# Find all 'match'
print(re.findall('match', 'test phrase match in match middle'))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\n')


###############################################################################
#
#
#

# Helper function for regex
def multi_re_find(patterns,phrase):
    for pattern in patterns:
        print(f"Searching for pattern {pattern}")
        print(re.findall(pattern,phrase))
        print('\n')



test_phrase = 'sdsd..sssddd.sdddsddd...dsds...dssssss...sddddd'
# s followed by 0 or more d
test_patterns = ['sd*']
# s followed by 1 or more d
test_patterns2 = ['sd+']
# s followed by 0 or 1 d
test_patterns3 = ['sd?']
# s followed by 3 d
test_patterns4 = ['sd{3}']
# s followed by 2 or 3 d
test_patterns5 = ['sd{2,3}']
# s followed either by 1 or more s or 1 or more d
test_patterns6 = ['s[sd]+']

multi_re_find(test_patterns,test_phrase)
multi_re_find(test_patterns2,test_phrase)
multi_re_find(test_patterns3,test_phrase)
multi_re_find(test_patterns4,test_phrase)
multi_re_find(test_patterns5,test_phrase)
multi_re_find(test_patterns6,test_phrase)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\n')

test_phrase2 = 'This is a string! But it has punctuation. How can we remove it?'
# Excluding ! or . or ?
# Can think of as multiple split call
tst_patterns = ['[^!.?]+']
# Sequences of all the lowercase characters
tst_patterns2 = ['[a-z]+']
# Sequences of all the uppercase characters
tst_patterns3 = ['[A-Z]+']
# Exclude all the uppercase chars
tst_patterns4 = ['[^A-Z]+']
multi_re_find(tst_patterns,test_phrase2)
multi_re_find(tst_patterns2,test_phrase2)
multi_re_find(tst_patterns3,test_phrase2)
multi_re_find(tst_patterns4,test_phrase2)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\n')


tst_phr = 'This is a string with numbers 12312 and a symbol #hashtag'
# Returns a sequence of digits
tst_pat = [r'\d+']
# Returns NON digits
tst_pat2 = [r'\D+']
# Returns whitespace
tst_pat3 = [r'\s+']
# Returns NON whitespace
tst_pat4 = [r'\S+']
# Returns all alphanumeric
tst_pat5 = [r'\w+']
# Returns all NON alphanumeric
tst_pat6 = [r'\W+']
multi_re_find(tst_pat,tst_phr)
multi_re_find(tst_pat2,tst_phr)
multi_re_find(tst_pat3,tst_phr)
multi_re_find(tst_pat4,tst_phr)
multi_re_find(tst_pat5,tst_phr)
multi_re_find(tst_pat6,tst_phr)
