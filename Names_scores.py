#https://projecteuler.net/problem=22
def main():
    new_list = []
    list_of_names = []
    f = open('p022_names.txt', 'r')
    for word in f:
        list_of_names.append(word)
    new_list = list_of_names[0].split(',')
    sorted_list = sorted(new_list)
    sum_of_scores = 0
    counter = 1
    for i in sorted_list:
        sum_of_scores += counter * score_name(i)
        counter += 1
    print(sum_of_scores)

def score_name(name):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    score = 0
    for i in name:
        counter = 1
        for j in alpha:
            if j == i:
                score += counter
            else:
                counter += 1
    return(score)

main()                    
