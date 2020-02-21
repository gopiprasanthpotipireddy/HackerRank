def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    #step=int(n/k)
    for i in range(0,len(string),k):
        t_i=string[i:i+k]
        #strip t_i to u_i
        u_i=""
        temp=[]
        for c in range(len(t_i)):
            
            if t_i[c] not in temp:
                u_i=u_i+t_i[c]
            temp.append(t_i[c])
        print(u_i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)