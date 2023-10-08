import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from threading import Thread


def download_csv(url, save_path, progress_bar):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    chunk_size = 8192
    bars_completed = 0

    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            file.write(chunk)
            bars_completed += len(chunk)

            progress_percentage = (bars_completed / total_size) * 100

            progress_bar["value"] = progress_percentage
            root.update_idletasks()  # Update the tkinter window to show the progress

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
                status_label.config(
                    text=f"Downloaded  file(s) for {date} successfully."
                )
            else:
                messagebox.showerror(
                    "Error",
                    f"Failed to download file  for {date}.",
                )
                break

    # Start a new thread for downloading files
    download_thread = Thread(target=download_files)
    download_thread.start()


root = tk.Tk()
root.title("CSV Downloader")

# Listbox for selecting dates
listbox_label = tk.Label(root, text="Select dates:")
listbox_label.pack()
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
options = [
    "2022-01",
    "2022-02",
    "2022-03",
    "2022-04",
    "2022-05",
    "2022-06",
    "2022-07",
    "2022-08",
    "2022-09",
    "2022-10",
    "2022-11",
    "2022-12",
]  # Add your date options here
for option in options:
    listbox.insert(tk.END, option)
listbox.pack()


# Download button
download_button = tk.Button(root, text="Download", command=on_download)
download_button.pack()

# Progress bar
progress_bar = ttk.Progressbar(
    root, orient="horizontal", length=200, mode="determinate"
)
progress_bar.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
