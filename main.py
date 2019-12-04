from sys import argv
from matplotlib.pylab import figure, plot, show, subplot, title, xlabel
from scipy import array, linspace, ndarray
from scipy.interpolate import CubicSpline
from sympy import sympify, SympifyError
from integral_equation import integral_equation
from utils import print_error


def get_limits():
    try:
        a, b = map(float, input('Insert the limits with the format "a, b": ').split(','))
    except ValueError:
        print_error('Error: Incorrect format, the limits should be a numbers and the separator should be a comma ",".')
    return a, b


def get_tabular_form_input():
    try:
        n = int(input('Insert the number of points of the function: '))
    except ValueError:
        print_error('Error: The number of points should be a integer.')
    print('Insert the points with the format "x, y":')
    x_points, y_points = [], []
    for _ in range(n):
        try:
            x, y = map(float, input().split(','))
        except ValueError:
            print_error('Error: Incorrect format, the points should be a numbers and the separator should be a comma ",".')
        x_points.append(x)
        y_points.append(y)
    return x_points, y_points


def get_tabular_form():
    x_points, y_points = get_tabular_form_input()
    function = CubicSpline(x_points, y_points)
    return function


def get_analytical_form(dim2 = False):
    try:
        function = sympify(input('Insert the analytical form of the function: '))
    except SympifyError:
        print_error('Error: It is not a recognizable function')
    if dim2:
        return lambda x, y: function.evalf(subs={'x': x, 'y': y})
    return lambda x: function.evalf(subs={'x': x})


def sample1():
    number_sample = 1
    print(f'Sample {number_sample}:')
    K = lambda x, y: sympify('1 + x * y').evalf(subs={'x': x, 'y': y})
    f = lambda x: sympify('1').evalf(subs={'x': x})
    a = -1
    b = 1
    print(f'K(x, y) = {K}')
    print(f'f(x) = {f}')
    print(f'Interval = [{a}, {b}]')
    solve1, cond1 = integral_equation(K, f, a, b, use_python_libs=True)
    solve2, cond2 = integral_equation(K, f, a, b, use_python_libs=False)
    x = linspace(a, b)
    y1 = solve1(x)
    y2 = solve2(x)
    figure(f'Sample {number_sample}')
    subplot(1, 2, 1)
    plot(x, y1)
    title(f'Sample {number_sample}: Use Python Libraries')
    xlabel(f'Matrix condition: {cond1}')
    subplot(1, 2, 2)
    plot(x, y2)
    title(f'Sample {number_sample}: NO use Python Libraries')
    xlabel(f'Matrix condition: {cond2}')
    show()


def sample2():
    number_sample = 2
    print(f'Sample {number_sample}:')
    K = lambda x, y: sympify('1 + x * y').evalf(subs={'x': x, 'y': y})
    f = lambda x: sympify('2 * x / 3').evalf(subs={'x': x})
    a = -1
    b = 1
    print(f'K(x, y) = {K}')
    print(f'f(x) = {f}')
    print(f'Interval = [{a}, {b}]')
    solve1, cond1 = integral_equation(K, f, a, b, use_python_libs=True)
    solve2, cond2 = integral_equation(K, f, a, b, use_python_libs=False)
    x = linspace(a, b)
    y1 = solve1(x)
    y2 = solve2(x)
    figure(f'Sample {number_sample}')
    subplot(1, 2, 1)
    plot(x, y1)
    title(f'Sample {number_sample}: Use Python Libraries')
    xlabel(f'Matrix condition: {cond1}')
    subplot(1, 2, 2)
    plot(x, y2)
    title(f'Sample {number_sample}: NO use Python Libraries')
    xlabel(f'Matrix condition: {cond2}')
    show()


if __name__ == "__main__":
    try:
        if len(argv) > 1 and argv[1] == 'samples':
            sample1()
            sample2()
            exit()
        option = int(input('Insert 1 if use Python libraries or 2 if no: '))
        if option != 1 and option != 2:
            print_error('Error: The number of option should be 1 or 2.')
        use_python_libs = option == 1
        option = int(input('Insert 1 if the function K is in the form of a table or 2 if it is in analytical form: '))
        if option != 1 and option != 2:
            print_error('Error: The number of option should be 1 or 2.')
        K = get_tabular_form() if option == 1 else get_analytical_form(True)
        option = int(input('Insert 1 if the function f is in the form of a table or 2 if it is in analytical form: '))
        if option != 1 and option != 2:
            print_error('Error: The number of option should be 1 or 2.')
        f = get_tabular_form() if option == 1 else get_analytical_form()
        a, b = get_limits()
        solve, cond = integral_equation(K, f, a, b, use_python_libs=use_python_libs)
        x = linspace(a, b)
        y = solve(x)
        plot(x, y)
        title(f'Matrix condition: {cond}')
        show()
    except ValueError:
        print_error('Error: The number of option should be a integer.')
