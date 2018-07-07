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
> (1) 取基准数x=a[0]=21，i=0，j=9，j从后向前，寻找第一个小于基准数的数字，然后与基准数进行替换。此时，i=0，j=6，x=21，将a[j]与x交换，结果如下：

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| *21*| 32| 43 |98 | 54| 45 | 23| *4*	| 66 | 86 |

| 0 | 1 | 2  | 3 | 4 | 5  | 6 | 7 | 8  | 9 |
|:-:|:-:| :-:|:-:|:-:| :-:|:-:|:-:| :-:| :-:|
| *4*| 32| 43 |98 | 54| 45 | 23| *21*	| 66 | 86 |

### 2. 快速排序实现TopK
