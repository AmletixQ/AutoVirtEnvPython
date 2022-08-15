from pathlib import Path
import tkinter
import tkinter.messagebox
import os
import subprocess

class Application:
    def __init__(self):

        self.folder_path = "/media/amletixq/AmletixQ-fileSys/amletixq/Personal Room/Программирование/pythonProject/"
        self.folder_path_lite = "/amletixq/Personal Room/Программирование/pythonProject/"

        self.main_window = tkinter.Tk()
        self.main_window.title("Create Project Python")
        # self.main_window.geometry("400x400")

        self.main_frame = tkinter.Frame(self.main_window)
        
        self.title = tkinter.Label(self.main_frame, text="Создать новый проект")
        self.current_folder = tkinter.Label(self.main_frame, text=f"Текущая дирректория: \n{self.folder_path_lite}")

        self.change_current_folder_button = tkinter.Button(
            self.main_frame, text="Изменить дирректорию", command=self.change_folder_method
        )

        self.enter_folder_name_label = tkinter.Label(self.main_frame, text="Введи имя нового проекта:")
        self.entry_folder_name = tkinter.Entry(self.main_frame)

        self.create_folder = tkinter.Button(self.main_frame, text="Создать новый проект", command=self.create_new_folder_method)

        self.title.pack(pady=(0, 20))
        self.current_folder.pack()
        self.change_current_folder_button.pack(pady=(20, 20))
        self.enter_folder_name_label.pack(pady=(20, 0))
        self.entry_folder_name.pack(pady=(0, 30))

        self.create_folder.pack(pady=(0, 30))

        self.main_frame.pack(pady=(10, 10), padx=(10, 10))

        tkinter.mainloop()

    def change_folder_method(self):
        self.main_frame.pack_forget()

        self.second_main_frame = tkinter.Frame(self.main_window)

        self.chande_folder_button = tkinter.Button(
            self.second_main_frame, text="Выбрать директорию", command=self.FolderMethod
        )

        self.button = tkinter.Button(self.second_main_frame, text="Сохранить изменения", command=self.commit_changes)
        self.quit_button = tkinter.Button(self.second_main_frame, text="Отмена", command=self.quitFromChangePageMethod)

        self.chande_folder_button.pack(pady=(10, 20))

        self.button.pack()
        self.quit_button.pack()

        self.second_main_frame.pack(padx=(10, 10), pady=(10, 10))

    def create_new_folder_method(self):
        self.folder_name = self.entry_folder_name.get()

        if self.folder_name == "":
            tkinter.messagebox.showinfo("Ошибка", "Вы не ввели названия дирректории!")
            return

        os.mkdir(self.folder_path + self.folder_name)

        tkinter.messagebox.showinfo(
            "Информация", "Дирректория успешно создана!"
        )

        os.chdir("..")
        os.chdir(self.folder_name)

        os.system("virtualenv .venv")

        Path(f"{self.folder_path + self.folder_name}/main.py").touch()

    def commit_changes(self):
        self.second_main_frame.pack_forget()
        self.main_frame.pack()

        try:
            if not self.path != "":
                print("Ok")
        except:
            tkinter.messagebox.showinfo(
                "Ошибка", "Выберите путь!"
            )

        self.folder_path = self.path
        self.folder_path_lite = self.path


        self.current_folder.config(text=rf"Текущая директория: \n{self.folder_path}")

    def quitFromChangePageMethod(self):
        self.second_main_frame.pack_forget()
        self.main_frame.pack(padx=(10, 10), pady=(10, 10))

    def FolderMethod(self):
        self.path = subprocess.getoutput("zenity --file-selection --directory")

        if "AmletixQ-fileSys" in self.path.split("/"):
            import createLitePath

            self.lite_path = createLitePath.create_lite_path(self.path)

            self.path = self.lite_path

if __name__ == "__main__":
    application = Application()