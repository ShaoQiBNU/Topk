TopK的问题的解决办法
==================

# 一. 问题描述
> 有 N (N>1000000)个数,求出其中的前K个最小/最大的数（又被称作topK问题)。

# 二. 解决方法

## (一) 基本思路
> 最基本的思路，将N个数进行完全排序，从中选出排在前K的元素即为所求。有了这个思路，我们可以选择相应的排序算法进行处理，目前来看快速排序，堆排序和归并排序都能达到O(NlogN)的时间复杂度。

## (二) 数据池思想
> 可以采用数据池的思想，选择其中前K个数作为数据池，后面的N-K个数与这K个数进行比较，若小于/大于其中的任何一个数，则进行替换。这种思路的算法复杂度是O(N*K)。

## (三) 堆
> 从思路(二)可以想到，剩余的N-K个数与前面K个数比较的时候，是顺序比较的，算法复杂度是K。怎么在这方面做文章呢？ 采用的数据结构是堆。

### 1. 堆的概念

> 堆（heap），是一种特殊的数据结构。之所以特殊，因为堆的形象化是一个棵完全二叉树，并且满足任意节点始终不小于（或者不大于）左右子节点（有别于二叉搜索树Binary Search Tree）。其中，前者称为为大顶堆（最大堆，堆顶为最大值），如图1所示，后者小顶堆（最小堆，堆顶为最小值），如图2所示。
![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap.jpg)

> 堆可以看成一个二叉树，所以可以考虑使用二叉树的表示方法来表示堆。但是因为堆中元素按照一定的优先顺序排列，因此可以使用更简单的方法——数组——来表示，这样可以节省子节点指针空间，并且可以快速访问每个节点。堆的数组表示其实就是堆层级遍历的结果，如下图所示：这样对于每一个下标为i的节点，其左子节点在下标为2 x i的位置，其右子节点在下标为2 x i+1的位置，而其父节点在下标为 floor{i/2}，最后一个非叶节点的下标为n/2，其中i从1开始，n为数组长度。通过数组的存储方式，可以通过计算下标，直接获取到相关节点。
![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_save.PNG)

### 2. 堆排序
> 堆排序过程说明。给定一个整形数组a=[-1,5,2,6,0,3,9,1,7,4]，-1为占位符，不参与排序，对其进行升序堆排序。

#### (1)构造初始堆
> 首先，根据数组构建一个完全二叉树，如图所示，然后从最后一个非叶节点开始调整，i=n/2=4，即a[4]=0，开始调整，调整过程为：寻找该节点的左右孩子中的最大值，最大值为7，如果最大的孩子大于该节点，则二者交换，将7和0交换。

![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_1.png)

> 寻找下一个非叶节点开始调整，i=i-1=3，即a[3]=6，开始调整，9和6交换。

![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_2.png)

> 寻找下一个非叶节点开始调整，i=i-1=2，即a[2]=2，开始调整，2和7交换，交换之后发现2不满足堆的性质，继续调整，4和2交换。

![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_3.png)

> 继续寻找下一个非叶节点开始调整，i=i-1=1，即a[1]=5，开始调整，5和9交换，交换之后发现5不满足堆的性质，继续调整，5和6交换。

![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_4.png)

#### (2)排序
> 经过(1)的过程后，此时a[1]为最大值，将其与a[n]交换位置，然后对剩下的a[1]~a[n-1]再次进行堆排序。

![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_5.png)

> 此时最大值位于a[1]位置，将其与a[n-1]交换位置。然后对剩下的a[1]~a[n-2]再次进行堆排序。

![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_6.png)

> 重复上述过程，直至最后

