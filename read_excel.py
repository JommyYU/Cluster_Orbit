import xlrd

#读取excel数据
fileNum = 22 
dataset = np.zeros((1024,fileNum*30))
for file in range(10,10+fileNum):
	filepath ='D:/704/work/长沙理工/数据/轴心轨迹-'+str(file)+'.xlsx'

	workbook = xlrd.open_workbook(filepath)
	table = workbook.sheet_by_index(0)
	print(table.nrows,table.ncols)
	for i in range(1,table.ncols):
		for j in range(1,table.nrows-1):
			dataset[j-1,i+30*(file-10)-1] = table.cell_value(j,i)

#print(dataset[1,659])
np.save("dataset.npy",dataset)
#读取数据end




