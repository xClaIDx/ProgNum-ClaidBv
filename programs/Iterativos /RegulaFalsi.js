const readline = require('readline');
const math = require('mathjs');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function runRegulaFalsiConsole() {
    console.log("--- MÉTODO DE REGULA FALSI (FALSA POSICIÓN) ---");

    rl.question("Ingrese la función f(x): ", (funcStr) => {
        if (!funcStr) {
            console.log("No se ingresó ninguna función.");
            rl.close();
            return;
        }

        const cleanFuncStr = funcStr.replace(/\*\*/g, '^').replace(/\s/g, '');

        let f;
        try {
            const node = math.parse(cleanFuncStr);
            const code = node.compile();
            f = x => code.evaluate({ x: x });
        } catch (error) {
            console.error("Error en la sintaxis de la función:", error.message);
            rl.close();
            return;
        }

        rl.question("¿Desea aplicar el método de Regula Falsi? (s/n): ", (op) => {
            if (op.toLowerCase() !== 's') {
                console.log("No se aplicó el método de Regula Falsi.");
                rl.close();
                return;
            }

            rl.question("Ingrese el valor de a (extremo izquierdo): ", (a_input) => {
                rl.question("Ingrese el valor de b (extremo derecho): ", (b_input) => {
                    let a = parseFloat(a_input);
                    let b = parseFloat(b_input);

                    if (isNaN(a) || isNaN(b)) {
                        console.error("Error: Los valores del intervalo deben ser numéricos.");
                        rl.close();
                        return;
                    }

                    // Comprobación del cambio de signo, requisito fundamental del método
                    if (f(a) * f(b) > 0) {
                        console.warn("\nLa función no cambia de signo en el intervalo. No se puede aplicar el método.");
                        rl.close();
                        return;
                    }

                    const tol = 1e-6;
                    const max_iter = 100;
                    let converged = false;
                    let c_old = a; // Para calcular el error

                    console.log("\nIteración |      a      |      b      |      c      |    f(c)     |    Error");
                    console.log("--------------------------------------------------------------------------------");

                    for (let i = 1; i <= max_iter; i++) {
                        const fa = f(a);
                        const fb = f(b);

                        if (Math.abs(fa - fb) < 1e-15) {
                            console.log(`\nDivisión por cero inminente en la iteración ${i}. El método se detiene.`);
                            break;
                        }

                        // Fórmula de Regula Falsi
                        const c = b - (fb * (b - a)) / (fb - fa);
                        const fc = f(c);
                        const error = Math.abs(c - c_old);
                        c_old = c;

                        const iterText = i.toString().padStart(9);
                        const aText = a.toFixed(6).padStart(11);
                        const bText = b.toFixed(6).padStart(11);
                        const cText = c.toFixed(6).padStart(11);
                        const fcText = fc.toFixed(6).padStart(13);
                        const errorText = error.toExponential(2).padStart(10);
                        
                        console.log(`${iterText} | ${aText} | ${bText} | ${cText} | ${fcText} | ${errorText}`);

                        if (Math.abs(fc) < tol || error < tol) {
                            console.log(`\nRaíz aproximada encontrada: ${c.toFixed(6)}`);
                            console.log(`Iteraciones realizadas: ${i}`);
                            converged = true;
                            break;
                        }

                        // Actualización de los intervalos, manteniendo el cambio de signo
                        if (fa * fc < 0) {
                            b = c;
                        } else {
                            a = c;
                        }
                    }

                    if (!converged) {
                        console.warn(`\nNo se alcanzó la convergencia después de ${max_iter} iteraciones.`);
                    }

                    rl.close();
                });
            });
        });
    });
}

runRegulaFalsiConsole();