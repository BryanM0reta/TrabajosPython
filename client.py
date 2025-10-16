import socket
import tkinter as tk
from tkinter import messagebox

def send_request():
    # Obtener los valores de los campos de entrada
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    op = operation_var.get()
    
    # Validar que los campos no estén vacíos
    if not num1 or not num2 or not op:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    
    # Formatear la solicitud según el protocolo
    request = f"{num1},{num2},{op}"
    
    try:
        # Conectar al servidor y enviar la solicitud
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('172.17.144.146', 5000))  # Tu IP como servidor
        client.send(request.encode('utf-8'))
        
        # Recibir y mostrar la respuesta
        response = client.recv(1024).decode('utf-8')
        result_label.config(text=f"Respuesta: {response}")
        
        # Cerrar la conexión si se envía "quit" (opcional aquí, manejado por el servidor)
        if request.lower() == 'quit':
            client.close()
            root.quit()
        else:
            client.close()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Cliente de Cálculo")

# Etiquetas y campos de entrada
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Operación:").grid(row=2, column=0, padx=5, pady=5)
operation_var = tk.StringVar(value="add")
tk.OptionMenu(root, operation_var, "add", "sub", "mul", "div").grid(row=2, column=1, padx=5, pady=5)

# Botón para enviar la solicitud
send_button = tk.Button(root, text="Calcular", command=send_request)
send_button.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="Respuesta: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Botón para salir
quit_button = tk.Button(root, text="Salir", command=lambda: [root.quit(), send_request() if messagebox.askyesno("Salir", "¿Enviar 'quit' al servidor?") else None])
quit_button.grid(row=5, column=0, columnspan=2, pady=5)

# Iniciar la aplicación
root.mainloop()
import socket
import tkinter as tk
from tkinter import ttk, messagebox

class MathClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente de Cálculo")
        self.root.geometry("400x300")
        self.root.configure(bg="#ecf0f1")

        # Estilo profesional
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10), padding=6)
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TFrame", background="#ecf0f1")

        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill="both", expand=True)

        # Título
        title_label = ttk.Label(main_frame, text="Calculadora Cliente", font=("Helvetica", 14, "bold"), foreground="#2c3e50")
        title_label.pack(pady=10)

        # Campos de entrada
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = ttk.Entry(input_frame, width=15)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = ttk.Entry(input_frame, width=15)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Operación:").grid(row=2, column=0, padx=5, pady=5)
        self.operation_var = tk.StringVar(value="add")
        operation_menu = ttk.OptionMenu(input_frame, self.operation_var, "add", "add", "sub", "mul", "div")
        operation_menu.grid(row=2, column=1, padx=5, pady=5)

        # Botón de cálculo
        calc_button = ttk.Button(main_frame, text="Calcular", command=self.send_request, style="TButton")
        calc_button.pack(pady=10)

        # Área de resultados
        self.result_label = ttk.Label(main_frame, text="Respuesta: ", font=("Helvetica", 10), foreground="#34495e")
        self.result_label.pack(pady=5)

        # Botón de salir
        quit_button = ttk.Button(main_frame, text="Salir", command=self.on_closing, style="TButton")
        quit_button.pack(pady=5)

    def send_request(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        op = self.operation_var.get()

        if not num1 or not num2 or not op:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        request = f"{num1},{num2},{op}"
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('172.17.129.168', 5000))
            client.send(request.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            self.result_label.config(text=f"Respuesta: {response}")
            if request.lower() == 'quit':
                client.close()
                self.root.quit()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")
        finally:
            client.close()

    def on_closing(self):
        if messagebox.askyesno("Salir", "¿Enviar 'quit' al servidor antes de salir?"):
            self.send_request()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathClientApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
