height = [1.70, 1.62, 1.52, 1.85, 1.91, 1.42]
weight = [72, 64, 84, 80, 72, 70]

mean_height = sum(height) / len(height)
mean_weight = sum(weight) / len(weight)

X = []
Y = []
X_squared = []
Y_squared = []
XY = []

for i in range(len(height)):
    x = round(height[i] - mean_height, 4)
    y = round(weight[i] - mean_weight, 4)

    X.append(x)
    Y.append(y)

    X_squared.append(round(x ** 2, 4))
    Y_squared.append(round(y ** 2, 4))
    XY.append(round(x * y, 4))

print("X:", X)
print("Y:", Y)
print("X²:", X_squared)
print("Y²:", Y_squared)
print("XY:", XY)