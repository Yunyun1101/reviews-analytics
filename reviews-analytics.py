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