import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def get_amazon_product_price(product_name):
    base_url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_links = soup.find_all("a", {"class": "a-link-normal a-text-normal"})
        if product_links:
            first_product_link = product_links[0]['href']
            product_url = f"https://www.amazon.com{first_product_link}"
            
            product_response = requests.get(product_url, headers=headers)
            if product_response.status_code == 200:
                product_soup = BeautifulSoup(product_response.content, 'html.parser')
                price_element = product_soup.find("span", {"id": "priceblock_ourprice"})
                
                if price_element:
                    price = price_element.get_text()
                    return price.strip()
                else:
                    return "Price not found"
            else:
                return "Product page request failed"
        else:
            return "No product found"
    else:
        return "Search page request failed"

def search_button_clicked():
    product_name = product_entry.get()
    if product_name:
        price = get_amazon_product_price(product_name)
        result_label.config(text=f"The best price on Amazon for '{product_name}' is: {price}")
    else:
        messagebox.showinfo("Error", "Please enter a product name.")

def close_button_clicked():
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Product Price Search")

    # Create and place widgets
    product_label = tk.Label(root, text="Enter Product Name:")
    product_label.pack(pady=10)

    product_entry = tk.Entry(root)
    product_entry.pack()

    search_button = tk.Button(root, text="Search", command=search_button_clicked)
    search_button.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack()

    close_button = tk.Button(root, text="Close", command=close_button_clicked)
    close_button.pack(pady=10)

    # Run the GUI event loop
    root.mainloop()
