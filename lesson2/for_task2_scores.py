all_scores = [
    {
    'school_class': '4a', 
    'scores': [3,4,4,5,2]
    },
    {
    'school_class': '4b', 
    'scores': [2,5,5,5]
    },
    {
    'school_class': '5a', 
    'scores': [2, 3, 4, 5, 4, 4]
    },
    {
    'school_class': '5b', 
    'scores': [4, 4, 4, 5, 5, 4, 3]
    },
    {
    'school_class': '6a', 
    'scores': [3, 2, 3, 4, 4, 2, 3, 2]
    }
]

students_count = 0
scores_summ = 0

for class_results in all_scores:
    for each_score in class_results['scores']:
        scores_summ += each_score
        students_count += 1 
    class_average = round(sum(class_results['scores']) / len(class_results['scores']), 1)
    print('Средний балл класса {} составляет: {}'.format(class_results['school_class'], class_average))
    

school_score_average = scores_summ / students_count
print('Средний балл школы составляет: {}'.format(round(school_score_average, 1)))


