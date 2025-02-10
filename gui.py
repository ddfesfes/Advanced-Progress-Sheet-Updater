import json
import os
from tkinter import *
from tkinter import ttk

import sv_ttk

class Gui:
    def __init__(self, **kwargs):
        # Read config and initialize Variables for Gui
        self.config = kwargs
        self.window = Tk()

        self.window.title("Advanced Progress Sheet Updater")
        self.window.geometry("890x400")
        self.path = StringVar()
        self.runs_to_average = IntVar()
        self.game = StringVar()

        self.preset_options = []
        for i in os.listdir('./presets/'):
            self.preset_options.append(str(i).replace('.json', ''))

        self.preset = StringVar()
        self.load_preset()  # Load preset on initialization
        self.preset.trace_add("write", self.update_config)  # Update config when preset changes

        self.notebook = ttk.Notebook(self.window)

        # Give start value to variables
        self.path.set(self.config["stats_path"])
        self.runs_to_average.set(int(self.config["num_of_runs_to_average"]))
        self.game.set(self.config["game"])
        self.game_options = ["Aimlab", "Kovaaks"]

        # 입력 길이 제한을 위한 validate 명령어 설정
        self.validate_length = self.window.register(self.validate_entry_length)

    def load_preset(self):
        if os.path.exists("preset.txt"):
            with open("preset.txt", "r", encoding='utf-8') as infile:
                preset_value = str(infile.read()).strip()
                self.preset.set(preset_value)  # Load preset value
                self.update_preset_options()  # Update options to include loaded preset

    def update_preset_options(self):
        # Ensure the loaded preset is in the options
        if self.preset.get() not in self.preset_options:
            self.preset_options.append(self.preset.get())
        self.preset.set(self.preset.get())  # Set the current preset

    def save_preset(self):
        with open("preset.txt", "w", encoding='utf-8') as outfile:
            outfile.write(str(self.preset.get()))

    def update_config(self, *args):
        selected_preset = self.preset.get()
        # 선택한 프리셋에 따라 config 업데이트
        data = json.load(open(f'./presets/{selected_preset}.json', 'r'))
        self.config = data

        self.runs_to_average.set(self.config["num_of_runs_to_average"])
        self.game.set(self.config["game"])

    def finished(self):
        self.config["stats_path"] = self.path.get()
        self.config["num_of_runs_to_average"] = self.runs_to_average.get()

        with open(f'./presets/{self.preset.get()}.json', "w") as outfile:
            json.dump(self.config, outfile, indent=4)
        self.save_preset()
        self.window.destroy()

    def validate_entry_length(self, new_value):
        # 최대 길이 설정 (예: 3)
        max_length = 3
        return len(new_value) <= max_length  # 입력 길이가 최대 길이 이하인지 확인

    def main(self):
        # Gui for advanced options
        advanced_padding_x = 25
        advanced_padding_y = 10
        self.window.configure(padx=20, pady=10)  # 전체 창에 패딩 추가

        advanced_frame = ttk.LabelFrame(self.window, text="Advanced Options", padding=(10, 10))  # ttk.LabelFrame으로 변경
        
        # Runs to average
        runs_to_average_frame = ttk.Frame(advanced_frame, padding=(10, 10))  # 패딩 추가
        runs_to_average_entry = ttk.Entry(
            runs_to_average_frame, 
            textvariable=self.runs_to_average, 
            width=3, 
            validate="key",  # 키 입력 시 검증
            validatecommand=(self.validate_length, '%P')  # 입력 값 검증
        )
        runs_to_average_label = ttk.Label(runs_to_average_frame, text="Number of runs to average")  # Label로 변경
        runs_to_average_entry.pack(side="left")
        runs_to_average_label.pack(side="left")
        runs_to_average_frame.grid(row="0", column="3", padx=advanced_padding_x, pady=advanced_padding_y)

        # 드롭다운 리스트 추가
        preset_frame = ttk.Frame(self.window, padding=(10, 10))  # 패딩 추가
        preset_label = ttk.Label(preset_frame, text="Select Preset: ")  # Label로 변경
        preset_dropdown = ttk.OptionMenu(preset_frame, self.preset, self.preset.get(), *self.preset_options)  # OptionMenu 생성
        preset_label.pack(side="left")
        preset_dropdown.pack(side="left")
        preset_frame.pack(fill="x")

        # Finished button
        finished_frame = ttk.Frame(self.window, padding=(10, 10))  # 패딩 추가
        finished_button = ttk.Button(finished_frame, command=self.finished, text="Finish")  # Button으로 변경
        finished_button.grid(row="1", column="1", columnspan="2")

        # Pack all frames
        self.notebook.pack(padx=10, pady=10)  # 노트북에 패딩 추가
        advanced_frame.pack(fill="x", padx=10, pady=10)  # 패딩 추가
        finished_frame.pack(padx=10, pady=10)  # 패딩 추가

        sv_ttk.set_theme("dark")

        # Run mainloop
        self.window.mainloop()
