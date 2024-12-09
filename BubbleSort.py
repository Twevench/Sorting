data = [4, 7, 5, 9, 6, 3, 12, 45, 67, 56]
print ("data sebelum diurutkan: ", data)
banyak_data = len (data)
for i in range (banyak_data - 1):
    for j in range (banyak_data - 1):
        if data [j] > data [j+1]:
            temp = data [j]
            data [j] = data [j+1]
            data [j+1] = temp
print("data setelah diurutkan : ", data)
