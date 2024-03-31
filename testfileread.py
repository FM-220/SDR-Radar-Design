import numpy
import matplotlib
import matplotlib.pyplot as plt




f = numpy.fromfile(open("C:/testfile/testfile"), dtype=numpy.float32)
numpy.savetxt("C:/testfile/testfileoutput.txt",f)

filename = "C:/testfile/testfileoutput.txt"  # 文件路径
num_lines = 0
with open(filename, 'r') as file:
    for line in file:
        num_lines += 1


numbers = []
with open(filename, 'r') as file:
    for line in file:
        # 将每行的内容转换为浮点数（或整数）并添加到列表中
        numbers.append(float(line.strip()))

# numberlength = len(numbers)
# index = 0
# newnumber = []
# while index<numberlength:
#     newnumber.append(numbers[index])
#     index += 1200

numberlength = len(numbers)
index = 0
newnumber = []
while index<numberlength:
    newnumber.append(numbers[index])
    index += 1

newnewnumber = newnumber#[:1000000]
# 绘制数字
plt.scatter(range(len(newnewnumber)), newnewnumber)
plt.title("File Numbers Scatter Plot")
plt.xlabel("Index")
plt.ylabel("Number")
plt.show()

# t = numpy.linspace(0, 999999 ,1000000, dtype=int)


# t = numpy.linspace(0, len(newnewnumber)-1 ,len(newnewnumber), dtype=int)
#
# yf = numpy.fft.fft(newnewnumber)
# N = len(t)  # 样本数量
# T = t[1] - t[0]  # 样本间隔
# xf = numpy.fft.fftfreq(N, T)
#
# # 步骤 3: 绘制傅里叶变换结果
# plt.figure(figsize=(100, 40))
# plt.plot(xf, numpy.abs(yf))
# plt.title("FFT of Signal")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.grid()
# plt.show()

