loc = ['서울','부산','광주','대구','대전'];
data = [28.8,33.7,29.4,35.2,26.3];

dic_data = dict(zip(loc,data))
print(sorted(dic_data.items(),key=lambda x : -x[1]))
