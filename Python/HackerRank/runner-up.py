# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input("Enter the number of elements to find runner-up: "))
    arr = map(int, input("Enter {} elements: ".format(n)).split())
    
    arr = list(set(arr))
    arr.sort(reverse=True)


    print(arr[1])