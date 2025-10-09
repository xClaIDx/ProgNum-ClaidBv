import sympy as sp

class NewtonRaphson:
    def __init__(self, fx_str, iter_max=100, tol=1e-6):
        self.x = sp.Symbol('x')
        self.f_expr = sp.sympify(fx_str)
        self.df_expr = sp.diff(self.f_expr, self.x)
        self.f = sp.lambdify(self.x, self.f_expr, 'math')
        self.df = sp.lambdify(self.x, self.df_expr, 'math')
        self.iter_max = iter_max
        self.tol = tol
        self.iteraciones = []

    def newton(self, x0):
        # Ajustar x0 si derivada es cero
        delta = 0.1
        while self.df(x0) == 0:
            x0 += delta

        self.iteraciones = []
        for i in range(1, self.iter_max + 1):
            f_val = self.f(x0)
            df_val = self.df(x0)
            if df_val == 0:
                print(f"Derivada cero en x = {x0}. Interrumpiendo.")
                break
            x1 = x0 - f_val / df_val
            error = abs(x1 - x0)
            self.iteraciones.append((i, x0, f_val, df_val, x1, error))
            if error < self.tol:
                break
            x0 = x1
        return x0

    def mostrar_tabla(self):
        print("\nIteración |    x_n     |   f(x_n)    |   f'(x_n)   |   x_(n+1)   |   Error")
        print("-------------------------------------------------------------------------")
        for it in self.iteraciones:
            print(f"{it[0]:9d} | {it[1]:10.6f} | {it[2]:11.6f} | {it[3]:11.6f} | {it[4]:11.6f} | {it[5]:10.6e}")
        if self.iteraciones:
            print(f"\nRaíz aproximada: {self.iteraciones[-1][4]:.10f}")
            print(f"Número de iteraciones: {len(self.iteraciones)}")

# --- Entrada de usuario ---
fx_str = input("Ingrese f(x): ")
x0_input = input("Ingrese el valor inicial x0 (Enter para usar x0=0): ")
x0 = float(x0_input) if x0_input.strip() != "" else 0

nr = NewtonRaphson(fx_str)
raiz = nr.newton(x0)
nr.mostrar_tabla()