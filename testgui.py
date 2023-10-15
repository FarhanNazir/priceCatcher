
import tkinter
import customtkinter
from functools import partial

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")

categories = ["Consumer Prices: Core CPI", "Consumer Prices: CPI by State", "Consumer Prices: Headline CPI", "Consumer Prices: PriceCatcher" , "Data Dictionaries: Economy", "Demography: Population", "Economic Indicators: Economy-Wide", "Economy: Household Income & Expenditure", "External Trade: Exchange Rates", "Gross Domestic Product: GDP by State", "Gross Domestic Product: National GDP", "Industrial Production: IPI", "Labour Force: Annual", "Labour Force: Monthly", "Wholesale and Retail Trade: IOWRT"
]


class App(customtkinter.CTk):

    frames = {}
    current = None
    bg = ""


    def __init__(self):
        super().__init__()
        self.bg = self.cget("fg_color")
        self.num_of_frames = 0
        # self.state('withdraw')
        self.title("CSV Downloader")

        # screen size
        self.geometry("800x600")

        # root!
        main_container = customtkinter.CTkFrame(self, corner_radius=8, fg_color=self.bg)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=8, pady=8)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkScrollableFrame(main_container, width=280, corner_radius=8, fg_color=self.bg)

        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=18, pady=10)



        # right side panel -> to show the frame1 or frame 2, or ... frame + n where n <= 5
        self.right_side_panel = customtkinter.CTkFrame(main_container, corner_radius=8, fg_color="#212121")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        self.right_side_panel.configure(border_width = 1)
        self.right_side_panel.configure(border_color = "#323232")
        [self.create_nav(self.left_side_panel, f"frame{i+1}") for i, category in enumerate(categories)]


    def color_by_id(self, id):
        match id:
            case 1:
                return "blue"
            case 2:
                return "green"
            case 3:
                return "orange"
            case 4:
                return "purple"
            case 5:
                return "grey" 
            case _:
                return "red"


    def frame_selector_bt(self, parent, frame_id):                  
        label = customtkinter.CTkLabel(parent, text="download")
        label.grid(row=0, column=0)

 

        # create frame 
        bt_frame = customtkinter.CTkButton(parent, width=260)
        # style frame
        bt_frame.configure(height = 40)
        # creates a text label
        bt_frame.configure(text = categories[self.num_of_frames])
        # bt_frame.configure(command =  partial( self.toggle_frame_by_id,  "frame" + str(self.num_of_frames + 1) ) )
        # set layout
        bt_frame.grid(pady = 3, row=self.num_of_frames + 1, column=0)
        # update state
        self.num_of_frames = self.num_of_frames + 1


    def create_nav(self, parent, frame_id):
        self.frame_selector_bt(parent, frame_id)
        




a = App()
a.mainloop()
