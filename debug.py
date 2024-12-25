from cats import *

# big_limit = 10
# test_case = minimum_mewtations("word", "word", big_limit)
# print('word | word:', 'success' if test_case == 0 else 'FAILED, expected ' + str(0) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("aord", "word", big_limit)
# print('Aord | word:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("wora", "word", big_limit)
# print('worA | word:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("ward", "word", big_limit)
# print('wArd | word:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("aword", "word", big_limit)
# print('Aword | word:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("word", "aword", big_limit)
# print('word | Aword:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("worda", "word", big_limit)
# print('wordA | word:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("word", "worda", big_limit)
# print('word | wordA:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("woord", "word", big_limit)
# print('woOrd | word:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))
# test_case = minimum_mewtations("word", "woord", big_limit)
# print('word | woOrd:', 'success' if test_case == 1 else 'FAILED, expected ' + str(1) + ' but got ' + str(test_case))




# p = [[1, 4, 6, 7], [0, 4, 6, 9]]
# words = ['This', 'is', 'fun']
# match = time_per_word(words, p)
# print(get_all_times(match))

# match = time_per_word(['Hi'], [[1,2]])
# fastest_words(match)

# p0 = [2, 2, 3]
# p1 = [6, 1, 2]
#  print(fastest_words(match(['What', 'great', 'luck'], [p0, p1])))

p0 = [2, 2, 3]
p1 = [6, 1, 3]
# print(fastest_words(match(['What', 'great', 'luck'], [p0, p1])))

p2 = [4, 3, 1]
print(fastest_words(match(['What', 'great', 'luck'], [p0, p1, p2])))