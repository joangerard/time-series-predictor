import matplotlib.pyplot as plt

file_names = ["2-exe-T-1000000-t-100000.txt", "4-exe-T-1000000-t-100000.txt", "8-exe-T-1000000-t-100000.txt"]
labels = ["2","4","8"]

all_data = []
count = 0
for file_name in file_names:
    count+=1
#    print(count)
    file = open(file_name,"r")
    data = file.read().split('\n')
    
    times = []
    for x in data:
        row = x.split(' ')
        if (len(row) > 1):
            times.append(float(row[1]))
    
    all_data.append(times)

plt.boxplot(all_data,patch_artist=True,labels=labels)
plt.xlabel("Number of Executors")
plt.ylabel("Job Duration")
plt.savefig("number_of_executors.png")
plt.close()