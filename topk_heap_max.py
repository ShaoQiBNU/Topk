########## 堆调整函数 ###########
'''
实现num[j]~num[k]的调整，使其满足小根堆的性质
'''
def heapadjust(num_k,j,k):

	##### j节点的左孩子 #####
	i=2*j

	##### j节点的值 #####
	temp=num_k[j]

	##### 从j节点开始调整 #####
	while i<=k:

		##### 判断j节点是否有右孩子以及比较左右孩子的大小 #####
		if (i+1)<=k and num_k[i]>num_k[i+1]:

			##### 如果左孩子>右孩子，则i=i+1，这样i的值是最小孩子的下标 #####
			i=i+1

		##### 比较j节点与最小孩子的大小 #####
		if num_k[i]>temp:

			##### 如果j节点小于最小孩子，不做任何处理 #####
			break

		##### 如果j节点大于最小孩子，交换两者，将最小值放在j节点 #####
		num_k[j]=num_k[i]

		##### j节点更新为最小孩子的节点i #####
		j=i

		##### 计算节点i的左节点，重复此过程 #####
		i=i*2

	##### j节点更新为原来j节点的值 #####
	num_k[j]=temp


########## 堆初始化函数 ###########
def buildheap(num_k,k):

	##### 最后一个非叶子节点 #####
	i=int(k/2)

	##### 依次向前遍历非叶子节点 #####
	for j in range(i,0,-1):

		##### 调整堆 #####
		heapadjust(num_k,j,k)

########## qsort ###########
def topk_heapsort(num,n,k):

	##### 将num的前k个元素做初始化堆———小根堆 #####
	num_k=[-1]
	num_k.extend(num[0:k].copy())
	buildheap(num_k,k)

	##### 遍历num的k+1~n个元素 #####
	for i in range(k,n):

		##### 与小根堆的堆顶元素比较如果num[i]>num_k[1]，则替换num_k[1]，然后对小根堆做调整 #####
		if num[i]>num_k[1]:
			
			##### 如果num[i]>num_k[1]，则替换num_k[1] #####
			num_k[1]=num[i]
			
			##### 然后对小根堆做调整 #####
			heapadjust(num_k,1,k)
	
	return num_k


########## main函数入口 ###########
if __name__ == '__main__':

	########## 列表 ###########
	num=[111,56,3,6,21,32,4,43,43,98,32,43,54,32,45,23,4,66,86,21]
	k=6
	n=len(num)

	########## print before sort ###########
	print(num)

	########## qsort ###########
	res=topk_heapsort(num,n,k)
	print(res)
