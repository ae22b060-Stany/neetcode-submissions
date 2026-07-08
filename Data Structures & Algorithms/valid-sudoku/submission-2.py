class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # go through every row
        # go through every column
        # go through every sub box

        n = len(board[0])


        for row_ind in range(n):
            row = board[row_ind][:]

            row = sorted(row)
            for i in range(len(row)-1):
                if row[i]== '.':
                    continue
                if row[i+1] == row[i]:
                    return False
        
        for col_ind in range(n):
            col = [row[col_ind] for row in board]

            col = sorted(col)
            for i in range(len(col)-1):
                if col[i]== '.':
                    continue
                if col[i+1] == col[i]:
                    return False

        sub_ind_r = 0 
        sub_ind_c = 0
        

        while sub_ind_r <9 and sub_ind_c < 9:
            subbox_arr = []
            subbox = [row[sub_ind_c:sub_ind_c+3]
                    for row in board[sub_ind_r:sub_ind_r+3]]           
            print('SUBBOX IS : ',subbox)
            for i_n in range(3):
                for j_n in range(3):
                        print(i_n,j_n)
  
                        subbox_arr.append(subbox[i_n][j_n])
            print('One box done')
            subbox_arr = sorted(subbox_arr)
            print(len(subbox_arr))
            for i in range(len(subbox_arr)-1):
                if subbox_arr[i]== '.':
                    continue
                if subbox_arr[i+1] == subbox_arr[i]:
                    return False

            sub_ind_c = sub_ind_c + 3
            print('sub_ind_c is  ', sub_ind_c)
            if sub_ind_c > 8 :
                sub_ind_c = 0
                sub_ind_r += 3
                print('sub_ind_r is now ', sub_ind_r)
                print('sub_ind_c is  ', sub_ind_c)
        return True
            

            