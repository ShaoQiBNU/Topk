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

### 1. 堆的概念及排序
### 2. 堆实现TopK
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
