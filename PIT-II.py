import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Função de login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "usuario" and password == "senha":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        login_frame.grid_forget()  # Remove o frame de login
        product_selection_frame.grid(row=0, column=0, padx=20, pady=20)  # Exibe o frame de produtos
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

# Função para adicionar produto à cesta
def add_to_cart():
    selected_product = product_listbox.curselection()
    if selected_product:
        product = products[selected_product[0]]
        cart_listbox.insert(tk.END, f"{product['name']} - R${product['price']}")
        total_price.set(total_price.get() + product['price'])

# Função para finalizar a compra
def checkout():
    payment_method = payment_var.get()
    if payment_method:
        messagebox.showinfo("Pagamento", f"Compra finalizada com {payment_method}!\nValor total: R${total_price.get():.2f}")
    else:
        messagebox.showerror("Pagamento", "Selecione um método de pagamento.")

# Criação da janela principal
root = tk.Tk()
root.title("Aplicativo de Login e Seleção de Produtos")

# Frame de login
login_frame = tk.Frame(root)
login_frame.grid(row=0, column=0, padx=20, pady=20)

label_username = tk.Label(login_frame, text="Nome de usuário")
label_username.grid(row=0, column=0, pady=5)

entry_username = tk.Entry(login_frame)
entry_username.grid(row=1, column=0, pady=5)

label_password = tk.Label(login_frame, text="Senha")
label_password.grid(row=2, column=0, pady=5)

entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=3, column=0, pady=5)

button_login = tk.Button(login_frame, text="Login", command=login)
button_login.grid(row=4, column=0, pady=20)

# Frame de seleção de produtos
product_selection_frame = tk.Frame(root)

products = [
    {"name": "Cupcake Morango", "price": 10.0, "image": "C:/Users/Arleilton/Documents/Python Scripts/.vscode/morango.jpeg"},
    {"name": "Cupcake Chocolate", "price": 20.0, "image":"C:/Users/Arleilton/Documents/Python Scripts/.vscode/chocolate.jpeg"},
    {"name": "Cupcake Creme", "price": 30.0, "image": "C:/Users/Arleilton/Documents/Python Scripts/.vscode/creme.jpeg"},
    {"name": "Cupcake Laranja", "price": 30.0, "image": "C:/Users/Arleilton/Documents/Python Scripts/.vscode/laranja.jpeg"},
    {"name": "Cupcake Limao Siciliano", "price": 30.0, "image": "C:/Users/Arleilton/Documents/Python Scripts/.vscode/Limao Siciliano.jpeg"},
]

product_listbox = tk.Listbox(product_selection_frame)
for product in products:
    product_listbox.insert(tk.END, f"{product['name']} - R${product['price']}")
product_listbox.grid(row=0, column=0, pady=5)

product_image_label = tk.Label(product_selection_frame)
product_image_label.grid(row=0, column=1, padx=10, pady=5)

def show_product_image(event):
    selected_product = product_listbox.curselection()
    if selected_product:
        product = products[selected_product[0]]
        image = Image.open(product["image"])
        image = image.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        product_image_label.config(image=photo)
        product_image_label.image = photo

product_listbox.bind("<<ListboxSelect>>", show_product_image)

button_add = tk.Button(product_selection_frame, text="Adicionar à Cesta", command=add_to_cart)
button_add.grid(row=1, column=0, pady=5)

cart_listbox = tk.Listbox(product_selection_frame)
cart_listbox.grid(row=1, column=1, pady=5)

# Frame de pagamento
payment_frame = tk.Frame(product_selection_frame)
payment_frame.grid(row=2, column=0, columnspan=2, pady=10)

payment_var = tk.StringVar()

label_payment = tk.Label(payment_frame, text="Selecione o método de pagamento")
label_payment.grid(row=0, column=0, pady=5)

radio_credit = tk.Radiobutton(payment_frame, text="Cartão de Crédito", variable=payment_var, value="Cartão de Crédito")
radio_credit.grid(row=1, column=0, pady=5)

radio_debit = tk.Radiobutton(payment_frame, text="Cartão de Débito", variable=payment_var, value="Cartão de Débito")
radio_debit.grid(row=2, column=0, pady=5)

radio_cash = tk.Radiobutton(payment_frame, text="Dinheiro", variable=payment_var, value="Dinheiro")
radio_cash.grid(row=3, column=0, pady=5)

button_checkout = tk.Button(payment_frame, text="Finalizar Compra", command=checkout)
button_checkout.grid(row=4, column=0, pady=20)

# Label para mostrar o valor total
total_price = tk.DoubleVar()
total_price.set(0.0)
label_total = tk.Label(product_selection_frame, textvariable=total_price)
label_total.grid(row=3, column=0, pady=5)

# Execução da janela
root.mainloop()
