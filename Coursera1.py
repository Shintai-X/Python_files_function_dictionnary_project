punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    for p in punctuation_chars:
        if p in string:
            string = string.replace(p ,"")
    return string
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(string):
    count = 0
    lower_string = string.lower()
    avg_string = strip_punctuation(lower_string)
    final_string = avg_string.split()
    for word in positive_words:
        if word in final_string:
            count = count + 1
    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())



def get_neg(string):
    count = 0
    lower_string = string.lower()
    avg_string = strip_punctuation(lower_string)
    final_string = avg_string.split()
    for word in negative_words:
        if word in final_string:
            count = count + 1
    return count


with open("resulting_data.csv" , "w" ) as result_file:
    result_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    result_file.write('\n')
    with open("project_twitter_data.csv") as twitter_file:
        lines = twitter_file.readlines()
        for line in lines[1:]:
            #line1 = line[2].replace("\n","")
            line2 = line.split(",")
            string='{},{},{},{},{}'.format(int(line2[1]),int(line2[2]),get_pos(line2[0]),get_neg(line2[0]),-(get_neg(line2[0])+get_pos(line2[0])))
            print(string)
            result_file.write(string)
            result_file.write("\n")




