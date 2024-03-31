import random
def monte_carlo_estimation():
    area_circle = 1
    area_square = 1
    pi = 0
    for z in range(10000000):
        x = random.uniform(0, 2)
        y = random.uniform(0, 2)
        in_circle = pow((x-1), 2) + pow((y-1), 2) <= 1
        if in_circle:
            area_circle += 1
        area_square += 1
        pi = 4 * (area_circle / area_square)
    print("Estimate: " + str(pi))
if __name__ == '__main__':
    monte_carlo_estimation()

















# def fact(n):
#     r=1
#     for i in range(n, 0, -1):
#         r*=i
#     return r

# def calc(res, n):
#     if n==6:
#         return res
#     return res/((2*n-1)+n**2/calc(res, n+1))

# print(calc(4, 1))
# # (2*i-1)+i**2
# # pi=4/1
# # print(pi)
# # pi=4/(1+pow(1,2))
# # print(pi)
# # pi=4/(1+pow(1,2)/(3+pow(2,2)))
# # print(pi)
# # pi=4/(1+pow(1,2)/(3+pow(2,2)/(5+pow(3,2))))
# # print(pi)
# # pi=4/(1+pow(1,2)/(3+pow(2,2)/(5+pow(3,2)/(7+pow(4,2)))))
# # print(pi)
# # pi=4/(1+pow(1,2)/(3+pow(2,2)/(5+pow(3,2)/(7+pow(4,2)/(9+pow(5,2))))))
# # print(pi)
# # pi=4/(1+pow(1,2)/(3+pow(2,2)/(5+pow(3,2)/(7+pow(4,2)/(9+pow(5,2)/(11+pow(6,2)))))))
# # print(pi)
# # pi=4/(1+pow(1,2)/(3+pow(2,2)/(5+pow(3,2)/(7+pow(4,2)/(9+pow(5,2)/(11+pow(6,2)/(13+pow(7,2))))))))
# # print(pi)