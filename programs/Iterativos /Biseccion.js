
const readline = require('readline');
const math = require('mathjs'); 

// Crear la interfaz para leer y escribir en la consola
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function runBisectionConsole() {
   
    rl.question("Ingrese la función f(x): ", (funcStr) => {
        if (!funcStr) {
            console.log("No se ingresó ninguna función.");
            rl.close();
            return;
        }

        // Se eliminan todos los espacios de la entrada del usuario.
        const cleanFuncStr = funcStr.replace(/\*\*/g, '^').replace(/\s/g, '');

      
        let f;
        try {
            
            const node = math.parse(cleanFuncStr);
            const code = node.compile();
            f = x => code.evaluate({ x: x });
        } catch (error) {
            console.error("Error en la función ingresada:", error.message);
            rl.close();
            return;
        }

      
        rl.question("¿Desea encontrar una raíz con el método de Bisección? (s/n): ", (op) => {
            if (op.toLowerCase() !== 's') {
                console.log("No se aplicó el método de Bisección.");
                rl.close();
                return;
            }

           
            rl.question("Ingrese el extremo izquierdo del intervalo (a): ", (a_input) => {
                rl.question("Ingrese el extremo derecho del intervalo (b): ", (b_input) => {
                    const a_start = parseFloat(a_input);
                    const b_start = parseFloat(b_input);

                    if (isNaN(a_start) || isNaN(b_start)) {
                        console.error("Error: Los valores del intervalo deben ser numéricos.");
                        rl.close();
                        return;
                    }

                    if (f(a_start) * f(b_start) > 0) {
                        console.warn("\n No hay cambio de signo en el intervalo. Intente con otro.");
                        rl.close();
                        return;
                    }

                   
                    const tol = 1e-6;
                    const max_iter = 100;
                    let a = a_start;
                    let b = b_start;
                    let converged = false;

                    console.log("\nIteración |     a       |      b       |      c       |    f(c)     |   Error");
                    console.log("-------------------------------------------------------------------------");

                    for (let i = 1; i <= max_iter; i++) {
                        const c = (a + b) / 2;
                        const fc = f(c);
                        const error = Math.abs(b - a) / 2;

                        const iterText = i.toString().padStart(9);
                        const aText = a.toFixed(6).padStart(12);
                        const bText = b.toFixed(6).padStart(12);
                        const cText = c.toFixed(6).padStart(12);
                        const fcText = fc.toFixed(6).padStart(12);
                        const errorText = error.toFixed(6).padStart(12);
                        console.log(`${iterText} | ${aText} | ${bText} | ${cText} | ${fcText} | ${errorText}`);

                        if (Math.abs(fc) < tol || error < tol) {
                            console.log(`\nRaíz aproximada encontrada: ${c.toFixed(6)}`);
                            console.log(`   Iteraciones realizadas: ${i}`);
                            converged = true;
                            break;
                        }

                        if (f(a) * fc < 0) {
                            b = c;
                        } else {
                            a = c;
                        }
                    }

                    if (!converged) {
                        console.warn(`\n No se alcanzó la convergencia después de ${max_iter} iteraciones.`);
                    }

                    rl.close(); 
                });
            });
        });
    });
}

runBisectionConsole();