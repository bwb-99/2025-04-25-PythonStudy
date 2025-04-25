'''
    for: 횟수가 지정된 경우
    for 형식
      for 받는 변수 in 범위지정(리스트,튜플)
                             ----  ----
                             List   Map
                             []     () => 데이터베이스
              ('King',1000,....)
      범위지정 range(1,9)
      for(int i=1;i<10;i++)
      for i in range(1,10)
                       --- 제외 1~9 end-1
'''
for i in range(1,10): #증가식
    print(f"i={i}")
print("================")
list=["red","blue","yellow","black","green"]
for color in list:
    print(color)
print("================")
for _ in range(5): #5번 수행
    print("Hello")
print("================")
for i in range(1,10):
  for j in range(2,10):
      print(f"{j} * {i} = {i*j}",end="\t")
  print()
'''
 *
 **
 ***
 ****
 i  star(j) 
 1   1
 2   2
 3   3
 4   4
 
 for i in range(1,5):
  for j in range(1,i+1): 
 
 ****
 ***
 **
 *
i  star(j) 
 1   4
 2   3
 3   2
 4   1
 for i in range(1,5):
  for j in range(1,5-i+1): 
'''
for i in range(1,5):
  for j in range(1,i+1):
      print("*",end="")
  print("")
print("")
for i in range(1, 5):
  for j in range(1, 5-i+1):
      print("*", end="")
  print("")