X = array[:,2:5] #memisahkan fitur dari dataset.
Y = array[:,0:1]  #memisahkan class dari dataset

dataset=pd.DataFrame({"Customer ID":array[:,0],"Gender":array[:,1],"Age":array[:,2],"Income":array[:,3],"Spending Score":array[:,4]})
print("dataset sebelum dinormalisasi :")
print(dataset.head(10))

min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1)) #inisialisasi normalisasi MinMax
data = min_max_scaler.fit_transform(X) #transformasi MinMax untuk fitur
dataset = pd.DataFrame({"Age":data[:,0],"Income":data[:,1],"Spending Score":data[:,2],"Customer ID":array[:,0],"Gender":array[:,1]})

print("dataset setelah dinormalisasi :")
print(dataset.head(10))
