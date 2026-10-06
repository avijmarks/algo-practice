# LeetCode #49 — Group Anagrams
# Given an array of strings strs, group together the strings that are anagrams of one another. 
# You may return the groups in any order.

# Input:
# strs = ["eat","tea","tan","ate","nat","bat"]

# Output:
# [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input:
# strs = [""]

# Output:
# [[""]]

# Input:
# strs = ["a"]

# Output:
# [["a"]]

# Anagrams are strings made from the same characters with the same counts, just arranged differently.


def group_anagrams_brute(strs):
    # so the obvious route would be to for each word check if the other words have the letters but that cant 
    # be efficient... whatever
    anagrams = []
    current_group = 0

    for word in strs:
        if not any(word in group for group in anagrams):
            # add new list with  the word
            anagram_group = [word]

            for word_checking in strs:
                # cant do the same word thats not an anagram lol
                if word_checking != word:
                    anagram = True
                    for char in word:
                        if char not in word_checking:
                            anagram = False
                            break

                    if anagram:
                        anagram_group.append(word_checking)

            anagrams.append(anagram_group)



        current_group += 1

    return anagrams

def group_anagrams_inefficient(strs):
    # hashtable approach, convert strs to dict of dicts with values of nested dicts being character counts. then compare.
    char_counts = {}

    for word in strs:
        word_dict = {}
        for char in word:
            if char in word_dict:
                word_dict[char] += 1
            else:
                word_dict[char] = 1
        char_counts[word] = word_dict

    # # so now we have a set of dictionaries of each word seperated by character as key and value as count
    # # now we can just compare each of those dictionaries wholesale
    # results = []
    # for word, dict in char_counts:
    #     # we need a way to backtrace to the original word from the dictionary though, hmmmm do we make char_counts a dict?
    #     #  ^ done
    #     anagram_group = [word]
    #     for word_comp, dict_comp in char_counts:
    #         if word != word_comp:
    #             #cant compare word against itself just like in brute force
    #             if dict == dict_comp:
    #                 #congrats its an anagram!
    #                 anagram_group.append(word_comp)

    #     results.append(anagram_group)

    # problem with ^, we still iterate through words whose group we've already determined so we want to remove those entries
    #not sure how to solve this yet as you cant modify the list while.... ohhhhhh we iterate through normal list and check if it exists in the dict to save some computations

    anagrams = []
    for word in strs:
        if word in char_counts:
            anagram_group = [word]
            for word_comp, word_dict in char_counts.items():
                # ignore same word since it will still be in dict
                if word != word_comp:
                    if char_counts[word] == word_dict:
                        #anagram!
                        anagram_group.append(word_comp)

            #we have now figured out what bucket these words go in so:
            for anagram in anagram_group:
                del char_counts[anagram]
            anagrams.append(anagram_group)

    return anagrams
    # seems like theres two ways to set up this duplicate checking, i could have iterated over full strs in inner loop and deleted when i detect an anagram
    # chose this way arbitrarily. 

def group_anagrams(strs):
    # use a key that is not the word since there can be duplicates.
    char_counts = {} 
    for i in range(len(strs)):
        word_dict = {}
        for char in strs[i]:
            if char in word_dict:
                word_dict[char] += 1
            else:
                word_dict[char] = 1
        char_counts[i] = word_dict

    result_buckets = {} #I want this to be a dictionary with keys  that are the dicts by letter, the value will be lists of words :)
    for key, word_dict in char_counts.items():
        frozen = frozenset(word_dict.items())
        if frozen in result_buckets:
            result_buckets[frozen].append(strs[key])
        else:
            result_buckets[frozen] = [strs[key]]

    return list(result_buckets.values())





            


strs = ["eat","tea","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))

