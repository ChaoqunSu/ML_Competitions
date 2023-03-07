#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
#时间复杂度：O(nlogk)
#空间复杂度：O(n)
import heapq
# 注意,heapq是专门用来实现小顶堆的库
# heapq中创建堆的方法有两种:
# heappush(heap, num),先建一个空堆,然后将数据一个个地添加到堆中,每添加一个数据,heap都满足小顶堆的特性
# heapify(array),直接将数据列表调整成一个小顶堆

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        以后解决问题要把核心问题列一列,列着列着就会了,而且思路会更清晰
        1. 关于存频次,很容易可以想到用哈希map,元素-频次
        2. 然后就是怎样才能找出topk高频次,然后拿出对应的元素,这里主要是前面存的时候是用字典存的
        而正常的排序需要在数组(向量)上进行,那可能就不适合用普通的排序了,所以就是第二步没想好怎么解决
        使用快排要将map转换为vector的结构,然后对整个数组进行排序,而这种场景下,其实只需维护k个有序的序列即可
        所以使用优先级队列是最优的。
            代码随想录用的是大顶堆/小顶堆的概念(即优先级队列)来实现部分频率的排序
            堆就是一颗完全二叉树,树中每个结点的值都不小于（或不大于）其左右孩子的值,如果父亲结点是大于等于
        左右孩子就是大顶堆,小于等于左右孩子就是小顶堆。大顶堆的堆头是最大元素。这里我们用小顶堆,因为要统计
        最大前k个元素,只有小顶堆每次将最小的元素弹出,最后小顶堆里积累的才是前k个最大元素
        1.借助 哈希表 来建立数字和其出现次数的映射，遍历一遍数组统计元素的频率
        2.维护一个元素数目为k的最小堆
        3.每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
        4.如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
        5.最终,堆中的k个元素即为前k个高频元素
        """
        # hash 图存元素-频次
        times_dict = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in times_dict.keys():
                times_dict[nums[i]] = 1
            else:
                times_dict[nums[i]] += 1
        
        # 对频率排序,定义一个小顶堆,大小为k
        pri_que = []
        # 用固定大小为k的小顶堆,扫描所有频率的数值
        for key, freq in times_dict.items():
            heapq.heappush(pri_que, (freq, key))
            # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        
        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0]*k
        # 编程时很容易错的思想,这里k-1是取得到的,-1是取不到的,所以是从k-1降序到0
        for i in range(k-1, -1, -1):
            # 因为存在堆里的是pair值对,所以这里的[1]指的是key对应的value(即频率)
            result[i] = heapq.heappop(pri_que)[1]
        return result

        


# @lc code=end