![image](https://github.com/ShaoQiBNU/Topk/blob/master/image/heap_7.png)

#### (3)代码

```python
########## 堆调整函数 实现num[j]~num[n]的调整，使其满足大根堆的性质 ##########
def heapadjust(num,j,n):

	##### j节点的左孩子 #####
	i=2*j

	##### j节点的值 #####
	temp=num[j]

	##### 从j节点开始调整 #####
	while i<=n:

		##### 判断j节点是否有右孩子以及比较左右孩子的大小 #####
		if (i+1)<=n and num[i]<num[i+1]:

			##### 如果左孩子<右孩子，则i=i+1，这样i的值是最大孩子的下标 #####
			i=i+1

		##### 比较j节点与最大孩子的大小 #####
		if num[i]<temp:

			##### 如果j节点大于最大孩子，不做任何处理 #####
			break

		##### 如果j节点小于最大孩子，交换两者，将最大值放在j节点 #####
		num[j]=num[i]

		##### j节点更新为最大孩子的节点i #####
		j=i

		##### 计算节点i的左节点，重复此过程 #####
		i=i*2

	##### j节点更新为原来j节点的值 #####
	num[j]=temp

########## 堆初始化函数 ###########
def buildheap(num,n):

	##### 最后一个非叶子节点 #####
	i=int(n/2)

	##### 依次向前遍历非叶子节点 #####
	for j in range(i,0,-1):

		##### 调整堆 #####
		heapadjust(num,j,n)

########## 堆排序函数 ###########
def heapsort(num,n):

	##### 初始化堆 #####
	buildheap(num,n)

	##### 排序 #####
	for i in range(n,0,-1):

		##### 交换：将第一个数，也就是从num[1]到num[i]中的最大的数，放到num[i]的位置 #####
		num[1],num[i]=num[i],num[1]

		##### 调整：对剩下的num[1]到num[i-1]，再次进行堆排序，选出最大的值，放到num[1]的位置 #####
		heapadjust(num,1,i-1)

########## main函数入口 ###########
if __name__ == '__main__':

	########## 列表 ###########
	num=[-1,5,2,6,0,3,9,1,7,4]
	n=len(num)-1

	########## print before sort ###########
	print(num)

	########## qsort ###########
	heapsort(num,n)

	########## print after sort ###########
	print(num)
```
### 3. 堆实现TopK
> 大根堆维护一个大小为K的数组，目前该大根堆中的元素是排名前K的数，其中根是最大的数。此后，每次从原数组中取一个元素与根进行比较，如小于根的元素，则将根元素替换并进行堆调整（下沉），即保证大根堆中的元素仍然是排名前K的数，且根元素仍然最大；否则不予处理，取下一个数组元素继续该过程。该算法的时间复杂度是O(N*logK)。

> 小根堆维护一个大小为K的数组，目前该小根堆中的元素是排名前K的数，其中根是最小的数。此后，每次从原数组中取一个元素与根进行比较，如大于根的元素，则将根元素替换并进行堆调整（下沉），即保证小根堆中的元素仍然是排名前K的数，且根元素仍然最小；否则不予处理，取下一个数组元素继续该过程。该算法的时间复杂度是O(N*logK)。

## (四) 快速排序
> 利用快速排序的分划函数找到分划位置K，则其前面的内容即为所求。在快排中每次用一个轴将数组划分为左右两部分，轴左边的数都小于轴，轴右边的数都大于轴，轴所在的位置和排好序后的位置相同。这里只要找到第k大的数作为轴进行划分，那么就找到了最大的k个数。该算法是一种非常有效的处理方式，时间复杂度是O(N)。对于能一次加载到内存中的数组，该策略非常优秀。

### 1. 快速排序原理及实现

> (1) 先从数列中取出一个数作为基准数
> (2) 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
> (3) 再对左右区间重复第二步，直到各区间只有一个数

> 举例说明，有一个数组a[10]如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 21| 32| 43 |98 | 54| 45 | 23| 4	| 66 | 86 |

> 算法流程如下：
> (1) 取基准数x=a[0]=21，i=0，j=9。j从后向前，寻找第一个小于基准数的数字，然后与基准数进行替换，此时，i=0，j=7，x=21。过程如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| **21**| 32| 43 |98 | 54| 45 | 23| **4**	| 66 | 86 |

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| **4**| 32| 43 |98 | 54| 45 | 23| **21**	| 66 | 86 |

> (2) i从前向后，寻找第一个大于基准数的数字，然后与基准数进行替换，此时，i=1，j=7，x=21。过程如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4| **32**| 43 |98 | 54| 45 | 23| **21**	| 66 | 86 |

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | **21**| 43 |98 | 54| 45 | 23| **32**	| 66 | 86 |

> (3) j从后向前，寻找第一个小于基准数的数字，然后与基准数进行替换，此时，i=1，j=0，j<=i，过程结束，此时可以发现21前面的数字都比21小，后面数字都比21大，如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | **21**| 43 |98 | 54| 45 | 23| 32	| 66 | 86 |

然后a被分为了两个子区间[0,0]和[2,9]，[0,0]只有一个数字，不需要排序，因此下面对[2,9]重复上述过程
------------------------------------------------------------------------------------

> (1) 取基准数x=a[2]=43，i=2，j=9。j从后向前，寻找第一个小于基准数的数字，然后与基准数进行替换，此时，i=2，j=7，x=43。过程如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| **43** |98 | 54| 45 | 23| **32**	| 66 | 86 |

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| **32** |98 | 54| 45 | 23| **43**	| 66 | 86 |

> (2) i从前向后，寻找第一个大于基准数的数字，然后与基准数进行替换，此时，i=3，j=7，x=43。过程如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| 32 |**98** | 54| 45 | 23| **43**	| 66 | 86 |

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| 32 |**43** | 54| 45 | 23| **98**	| 66 | 86 |

> (3) j从后向前，寻找第一个小于基准数的数字，然后与基准数进行替换，此时，i=3，j=6，x=43。过程如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| 32 |**43** | 54| 45 | **23**| 98	| 66 | 86 |

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| 32 |**23** | 54| 45 | **43**| 98	| 66 | 86 |

> (4) i从前向后，寻找第一个大于基准数的数字，然后与基准数进行替换，此时，i=4，j=6，x=43。过程如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| 32 |23 | **54**| 45 | **43**| 98	| 66 | 86 |

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| 32 |23 | **43**| 45 | **54**| 98	| 66 | 86 |

> (5) j从后向前，寻找第一个小于基准数的数字，然后与基准数进行替换，i=4，j=3，j<=i，过程结束，此时可以发现43前面的数字都比43小，后面数字都比43大，如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| 4 | 21| 32 |23 | **43**| 45 | 54| 98	| 66 | 86 |

然后a被分为了两个子区间[2,3]和[5,9]，分别重复上述过程，即可得到排序后的结果。
------------------------------------------------------------------

> 代码如下：
```python
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
```

### 2. 快速排序实现TopK

```python
########## qsort ###########
def topk_qsort(num,left,right,k):

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
	print(num)

   '''
    此时数组被分割成两个部分  
    -->  array[left] ~ array[i-1] < array[left]
    -->  array[i+1] ~ array[right] > array[left]
    
    i与k比较，如果不等，则划分位置不是k，继续处理
    i<k，说明k在分划点后面部分
    i>k，说明k在分划点前面部分
    '''

	if i<k:
		return topk_qsort(num,i+1,right,k)
	if i>k:
		return topk_qsort(num,left,i-1,k)
	return num[:k]

########## main函数入口 ###########
if __name__ == '__main__':

	########## 列表 ###########
	num=[111,56,3,6,21,32,4,43,43,98,32,43,54,32,45,23,4,66,86,21]

	########## set left and right ###########
	left=0
	right=len(num)-1
	k=6

	########## print before sort ###########
	print(num)

	########## qsort ###########
	res=topk_qsort(num,left,right,k)
	print(res)

	########## print after sort ###########
	print(num)
```
