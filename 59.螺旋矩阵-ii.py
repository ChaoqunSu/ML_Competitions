#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int):
        # 一定要坚持左闭右开的原则，忌讳来回倒腾，否则很容易乱
        # 每一圈的规律是类似的，一圈一圈来
        # 对于每一圈来说，拆解出来的每条边都该是一样的，都坚持左闭右开原则
        # 按照，上边、右边、下边、左边，一个一个来，整体是一个二维坐标系(i,j)
        # 先定义一些必要的变量，多少圈(n/2圈)、起始坐标(0,0)，数，控制边的长度(offset)
        count = 1
        loop = int(n / 2)
        start_x, start_y = 0, 0
        offset = 1
        g_ls = [[0]*n for _ in range(n)]
        for _ in range(loop):
            # 上边, i=start_x, j:start_y->n-offset
            for j in range(start_y, n-offset):
                g_ls[start_x][j] = count
                count += 1 
            j += 1   
            # 右边, i:start_x->n-offset, j:n-offset
            for i in range(start_x, n-offset):
                g_ls[i][j] = count
                count += 1
            # 下边, i=n-offset, j:n-offset->start_y+1
            i += 1
            for j in range(n-offset, start_y, -1):
                g_ls[i][j] = count
                count += 1
            # 左边, i:n-offset->start_x+1, j:start_y
            j -= 1
            for i in range(n-offset, start_x, -1):
                g_ls[i][j] = count
                count += 1
            # 下一圈变起点
            start_x += 1
            start_y += 1
            # 内圈的offset增加
            offset += 1
        # 若n是奇数，最内核那个是一个落单的数而不是圈，直接赋值
        if n % 2 != 0:
            g_ls[loop][loop] = n*n
        
        return g_ls
# @lc code=end

