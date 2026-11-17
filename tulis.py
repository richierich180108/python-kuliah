with open('file_example\\file_example.txt','r') as f:
    f.readline()
    data = f.readline().strip()
    while data.startswith('#'):
        data = f.readline().strip()
    total = int(data)
    counter = 1
    max = total
    min = total
    for d in f:
        nilai = int(d.strip())
        total += nilai
        counter += 1
        if nilai > max:
            max = nilai
        if nilai < min:
            min = nilai
print(f'hasil penjumlahan {total}')
print(f'hasil rata rata  {total/counter}')
print(f'nilai bsar {max}')
print(f'nilai kecil {min}')