########## qsort ###########
def qsort(num,left,right):

	########## base number ###########
	base=num[left]

	########## set left and right ###########
	i=left
	j=right

	########## 根据 base number 对数组进行排序 ###########
	while i<j:

		#### i从前向后，寻找第一个大于base number的数字 ####
		if num[i]<base:
			i+=1

		#### j从后向前，寻找第一个小于base number的数字 ####
		elif num[j]>base:
			j-=1
		
		#### i,j交换 ####
		else:
			#### 如果数字相等，则调整i或j，否则会出现问题 ####
			if num[i]==num[j]:
				j-=1 ## i+=1

			#### 交换 ####
			num[i],num[j]=num[j],num[i]

	'''
	此时数组被分割成两个部分  
	-->  array[left] ~ array[i-1] < array[left]
    -->  array[i+1] ~ array[right] > array[left]
    进行两个分割部分的排序：
    如果数组长度大于1，则排序；
    如果数组长度等于1，说明数组只有一个数字，已经排好 
    '''

    ########## 分割后的数组进行排序 ###########
	if i>left:
		qsort(num,left,i-1)
	
	if i<right:
		qsort(num,i+1,right)

########## main函数入口 ###########
if __name__ == '__main__':

	########## 列表 ###########
	num=[21,32,4,43,43,98,32,43,54,32,45,23,4,66,86,21]

	########## set left and right ###########
	left=0
	right=len(num)-1

	########## print before sort ###########
	print(num)

	########## qsort ###########
	qsort(num,left,right)

	########## print after sort ###########
	print(num)