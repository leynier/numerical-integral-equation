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


if __name__ == "__main__":
    try:
        if len(argv) > 1 and argv[1] == 'samples':
            print('Sample 1:')
            K1 = lambda x, y: sympify('1 + x * y').evalf(subs={'x': x, 'y': y})
            f1 = lambda x: sympify('1').evalf(subs={'x': x})
            a1 = -1
            b1 = 1
            print(f'K(x, y) = {K1}')
            print(f'f(x) = {f1}')
            print(f'Interval = [{a1}, {b1}]')
            solve1_1, cond1_1 = integral_equation(K1, f1, a1, b1, use_python_libs=True)
            solve1_2, cond1_2 = integral_equation(K1, f1, a1, b1, use_python_libs=False)
            x1 = linspace(a1, b1)
            y1_1 = solve1_1(x1)
            y1_2 = solve1_2(x1)
            figure('Sample 1')
            subplot(1, 2, 1)
            plot(x1, y1_1)
            title(f'Sample 1: Use Python Libraries')
            xlabel(f'Matrix condition: {cond1_1}')
            subplot(1, 2, 2)
            plot(x1, y1_2)
            title(f'Sample 1: NO use Python Libraries')
            xlabel(f'Matrix condition: {cond1_2}')
            show()
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
