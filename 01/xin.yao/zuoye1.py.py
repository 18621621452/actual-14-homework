 arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45] 
 max_num1 = 0
 max_num2 = 0
 for i in arr:
 	if max_num1 < i:
 		max_num1 = i
 for j in arr:
 	if max_num2 < j and max_num2 <= max_num1:
 		max_num2 = j
 		
print max_num