data = []
count = 0
length = []
line_length = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length.append(len(line))
		line_length = line_length + len(line)
		count += 1

average = line_length / count

print('檔案讀取完了, 總共有',len(data), '筆資料') 
print('留言平均長度為', average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new), '筆長度小於100的資料')
print(new[0])
print(new[1])


# good = []
# for d in data:
#	if 'good' in d:
#		good.append(d)

#print('一共有', len(good), '筆留言提到good')
#print(good[0])

# 快寫法
good = [1 for d in data if 'good' in d]
print(good) 

# 快寫法 list comprehension
bad = ['bad' in d for d in data]
print(bad)
