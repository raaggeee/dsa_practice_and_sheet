def threeSum(arr):
	res=[]
	for i in range(len(arr)):
		j=i+1
		k=j+1
		print(i,j,k)
		if k==len(arr):
			break

		if arr[i]+arr[j]+arr[k] ==0:
			res.append([arr[i], arr[j], arr[k]])

	return res

print(threeSum([-1,0,1,2,-1,-4]))
