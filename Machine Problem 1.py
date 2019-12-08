# Machine Problem 1

# import code for plotting
import matplotlib.pyplot as plt

# define the given piecewise function
def f(n):
    if n <= 9:
        return n * n - 7
    return f(n - 10)

if __name__ == '__main__':
    # looping the given function from 0 to 99
    x = []
    y = []
    for i in range(1, 100):
        x.append(i)
        y.append(f(i))

    # printing the x and y values for output
    print(x)
    print(y)
    
    # plotting the points
    plt.plot(x, y)

    # naming the x axis in the graph
    plt.xlabel('x - axis')
    # naming the y axis in the graph
    plt.ylabel('y - axis')

    # naming title for the graph
    plt.title('The Graph for f(n) ')

    # showing the plot
    plt.show()
# end of code