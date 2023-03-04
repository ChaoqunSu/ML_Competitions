#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        这题太妙了,艹,如果暴力求解的话,那复杂度太高，如果能想到哈希,把四个数组分成两组,
        先求出其中一组(两个数组)的所有元素和,再用hash map记录下每个和值与其出现的次数,
        再用0-c-d去hash map里面去匹配即可
        """
        sum_dict12 = {}
        tar_num = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum12 = nums1[i] + nums2[j]
                if sum12 in sum_dict12.keys():
                    sum_dict12[sum12] += 1
                else:
                    sum_dict12[sum12] = 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                sum34 = nums3[i] + nums4[j]
                match_sum12 = 0-sum34
                if match_sum12 in sum_dict12.keys():
                    tar_num += sum_dict12[match_sum12]
        return tar_num



# @lc code=end

