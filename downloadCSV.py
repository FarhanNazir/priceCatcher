import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import customtkinter
from threading import Thread
from CTkListbox import *

def download_csv(url, save_path, progress_bar):
    chunk_size = 8192
    bars_completed = 0
    update_interval = 5  # Update progress bar after every 5 chunks

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            file.write(chunk)
            bars_completed += len(chunk)

            if bars_completed % (chunk_size * update_interval) == 0:
                progress_percentage = (bars_completed / total_size) * 100
                progress_bar["value"] = progress_percentage
                root.update_idletasks()  # Update the tkinter window to show the progress

    # Set the progress bar to 100% after the download is complete
    progress_bar["value"] = 100
    root.update_idletasks()  # Update the tkinter window

    return True


def on_download():
    selected_dates = listbox.curselection()  # Get the selected indices from the listbox

    total_files = len(selected_dates)
    progress_bar["maximum"] = total_files  # Set the maximum value for the progress bar
    progress_bar["value"] = 0  # Reset progress bar

    def download_files():
        for date_index in selected_dates:
            date = listbox.get(date_index)
            url = f"https://storage.data.gov.my/pricecatcher/pricecatcher_{date}.csv"
            filename = f"pricecatcher_{date}.csv"
            success = download_csv(url, filename, progress_bar)
            if success:
                root.after(0, lambda: status_label.configure(text=f"Downloaded file(s) for {date} successfully."))
            else:
                messagebox.showerror("Error", f"Failed to download file for {date}.")
                break

    # Start a new thread for downloading files
    download_thread = Thread(target=download_files)
    download_thread.start()


def show_value(selected_option):
    print(selected_option)



# GUI 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("CSV Downloader")
root.geometry("480x480")

listbox_label = customtkinter.CTkLabel(root, text="Select dates:")
listbox_label.pack(padx=5, pady=5)
listbox = CTkListbox(root, command=show_value, multiple_selection=True)
listbox.pack(fill="both", expand=True, padx=10, pady=5)

listbox.insert(0, "2022-01")
listbox.insert(1, "2022-02")
listbox.insert(2, "2022-03")
listbox.insert(3, "2022-04")
listbox.insert(4, "2022-05")
listbox.insert(5, "2022-06")
listbox.insert(6, "2022-07")
listbox.insert(7, "2022-08")
listbox.insert(8, "2022-09")
listbox.insert(9, "2022-10")
listbox.insert(10, "2022-11")
listbox.insert(11, "2022-12")
listbox.insert(12, "2023-01")
listbox.insert(13, "2023-02")
listbox.insert(14, "2023-03")
listbox.insert(15, "2023-04")
listbox.insert(16, "2023-05")
listbox.insert(17, "2023-06")
listbox.insert(18, "2023-07")
listbox.insert(19, "2023-08")
listbox.insert(20, "2023-09")
listbox.insert(21, "2023-10")
listbox.insert(22, "2023-11")
listbox.insert("END", "2023-12")


# Download button
download_button = customtkinter.CTkButton(root, text="Download", command=on_download)
download_button.pack()
# Progress bar
progress_bar = ttk.Progressbar(
    root, orient="horizontal", length=200, mode="determinate"
)
progress_bar.pack(pady=5)

# Status label
status_label = customtkinter.CTkLabel(root, text="")
status_label.pack()

root.mainloop()
