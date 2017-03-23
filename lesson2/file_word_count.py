word_count = 0
with open ('referat.txt', 'r', encoding='utf-8' ) as referat:
    for line in referat:
        word_count += len(line.split())
    
print(word_count)
