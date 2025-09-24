class GraficadoraTexto:
    def __init__(self, xmin=-20, xmax=20, ymin=-10, ymax=10):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.funciones = []  
    
    def preparar_expresion(self, expr: str) -> str:
        """Convierte la expresión escrita en forma amigable a Python"""
        expr = expr.replace(" ", "")       # quitar espacios
        expr = expr.replace("^", "**")     # potencia con ^
        if expr.startswith("x"):           # caso si empieza con x
            expr = "1*" + expr
        expr = expr.replace("-x", "-1*x")  # -x → -1*x
        expr = expr.replace("+x", "+1*x")  # +x → +1*x
        expr = expr.replace("x", "*x")     # 2x → 2*x
        expr = expr.replace("**x", "*x")   # corregir posibles duplicados
        return expr
    
    def agregar_funcion(self, expresion: str, simbolo: str):
        expr_preparada = self.preparar_expresion(expresion)
        self.funciones.append((expr_preparada, simbolo))
    
    def graficar(self):
        print("\nGráfico en Plano Cartesiano \n")
        for y in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x in range(self.xmin, self.xmax + 1):
                simbolo = " "
                intersecciones = []
                
                for expr, simb in self.funciones:
                    try:
                        y_eval = eval(expr, {"x": x})
                        if abs(y - y_eval) < 0.5:  # tolerancia
                            intersecciones.append(simb)
                    except:
                        pass
                
                if len(intersecciones) > 1:
                    simbolo = "#"  #Cruce
                elif len(intersecciones) == 1:
                    simbolo = intersecciones[0]
                elif x == 0 and y == 0:
                    simbolo = "+"  # origen
                elif x == 0:
                    simbolo = "|"  # eje Y
                elif y == 0:
                    simbolo = "-"  # eje X
                
                linea += simbolo
            print(linea)


if __name__ == "__main__":
    graf = GraficadoraTexto()
    
    # Pedimos dos funciones
    f1 = input("Ingrese la primera función (ejemplo: 2x+1): ")
    f2 = input("Ingrese la segunda función (ejemplo: -x+3): ")
    
    graf.agregar_funcion(f1, "*")
    graf.agregar_funcion(f2, "@")
    
    graf.graficar()